"""Use the progrma with GUI"""

import sys
import gi
from gi.repository import Gtk

import libs.Password as Password
import libs.WordDictionary as WordDictionary
import libs.cli_parser as CLI
import libs.Interface as GUI
import preferences as prefs

gi.require_version("Gtk", "3.0")

# ===================================

if __name__ == '__main__':
    GUI.GUI_prefs = prefs.current_prefs.copy()

    win = GUI.MainWindow()
    win = MainWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

    dictionary = WordDictionary.WordDictionary(DICT_PATH)
    sample_password = Password.WordPassword(dictionary, WORDS_IN_PASS, CAPITALIZE, SEPARATOR, NUMBERS_TO_INSERT)
    print(sample_password.password)