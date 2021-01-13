"""
Class for handling functions under the hood.
It's purpose is making any interface creation easy.
"""

import os

import res.Password as Password
import res.WordDictionary as wd

IB_DEFAULTS = {"dictionaries_path": "./res/dictionaries/",
               "dictionary": "NOT_SET",
               "word_count": 4,
               "separator": "-",
               "capitalize": False,
               "insert_number": False,
               "recommended_separators": ["-", "_", "*", "#"]}

class InterfaceBridge():
    def __init__(self):
        self._dictionaries_path = IB_DEFAULTS["dictionaries_path"]
        self._dictionaries = {}
        self._word_count = IB_DEFAULTS["word_count"]
        self._chosen_dict = IB_DEFAULTS["dictionary"]
        self._chosen_separator = IB_DEFAULTS["separator"]
        self._if_capitalize = IB_DEFAULTS["capitalize"]
        self._if_insert_number = IB_DEFAULTS["insert_number"]

        self._dictionaries = self._import_dictionaries()

    def get_available_dictionaries(self):
        """return list with available dictionaries"""

        return self._dictionaries.keys()

    def get_recommended_separators(self):
        """return list with recommended separators to use"""
        
        return IB_DEFAULTS["recommended_separators"] 

    def get_next_password(self):
        """create passphrase with preferences set earlier and return it"""

        new_password = Password.WordPassword(dictionary=self._dictionaries[self._chosen_dict],
                                             no_of_words=self._word_count,
                                             capitalize=self._if_capitalize,
                                             separator=self._chosen_separator,
                                             numbers_to_insert=int(self._if_insert_number))

        return str(new_password.password)

    def get_another_password(self,
                             dictionary_name,
                             word_count,
                             separator,
                             if_insert_number,
                             if_capitalize):
        """create passphrase using given preferences (ignoring previously set prefs)"""
        # TODO create it, it's just an idea at the moment

        return "your-mom"

    def set_arguments(self, 
                      dictionary_name=None,
                      word_count=None,
                      separator=None,
                      if_insert_number=None,
                      if_capitalize=None):
        """set password/passphrase preferencies"""
        # TODO arguments validation

        if dictionary_name != None:
            self._chosen_dict = dictionary_name
        if word_count != None:
            self._word_count = word_count
        if separator != None:
            self._chosen_separator = separator
        if if_insert_number != None:
            self._if_insert_number = if_insert_number
        if if_capitalize != None:
            self._if_capitalize = if_capitalize

    def get_chosen_dictionary(self):
        """get name of currently used dictionary"""

        return self._chosen_dict

    def get_word_count(self):
        """return number of words in new password"""

        return self._word_count
    
    def get_chosen_separator(self):
        """return chosen separator"""

        return self._chosen_separator

    def get_capitalize_mode(self):
        """return bool that informs if words in new password will be capitalized"""

        return self._if_capitalize

    def get_insert_number_mode(self):
        """get info about inserting number activation (returned bool value)"""

        return self._if_insert_number

    def _import_dictionaries(self):
        """import all dictionary files from default directory.
        Function doesn't verify whether file is correct.
        In current stage, in the directory should only be dictionary files
        TODO some kind of veryfing directory"""

        dictionary_list = os.listdir(self._dictionaries_path)
        dictionaries = {}

        # import all dicts in directory
        for dictionary_name in dictionary_list:
            imported_dict = wd.WordDictionary(str(self._dictionaries_path + dictionary_name))
            dictionaries[dictionary_name] = imported_dict

        # set first dictionary in keys() list as default
        self._chosen_dict = list(dictionaries.keys())[0]

        return dictionaries