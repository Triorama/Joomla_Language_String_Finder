import argparse
import configparser
import os
import re
import datetime

# Definition of search function
def search(directory, prefix, exclusion_folders):

    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        log(path)
        if os.path.isdir(path) and filename not in exclusion_folders:
            search(path, prefix, exclusion_folders)
        elif os.path.isfile(path):
            with open(path, "r") as f:
                inhalt = f.read()
                for match in SEARCHPATTERN.finditer(inhalt):
                    string = match.group()
                    # Check, if String is already present in INI-File
                    if not string in open(output_file, "r").read():
                        log(f"String found: {string}")

                        with open(output_file, "a") as f:
                            f.write(f"{string} = \"{string}\"\n")

# Definition of Logfunction
def log(message):
    with open(log_file, "a") as f:
        f.write( message + "\n")

def load_configuration(path_ini_file):
    """
    Loads Configuration from INI File in key=value-Format.

    Args:
        path_ini_file: The path to INI-File.

    Returns:
        A Dictionary with loaded Configuration-Parameters.
    """

    config = {}
    with open(path_ini_file, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()

    return config
# Argumentparser
parser = argparse.ArgumentParser(description="Skript zur Suche nach Strings in einem Verzeichnisbaum")

parser.add_argument("-c", "--config", help="Der path zur Konfigurationsdatei.", required=False)

# Parse the Arguments
args = parser.parse_args()

FILEPATH = os.path.dirname(__file__)
# Automatische Suche nach einer config.ini-Datei im aktuellen Verzeichnis, wenn keine angegeben wurde
if not args.config:
    args.config = os.path.join(FILEPATH, "config.ini")

# Load Configuration
config = load_configuration(args.config)

# Extract the Configurationparameter
search_folder = os.path.join(FILEPATH,config["search_folder"])
prefix = config["prefix"]
exclusion_folders = config["exclusion_folders"].split(",")
output_file = os.path.join(FILEPATH,config["output_file"])
log_file = os.path.join(FILEPATH,config["log_file"])

# Searchpattern
SEARCHPATTERN = re.compile(r"{0}_[A-Z0-9_]+".format(prefix))

# Start of Script
log("**Start of Script**")
search(search_folder, prefix, exclusion_folders)
log("**End of Script**")
