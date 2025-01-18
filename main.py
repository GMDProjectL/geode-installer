import os
from gi import require_version
require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from locales import get_text
from installer import install_geode

LANG = os.getenv('LANG', 'en_US.UTF-8')


class GeodeInstaller(Gtk.Window):
    def __init__(self):
        super().__init__(title=get_text('geode_installer', LANG))
        self.set_size_request(579, 300)
        self.set_resizable(False)
        self.set_border_width(10)
        self.game_directory = None
        self.installation_type = 'steam'

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(box)

        box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box.pack_start(box2, True, True, 0)

        radio_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        box2.pack_start(radio_box, True, True, 0)

        label1 = Gtk.Label(label=get_text('welcome', LANG))

        style_provider = Gtk.CssProvider()
        css = open('style.css') 
        css_data = css.read()
        css.close()

        style_provider.load_from_data(css_data)

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), style_provider, 
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        label1.get_style_context().add_class('title')

        gap = Gtk.Label(label='')
        label = Gtk.Label(label=get_text('choose_your_installation', LANG))
        radio_box.pack_start(label1, False, False, 0)
        radio_box.pack_start(gap, False, False, 0)
        radio_box.pack_start(label, False, False, 0)

        radio_button1 = Gtk.RadioButton(label=get_text('steam', LANG))
        radio_box.pack_start(radio_button1, False, False, 0)

        radio_button2 = Gtk.RadioButton(label=get_text('wine', LANG), group=radio_button1)
        radio_box.pack_start(radio_button2, False, False, 0)

        radio_button1.connect("toggled", self.on_radio_toggled, "steam")
        radio_button2.connect("toggled", self.on_radio_toggled, "wine")

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        box.pack_start(button_box, False, False, 0)

        install_button = Gtk.Button(label=get_text('install', LANG))
        install_button.connect("clicked", self.on_install_clicked)
        button_box.pack_start(install_button, True, True, 0)

        cancel_button = Gtk.Button(label=get_text('close', LANG))
        cancel_button.connect("clicked", self.on_cancel_clicked)
        button_box.pack_start(cancel_button, True, True, 0)

    def on_install_clicked(self, button):
        install_geode(self.installation_type, self.game_directory)

        dialog = Gtk.MessageDialog(
            parent=self, 
            flags=Gtk.DialogFlags.DESTROY_WITH_PARENT, 
            type=Gtk.MessageType.INFO, 
            buttons=Gtk.ButtonsType.OK, 
            message_format=get_text('finished', LANG)
        )

        dialog.run()
        dialog.destroy()

    def on_cancel_clicked(self, button):
        self.destroy()

    def on_radio_toggled(self, button, name):
        if button.get_active():
            print(name)
            self.installation_type = name
            if name == "wine":
                self.open_directory_picker()

    def open_directory_picker(self):
        dialog = Gtk.FileChooserDialog(title=get_text('select_game_directory', LANG), parent=self, action=Gtk.FileChooserAction.SELECT_FOLDER, buttons=(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.game_directory = dialog.get_filename()
            print(self.game_directory)
        dialog.destroy()


if __name__ == "__main__":
    window = GeodeInstaller()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()