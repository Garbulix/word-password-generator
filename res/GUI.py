import gi
from gi.repository import Gtk

import res.InterfaceBridge

gi.require_version("Gtk", "3.0")

class MainWindow(Gtk.Window):
    """Main program's window with output field and clickable preferences"""
    # guitext_something - some kind of interface text, my step for making program international in the future
    guitext_window_label = "Word Password Generator 0.1"
    guitext_no_of_words = "Words in password"
    guitext_capitalize = "Capitalize words"
    guitext_separator = "Separator"
    guitext_numbers_to_insert = "Insert number"
    guitext_generate_button = "Generate password"
    guitext_select_dict = "Select dictionary"

    def __init__(self, controller):
        """creating window using InterfaceBridge object as MVC-ish controller"""

        # TODO check if every self. need to be self.

        self._controller = controller

        Gtk.Window.__init__(self, 
                            title=self.guitext_window_label,
                            resizable=False)
        self.set_border_width(10)
        self.set_size_request(500, 100)
        self.set_position(Gtk.WindowPosition.CENTER)

        # PASSWORD OUTPUT
        self.output = Gtk.Entry()
        self.output.set_text("")
        self.output.set_editable(False)

        # "GENERATE" BUTTON
        # TODO buttons:
        # - set colors
        # - add "copy to clipboard" and "reset clipboard"
        self.generate_button_box = Gtk.Box(spacing=10)
        self.generate_button = Gtk.Button.new_with_label(self.guitext_generate_button)
        self.generate_button.connect("clicked", self._on_generate_clicked)
        self.generate_button_box.pack_end(self.generate_button, False, False, 0)

        # PASSPHRASE PREFERENCES BIG VERTICAL BOX
        # TODO saving and loading previous states
        self.selected_dict_hbox = Gtk.Box(spacing=10)
        self.demanded_words_hbox = Gtk.Box(spacing=10)
        self.capitalize_hbox = Gtk.Box(spacing=10)
        self.separator_hbox = Gtk.Box(spacing=10)
        self.insert_number_hbox = Gtk.Box(spacing=10)

        self.passphrase_preferences_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
        self.passphrase_preferences_vbox.pack_start(self.selected_dict_hbox, False, False, 0)
        self.passphrase_preferences_vbox.pack_start(self.demanded_words_hbox, False, False, 0)
        self.passphrase_preferences_vbox.pack_start(self.capitalize_hbox, False, False, 0)
        self.passphrase_preferences_vbox.pack_start(self.insert_number_hbox, False, False, 0)
        self.passphrase_preferences_vbox.pack_start(self.separator_hbox, False, False, 0)

        ### selected dictionary box
        selected_dict_label = Gtk.Label(label=self.guitext_select_dict)
        select_dict_combo = Gtk.ComboBoxText()
        select_dict_combo.set_entry_text_column(0)
        select_dict_combo.connect("changed", self._on_dict_chosed)
        for dictionary in controller.get_available_dictionaries():
            select_dict_combo.append_text(dictionary)
        select_dict_combo.set_active(0) # TODO load from InterfaceBridge 
        self._on_dict_chosed(select_dict_combo)  # set dictionary
        self.selected_dict_hbox.pack_start(selected_dict_label, False, False, 0)
        self.selected_dict_hbox.pack_end(select_dict_combo, False, False, 0)

        ### demanded words box
        demanded_words_label = Gtk.Label(label=self.guitext_no_of_words)
        self.words_spin = Gtk.SpinButton()
        words_spin_adj = Gtk.Adjustment(value=controller.get_word_count(), 
                                        lower=1, 
                                        upper=12, 
                                        step_increment=1)
        self.words_spin.set_adjustment(words_spin_adj)
        self.words_spin.connect("value-changed", self._on_word_value_changed)
        self.demanded_words_hbox.pack_start(demanded_words_label, False, False, 0)
        self.demanded_words_hbox.pack_end(self.words_spin, False, False, 0)

        ### capitalize words box
        capitalize_label = Gtk.Label(label=self.guitext_capitalize)
        self.capitalize_switch = Gtk.Switch()
        self.capitalize_switch.connect("notify::active", self._on_capitalize_switch_toggled)
        self.capitalize_switch.set_active(self._controller.get_capitalize_mode())
        self.capitalize_hbox.pack_start(capitalize_label, False, False, 0)
        self.capitalize_hbox.pack_end(self.capitalize_switch, False, False, 0)

        ### insert number box
        insert_number_label = Gtk.Label(label=self.guitext_numbers_to_insert)
        self.insert_number_switch = Gtk.Switch()
        self.insert_number_switch.connect("notify::active", self._on_number_switch_toggled)
        self.insert_number_switch.set_active(self._controller.get_insert_number_mode())
        self.insert_number_hbox.pack_start(insert_number_label, False, False, 0)
        self.insert_number_hbox.pack_end(self.insert_number_switch, False, False, 0)

        ### chosed separator box
        separator_label = Gtk.Label(label=self.guitext_separator)
        separator_chose_box = Gtk.ComboBoxText()
        separator_chose_box.set_entry_text_column(0)
        separator_chose_box.connect("changed", self._on_separator_chosed)
        for separator in controller.get_recommended_separators():
            separator_chose_box.append_text(separator)
        separator_chose_box.set_active(0)   # TODO load from InterfaceBridge 
        self.separator_hbox.pack_start(separator_label, False, False, 0)
        self.separator_hbox.pack_end(separator_chose_box, False, False, 0)

        # PACKING ALL TOGETHER
        main_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(main_vbox)

        divider = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        
        main_vbox.pack_start(self.output, True, True, 0)
        main_vbox.pack_start(self.generate_button_box, True, True, 0)
        main_vbox.pack_start(divider, True, True, 0)
        main_vbox.pack_start(self.passphrase_preferences_vbox, True, True, 0)

    def _on_dict_chosed(self, combo):
        self._controller.set_arguments(dictionary_name=combo.get_active_text())

    def _on_word_value_changed(self, scroll):
        self._controller.set_arguments(word_count=self.words_spin.get_value_as_int())

    def _on_generate_clicked(self, button):
        self.output.set_text(self._controller.get_next_password())

    def _on_capitalize_switch_toggled(self, switch, gparam):
        self._controller.set_arguments(if_capitalize=switch.get_active())

    def _on_number_switch_toggled(self, switch, gparam):
        self._controller.set_arguments(if_insert_number=switch.get_active())

    def _on_separator_chosed(self, combo):
        self._controller.set_arguments(separator=combo.get_active_text())