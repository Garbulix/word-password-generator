import gi
import sys

import WordDictionary
import Password

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

"""
TODO:
- use DICT_PATH in more elegant way
- change available numbers to one switch
- use it as a module for main.py
- just clean up the mess
"""


DICT_PATH = "./dictionaries/POLISH.txt"

class MainWindow(Gtk.Window):
    #
    # guitext_(blahblah) - some kind of interface text, first step for making program international 
    #
    guitext_window_label = "Word Password Generator 0.1"
    guitext_no_of_words = "Liczba słów"
    guitext_capitalize = "Duże pierwsze litery"
    guitext_separator = "Separator słów"
    guitext_numbers_to_insert = "Losowe cyfry"
    guitext_generate_button = "Generuj hasło"
    

    def __init__(self):
        Gtk.Window.__init__(self, 
            title=self.guitext_window_label,
            resizable=False)
        self.set_border_width(10)
        self.set_size_request(500, 100)
        self.set_position(Gtk.WindowPosition.CENTER)

        default_number_of_words = 4
        self.demanded_words = default_number_of_words
        self.capitalize = False
        self.separator = "-"
        self.numbers_to_insert = 0
        self.available_separators = ["-", "_", "*", "#"]
        self.available_numbers = [i for i in range(0, 13)]

        main_vertical_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.output = Gtk.Entry()
        self.output.set_text("")
        self.output.set_editable(False)
        
        demanded_words_box = Gtk.Box(spacing=10)
        capitalize_box = Gtk.Box(spacing=10)
        separator_box = Gtk.Box(spacing=10)
        numbers_to_insert_box = Gtk.Box(spacing=10)
        generate_button_box = Gtk.Box(spacing=10)

        self.add(main_vertical_box)
        main_vertical_box.pack_start(self.output, True, True, 0)
        main_vertical_box.pack_start(demanded_words_box, True, True, 0)
        main_vertical_box.pack_start(capitalize_box, True, True, 0)
        main_vertical_box.pack_start(separator_box, True, True, 0)
        main_vertical_box.pack_start(numbers_to_insert_box, True, True, 0)
        main_vertical_box.pack_start(generate_button_box, True, True, 0)

        demanded_words_label = Gtk.Label(label=self.guitext_no_of_words)
        demanded_words_box.pack_start(demanded_words_label, False, False, 0)
        self.words_spin = Gtk.SpinButton()
        words_spin_adjustment = Gtk.Adjustment(value=default_number_of_words, 
            lower=1, upper=12, step_increment=1)
        self.words_spin.set_adjustment(words_spin_adjustment)
        self.words_spin.connect("value-changed", self.on_word_value_changed)
        demanded_words_box.pack_end(self.words_spin, False, False, 0)

        capitalize_label = Gtk.Label(label=self.guitext_capitalize)
        capitalize_box.pack_start(capitalize_label, False, False, 0)
        capitalize_switch = Gtk.Switch()
        capitalize_switch.connect("notify::active", self.on_switch_toggled)
        capitalize_box.pack_end(capitalize_switch, False, False, 0)

        separator_label = Gtk.Label(label=self.guitext_separator)
        separator_box.pack_start(separator_label, False, False, 0)
        separator_combo = Gtk.ComboBoxText()
        separator_combo.set_entry_text_column(0)
        separator_combo.connect("changed", self.on_separator_combo_changed)
        for separator in self.available_separators:
            separator_combo.append_text(separator)
        separator_combo.set_active(0)
        separator_box.pack_end(separator_combo, False, False, 0)

        numbers_to_insert_label = Gtk.Label(label=self.guitext_numbers_to_insert)
        numbers_to_insert_box.pack_start(numbers_to_insert_label, False, False, 0)
        numbers_to_insert_combo = Gtk.ComboBoxText()
        numbers_to_insert_combo.set_entry_text_column(0)
        numbers_to_insert_combo.connect("changed", self.on_numbers_combo_changed)
        for number in self.available_numbers:
            numbers_to_insert_combo.append_text(str(number))
        numbers_to_insert_combo.set_active(0)
        numbers_to_insert_box.pack_end(numbers_to_insert_combo, False, False, 0)

        generate_button = Gtk.Button.new_with_label(self.guitext_generate_button)
        generate_button.connect("clicked", self.on_generate_clicked)
        generate_button_box.pack_end(generate_button, False, False, 0)

    def on_word_value_changed(self, scroll):
        self.demanded_words = self.words_spin.get_value_as_int()

    def on_generate_clicked(self, button):
        dictionary = WordDictionary.WordDictionary(DICT_PATH)
        new_password = Password.WordPassword(
            dictionary, 
            self.demanded_words, 
            self.capitalize, 
            self.separator, 
            self.numbers_to_insert)
        self.output.set_text(new_password.password)

    def on_switch_toggled(self, switch, gparam):
        self.capitalize = switch.get_active()

    def on_separator_combo_changed(self, combo):
        self.separator = combo.get_active_text()

    def on_numbers_combo_changed(self, combo):
        self.numbers_to_insert = int(combo.get_active_text())

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()