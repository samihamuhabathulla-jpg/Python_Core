from configparser import ConfigParser
import os

def get_config(category, key):
    config = ConfigParser()

    config_path = os.path.join(
        os.path.dirname(__file__),
        "config.ini"
    )

    print("Config path:", config_path)

    config.read(config_path)

    print("Sections:", config.sections())

    return config.get(category, key)