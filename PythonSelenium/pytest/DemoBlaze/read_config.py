from configparser import ConfigParser
import configparser

def get_config(category,key):
    config = ConfigParser()
    config.read("./config.ini")
    return config.get(category,key)