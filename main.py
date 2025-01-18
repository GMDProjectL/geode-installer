from gi import require_version
require_version("Gtk", "3.0")
from gi.repository import Gtk


class GeodeInstaller(Gtk.Window):
    def __init__(self):
        super().__init__(title="Geode Installer")
        self.set_default_size(400, 300)
        self.set_border_width(10)

        self.set_title("Geode Installer")

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(box)

        label = Gtk.Label(label="Welcome to Geode Installer")
        box.pack_start(label, True, True, 0)

        button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        box.pack_start(button_box, False, False, 0)

        install_button = Gtk.Button(label="Install")
        install_button.connect("clicked", self.on_install_clicked)
        button_box.pack_start(install_button, True, True, 0)

        cancel_button = Gtk.Button(label="Cancel")
        cancel_button.connect("clicked", self.on_cancel_clicked)
        button_box.pack_start(cancel_button, True, True, 0)

    def on_install_clicked(self, button):
        print("Install button clicked")

    def on_cancel_clicked(self, button):
        self.destroy()

if __name__ == "__main__":
    window = GeodeInstaller()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()