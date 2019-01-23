# Geometry Vertices to 3D by Points 
# geomo_to_3d_by_point.py

# Horner and Shifrin
# Author: Andrew Schreiber, Kip Kritis
# Created: 1/22/19
# Modified: 1/23/19

'''
Takes elevation points, matches them to a geometrie's vertices, and assigns elevations to the vertices
'''

import arcpy, os, sys, traceback, datetime
print "importing modules..."

###################################################################

workspace = r"C:\Users\apschreiber\Dropbox\Projects\Git\pyGIS\py\test\test.gdb"

source_fc = 'Line2'
target_fc = 'Line1'

###################################################################


####################################################################

try:


    ###################################################################
    # Some test code
    ###################################################################

    # Set the workspace
    arcpy.env.workspace = workspace

    # Get the source geometry
    src_geometry = None
    with arcpy.da.SearchCursor(source_fc, ["SHAPE@",]) as s_cursor:
        for row in s_cursor:
            src_geometry = row[0]
        
            del row
            break
        del s_cursor

    # Update polyline geometries
    with arcpy.da.UpdateCursor(target_fc, ["SHAPE@",]) as u_cursor:
        for row in u_cursor:
            row[0] = src_geometry
            u_cursor.updateRow(row)

            del row

    ###################################################################
    ###################################################################


    ######## Pseudo-code ########

    # Create an update cursor for the target layer

    # Loop through each feature in the target layer

        # Get the feature's geometry object
        
        # Create an empty array to store new geometry object

        # Loop through each vertex in the geometry object

            # Get the XY of the vertex

            # Create an in-memory point geometry object from the XY coords

            # Select the point in the soure layer by the geometry object

            # Create a search cursor to get the selected point

            # Loop through to cursor to get the first row

                # Get the geometry of the selected point

                # Break the loop

            # Create an XYZ coord array based on the XY of the current source layer's row and the Z from the selected point

            # Add the new coordinate array to new geometry object

        # Set the feature's geometry to the new geometry object
            

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
