# config tool
#config.py

# Horner and Shifrin
# Author: Andrew Schreiber
# Created: 6/17/13
# Modified: 1/22/19

print "importing modules..."
import os, sys, traceback, datetime, ConfigParser, time

start_time = datetime.datetime.now()

try:

    ###################################################################

    def get_config():

        # get variables from config file
        working_dir = os.getcwd()
        config = working_dir + os.sep + "example.config"
        parser = ConfigParser.SafeConfigParser()
        parser.read(config)

        test = parser.get("category1", "test")
        print test
        
    ###################################################################
        
    get_config()

    today = str(datetime.date.today())
    today_strip = today.replace("-", "")
    time = str(datetime.datetime.time(datetime.datetime.now()))


except Exception as e:
    print e.message
