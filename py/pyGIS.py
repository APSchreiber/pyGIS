# pyGIS
# pGIS.py

# Horner and Shifrin
# Author: Andrew Schreiber
# Created: 1/22/19
# Modified: 1/22/19

'''
Template description
'''

import arcpy, os, sys, traceback, datetime
print "importing modules..."

###################################################################

###################################################################


####################################################################

try:

    pass


except:

    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n     " + str(sys.exc_info()[1])
  
    msgs = "ARCPY ERRORS:\n" + arcpy.GetMessages(2) + "\n"
  
    arcpy.AddError(msgs)
    arcpy.AddError(pymsg)
  
    print msgs
    print pymsg
      
    arcpy.AddMessage(arcpy.GetMessages(1))
    print arcpy.GetMessages(1)
