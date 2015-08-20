"""
    This file contains all the constants that are used throughout the program.
    All the values are read from config.ini file.
"""

import ConfigParser
from errorCodes import *

DEJAVU_SECTION = "Dejavu"
SQL_SECTION = "Sql"
GENERATE_SECTION = "Generate"
RECOGNIZE_SECTION = "Recognize"
WEB_SECTION = "Web"

Config = ConfigParser.ConfigParser()
Config.read('../config.ini')

def ConfigRead(section):
    
    """ 
        Used to read the desired section from the file.
        Returns: dictionary of name:value pairs present in the section of the config file
    """
    
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None

    return dict1

def ConfigWrite(section, name, value):
    
    """
        Updates the config file with a particular value, in the required section and name
    """
    
    Config.set(section, name, value)

#For dejavu
try:
    CONFIG = {
        "database": {
            "host": ConfigRead(SQL_SECTION)['host'],
            "user": ConfigRead(SQL_SECTION)['user'],
            "passwd": ConfigRead(SQL_SECTION)['passwd'],
            "db": ConfigRead(SQL_SECTION)['db']
        }
    }
    
except:
    #If the config file is being read from django, then it needs a different location
    Config.read('../../config.ini')
    CONFIG = {
        "database": {
            "host": ConfigRead(SQL_SECTION)['host'],
            "user": ConfigRead(SQL_SECTION)['user'],
            "passwd": ConfigRead(SQL_SECTION)['passwd'],
            "db": ConfigRead(SQL_SECTION)['db']
        }
    }

DJV_CONFIDENCE = ConfigRead(DEJAVU_SECTION)['confidence_field']
DJV_SONG_NAME = ConfigRead(DEJAVU_SECTION)['song_name_field']
DJV_OFFSET = ConfigRead(DEJAVU_SECTION)['offset_field']

try:
    CONFIDENCE_THRESH = int(ConfigRead(DEJAVU_SECTION)['confidence'])
except:
    print "Confidence thresh has to be integer"
    raise ValueError(CONFIG_DTYPE_MISMATCH_ERROR)
    
#For generate.py
DB_FOLDER = ConfigRead(GENERATE_SECTION)['db_folder']
DB_AUDIO = DB_FOLDER + ConfigRead(GENERATE_SECTION)['db_audio']
DB_VIDEO = DB_FOLDER + ConfigRead(GENERATE_SECTION)['db_video']
DBNAME = ConfigRead(GENERATE_SECTION)['dbname']

VIDEO_EXT = ConfigRead(GENERATE_SECTION)['video_ext']
AUDIO_EXT = ConfigRead(GENERATE_SECTION)['audio_ext']

#For recognize.py
OUTPUT = ConfigRead(RECOGNIZE_SECTION)['output']

#in seconds
try:
    VIDEO_SPAN = int(ConfigRead(RECOGNIZE_SECTION)['video_span'])
except:
    print "video span has to be integer"
    raise ValueError(CONFIG_DTYPE_MISMATCH_ERROR)

try:    
    VIDEO_GAP = int(ConfigRead(RECOGNIZE_SECTION)['video_gap'])
except:
    print "video gap has to be integer"
    raise ValueError(CONFIG_DTYPE_MISMATCH_ERROR)
    
TEMP_VIDEO = ConfigRead(RECOGNIZE_SECTION)['temp_video']
TEMP_AUDIO = ConfigRead(RECOGNIZE_SECTION)['temp_audio']

#For fileHandler
UNCLASSIFIED_CONTENT = ConfigRead(RECOGNIZE_SECTION)['unclassified_content']

#For web content
WEB_VIDEO_NAME = ConfigRead(WEB_SECTION)['web_video_name']
WEB_LABELS = ConfigRead(WEB_SECTION)['web_labels']
