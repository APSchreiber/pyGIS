# Send Result to Email

# Horner and Shifrin
# Author: Andrew Schreiber
# Created: 6/17/13
# Modified: 11/16/18

print "importing modules..."
import arcpy, os, sys, traceback, datetime, ConfigParser, time

start_time = datetime.datetime.now()

try:

    # Get variables from config file
    working_dir = os.getcwd()
    config = working_dir + os.sep + "export_to_gdb_config.txt"
    parser = ConfigParser.SafeConfigParser()
    parser.read(config)

    to_addr = parser.get("email", "to_addr")
    from_addr = parser.get("email", "from_addr")
    subject = parser.get("email", "subject")
    ip = parser.get("email", "ip")
    port = parser.get("email", "port")

    title = parser.get("log", "title")
    process_name = parser.get("log", "process_name")

    in_dir = parser.get("dirs", "in_dir")
    in_files = os.listdir(in_dir)
    in_GDBs = []
    for each in in_files:
        if str(each)[-4:] == ".sde":
            in_GDBs.append(each)

    today = str(datetime.date.today())
    today_strip = today.replace("-", "")
    time = str(datetime.datetime.time(datetime.datetime.now()))


except Exception as e:
    print e.message