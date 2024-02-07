# Find untranslated languagestrings in Joomla component

While deveolping an Joomla Component I noticed, that it is hard to find all untranslated strings. The "Untranslated strings designer" mentioned on this site: https://docs.joomla.org/Debugging_a_translation seems not to work for the backend. So i decided to make this little Helper script.

**How it works**
This script recursively searches a directory tree and all subdirectories for files that contain the search string. Found strings are appended to an INI file and logged in a log file.

**Features:**

- Recursive search of a directory tree
- Configurable search string
- Exclusion of specific folders
- Logging of found strings
- Automatic search for a config.ini file

**Usage:**

1. Create a config.ini file with the following parameters:

```
search_folder = ../Path/to/search/folder
prefix = PREFIX
exclusion_folders = language
output_file = ./path/to/language/file.ini
log_file = ./path/to/log.txt
```

All pathes are relative to location of the Scriptfile.

2. Run the script with the following command:

```
python script.py
```

Without an Option it automaticly searches for a config.ini file in the folder of the script file.
**Options:**

- `-c, --config`: The path to the configuration file.

**Example:**

```
python script.py -c config.ini
```

You can create multiple configuration-files i.e. config-site.ini and config-admin.ini to differentiate between site and admin language files.
**Notes:**

- The exclusion folders are comma-separated.
- The output file is an INI file.
- The log file is a text file.

**Further Information:**

- INI files: [https://en.wikipedia.org/wiki/INI_file](https://en.wikipedia.org/wiki/INI_file)
- Python configuration: [https://docs.python.org/3/library/configparser.html](https://docs.python.org/3/library/configparser.html)
- argparse module: [https://docs.python.org/3/library/argparse.html](https://docs.python.org/3/library/argparse.html)
