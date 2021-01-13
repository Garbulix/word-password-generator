"""
Store program configurations, such as default dictionary, preferred 
number of words, available separators for GUI etc.
TODO: savable state
"""

DEFAULT_DICT_PATH = "./dictionaries/"
DICT_EXTENSION = ".txt"

def generate_dict_path(dict_name):
    return  str(DEFAULT_DICT_PATH + dict_name + DICT_EXTENSION)


default_prefs = {"dictionary": "",
                 "no_of_words": 4,
                 "separator":"-",
                 "capitalize": False,
                 "insert_number": False}
default_prefs["dictionary"] = generate_dict_path("ENGLISH-LONG")


GUI_availables = {"dicts": ["ENGLISH-LONG", "ENGLISH-UNIQUE", "POLISH"],
                  "separators": ["-", "_", "*", "#"]}

GUI_prefs = default_prefs.copy()


