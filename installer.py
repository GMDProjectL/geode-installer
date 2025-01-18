import psutil
import requests
import zipfile
import os
import vdf
import json
from typing import Literal


def get_latest_releases():
    url = "https://api.github.com/repos/geode-sdk/geode/releases"
    response = requests.get(url)
    return response.json()

def get_windows_zip_link():
    latest_releases = get_latest_releases()
    assets = latest_releases[0]["assets"]

    win_zip_release_link = ""

    for asset in assets:
        if "win.zip" in asset["name"]:
            win_zip_release_link = asset["browser_download_url"]
    
    return win_zip_release_link

def unzip_to_destination(zip_url, destination_dir):
    zip_response = requests.get(zip_url, stream=True)
    zip_file_path = os.path.join(destination_dir, "geode_win.zip")
    with open(zip_file_path, 'wb') as f:
        for chunk in zip_response.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_dir)
    os.remove(zip_file_path)

def install_to_dir(dir: str):
    win_zip_release_link = get_windows_zip_link()
    unzip_to_destination(win_zip_release_link, dir)

def tweak_wine_registry():
    locales_dir = os.path.dirname(os.path.abspath(__file__))
    wine_registry_path = os.path.join(locales_dir, "wine_reg.reg")
    os.system(f"wine regedit {wine_registry_path}")

def tweak_steam_lauch_options():
    userdata_dir = f'{os.getenv('HOME')}/.steam/steam/userdata'
    user_id = ''

    for dir in os.listdir(userdata_dir):
        user_id = dir
    
    config = f'{userdata_dir}/{user_id}/config/localconfig.vdf'

    with open(config, 'r') as f:
        config_data = vdf.load(f)
    
    apps = config_data['UserLocalConfigStore']['Software']['Valve']['Steam']['apps']
    
    try:
        gd_config = apps['322170']
        print(json.dumps(gd_config))
    except:
        apps['322170'] = {}
    
    config_data['UserLocalConfigStore']['Software']['Valve']['Steam']['apps']['322170']['LaunchOptions'] = 'WINEDLLOVERRIDES="XInput1_4.dll=n,b" %command%'

    print(json.dumps(gd_config))
    
    vdf.dump(config_data, open(config,'w'), pretty=True)

def get_steam_gd_path():
    steamapps = f'{os.getenv('HOME')}/.steam/steam/steamapps/common/Geometry Dash'
    return steamapps

def check_steam_running():
    steam_process = None
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == 'steam':
            steam_process = proc
            break
    
    return steam_process is not None

def install_geode(variant: Literal['wine'] | Literal['steam'], wine_path: str | None = None):
    print(f'Installing for: {variant}')

    if variant == 'wine':
        install_to_dir(wine_path)
        tweak_wine_registry()

    elif variant == 'steam':
        gd_steam_path = get_steam_gd_path()
        install_to_dir(gd_steam_path)
        tweak_steam_lauch_options()

    else:
        raise ValueError('Invalid variant. Please choose either "wine" or "steam".')


if __name__ == '__main__':
    print(check_steam_running())