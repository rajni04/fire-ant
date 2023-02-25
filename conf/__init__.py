import logging
import tomllib

from constants import BASE_DIR

logger = logging.getLogger(__name__)


def get_config_file():
    """Get the config file path"""
    cf = BASE_DIR.joinpath("config.toml")
    if cf.exists():
        return cf
    cf = BASE_DIR.joinpath("config.toml.example").rename(cf)
    return cf


def load():
    """Load the settings from the config file"""

    config_file = get_config_file()
    with open(str(config_file), "rb") as f:
        t = tomllib.load(f)
        logger.debug("Settings loaded successfuly")
    return t


# This is to have only one instance of the settings
SETTINGS = load()
