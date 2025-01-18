pkgname=geode-installer
pkgver=1.0
pkgrel=1
pkgdesc="Install Geometry Dash Modloader"
arch=('any')
url="https://github.com/GMDProjectL/geode-installer"
license=('GPL')
depends=('python-gobject' 'gtk3' 'python-requests' 'python-vdf')
makedepends=()
checkdepends=()
optdepends=()
backup=()
options=()
install=
source=("git+file://${PWD}")



package() {
  mkdir -p "$pkgdir/opt/geode-installer"
  install -Dm7777 "$srcdir/main.py" "$pkgdir/opt/geode-installer"
  install -Dm7777 "$srcdir/style.css" "$pkgdir/opt/geode-installer"
  install -Dm7777 "$srcdir/wine_reg.reg" "$pkgdir/opt/geode-installer"
  install -Dm7777 "$srcdir/installer.py" "$pkgdir/opt/geode-installer"
  install -Dm7777 "$srcdir/geode-installer.png" "$pkgdir/opt/geode-installer"
  install -Dm7777 "$srcdir/locales/__init__.py" "$pkgdir/opt/geode-installer/locales"
  install -Dm7777 "$srcdir/locales/en.json" "$pkgdir/opt/geode-installer/locales"
  install -Dm7777 "$srcdir/locales/ru.json" "$pkgdir/opt/geode-installer/locales"
  install -Dm0644 $srcdir/geode-installer.desktop -t "${pkgdir}/usr/share/applications"
}