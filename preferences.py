"""Store program preferences, such as default dictionary, preferred 
number of words etc."""

default_prefs = {"dictionary": "english-long",
                 "no_of_words": 4,
                 "separator":"-",
                 "capitalize": False,
                 "insert_number": False}

dict_paths = {"polish": "./dictionaries/POLISH.txt",
              "english-long": "./dictionaries/ENGLISH-LONG.txt",
              "english-unique": "./dictionaries/ENGLISH-UNIQUE.txt"}

# TODO ability to create custom, savable preferences
saved_prefs = default_prefs.copy()

# place dictionary path insted its name
used_prefs = default_prefs.copy()