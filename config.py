import os
import shutil
import traceback
import configparser

# Singleton config class

class Config:
    config = configparser.ConfigParser()
    for inifile in [os.path.expanduser('~')+'/.bayohwoolph.ini','bayohwoolph.local.ini','bayohwoolph.ini']:
        if os.path.isfile(inifile):
            config.read(inifile)
            break # First config file wins
    MAIN = config['MAIN']
