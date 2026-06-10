from configparser import ConfigParser
import os

config = ConfigParser()
path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"Configurations","config.ini")
config.read(path)

def get_data(section, key):
    return config.get(section, key)