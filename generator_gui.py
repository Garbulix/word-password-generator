"""word-password-generator with GUI interface"""

import gi
from gi.repository import Gtk

gi.require_version("Gtk", "3.0")

import res.GUI as GUI
import res.InterfaceBridge as controller

program = controller.InterfaceBridge()

win = GUI.MainWindow(program)
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()