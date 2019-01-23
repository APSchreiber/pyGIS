# FFeatures With Data
# features_with_data.py

# Author: Andrew Schreiber
# Created: 10/29/18
# Modified: 11/9/18

'''
Find all features with data in a geodatabase and create report
'''

print "importing modules..."
import arcpy, os, sys, traceback, datetime, glob, csv


#####################################################################

# A geodatabase location
workspace = r""

# A csv file name (with full path) to be created as ouotput
out_file = r""

#####################################################################


try:

    # Initialize some variables
    layers_with_data = []

    # Set the workspace
    arcpy.env.workspace = workspace

    # List datasets
    datasets = arcpy.ListDatasets()
    
    # Loop through each dataset
    for dataset in datasets:
        
        # List feature classes
        print dataset
        arcpy.env.workspace = workspace + os.sep + dataset
        fcs = arcpy.ListFeatureClasses()
        
        # Get counts 
        for fc in fcs: 
            # Create a feature layer
            fl = fc + '_lyr'
            arcpy.MakeFeatureLayer_management(fc, fl)
            # Get a count of features in the layer
            count = arcpy.GetCount_management(fl).getOutput(0)

            # Add the layer name to list of layers that have some data
            row_dict = {}
            row_dict["Name"] = fc
            row_dict["Count"] = count

            layers_with_data.append(row_dict)
                
            # Print some results
            print fl, count
            # Delete feature layer
            arcpy.Delete_management(fl)
            
    print layers_with_data

    # Write the output to a CSV file
    f = open(out_file, "wb")
    writer = csv.DictWriter(
        f, fieldnames=["Name", "Count"])
    writer.writeheader()
    writer.writerows(layers_with_data)
    f.close()

    print "\nscript completed successfully."
    
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
    