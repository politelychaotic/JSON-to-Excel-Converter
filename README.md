# JSON-to-Excel-Converter

This Python program takes JSON data and interprets it as a Dict data type. After this, the program will iterate through layers of Dict objects and List objects (even nested ones, though if it is too nested it may not turn out as expected). This is to mimic a JSON report that has lots of data that is nested in different ways, with dict keys to data, dict keys to dicts, dict keys to lists, etc.
