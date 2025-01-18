pkgname=geode-installer
pkgver=1.0
pkgrel=1
pkgdesc="Install Geometry Dash Modloader"
arch=('any')
url="https://github.com/GMDProjectL/geode-installer"
license=('GPL')
depends=('python-gobject' 'gtk3' 'python-requests' 'python-vdf' 'python-psutil')
makedepends=()
checkdepends=()
optdepends=()
backup=()
options=()
install=
source=("git+file://${PWD}")



package() {
  mkdir -p "$pkgdir/opt/geode-installer"
  mkdir -p "$pkgdir/opt/geode-installer/locales"
  install -Dm7777 "$srcdir/geode-installer/main.py" "$pkgdir/opt/geode-installer"
  install -Dm7777 "$srcdir/geode-installer/style.css" "$pkgdir/opt/geode-installer"
  install -Dm7777 "$srcdir/geode-installer/wine_reg.reg" "$pkgdir/opt/geode-installer"
  install -Dm7777 "$srcdir/geode-installer/installer.py" "$pkgdir/opt/geode-installer"
  install -Dm7777 "$srcdir/geode-installer/geode-installer.png" "$pkgdir/opt/geode-installer"
  install -Dm7777 "$srcdir/geode-installer/locales/__init__.py" "$pkgdir/opt/geode-installer/locales/"
  install -Dm7777 "$srcdir/geode-installer/locales/en.json" "$pkgdir/opt/geode-installer/locales/"
  install -Dm7777 "$srcdir/geode-installer/locales/ru.json" "$pkgdir/opt/geode-installer/locales/"
  install -Dm0644 $srcdir/geode-installer/geode-installer.desktop -t "${pkgdir}/usr/share/applications"
}