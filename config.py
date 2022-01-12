import os
import shutil
import traceback
import configparser
import logging
logger = logging.getLogger('bayohwoolph.config')

# Singleton config class

class Config:
    config = configparser.ConfigParser()
    for inifile in [os.path.abspath('C:\Users\Zach\Documents\GitHub\Bay-Oh-Woolph')+'bayohwoolph.local.ini','bayohwoolph.ini']:
        if os.path.isfile(inifile):
            logger.info('reading config file: ' + inifile)
            config.read(inifile)
            break # First config file wins
    MAIN = config['MAIN']
    
    # pull debug level from config
    debug = MAIN.getint('debug',3)

    # Set up log level based on debug level
    if debug >= 3:
        logging.basicConfig(level=logging.DEBUG)
    elif debug >= 2:
       logging.basicConfig(level=logging.INFO)
    elif debug >= 1:
       logging.basicConfig(level=logging.WARNING)
    else:
       logging.basicConfig(level=logging.ERROR)
