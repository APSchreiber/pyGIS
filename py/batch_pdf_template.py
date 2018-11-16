# Batch PDF Template
# batch_pdf.py

# Horner and Shifrin
# Author: Andrew Schreiber
# Created: 6/1/2018
# Modified: 6/1/2018

'''
Batch PDF Template
'''

print "importing modules..."
import arcpy, os, sys, traceback, datetime, csv


#####################################################################

workspace = r""

title_text = "Vertical Clearance Diagram"

template = "template.mxd"
info_csv = "info.csv"
output_dir = "output"
input_dir = "input"

#####################################################################

def set_image(img_src, elem_name):
    img_item = arcpy.mapping.ListLayoutElements(mxd, "PICTURE_ELEMENT", elem_name)[0]
    img_item.sourceImage = img_src

def set_text(text, elem_name):
    # change title text
    titleItem = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", elem_name)[0]
    titleItem.text = text

try:
    arcpy.env.workspace = r"O:\GIS\Tools\Scripts\py\batch_pdf"
    arcpy.env.overwriteOutput = True
    mxd = arcpy.mapping.MapDocument(template)

    info_dict = {}
    with open(info_csv, mode='r') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            info_dict[row['STRUCTURE']] = row

    
  
    dirs = os.listdir(input_dir)
    
    for d in dirs:
        print d

        try:
            doc_info = info_dict[d]
        except:
            continue

        files = os.listdir(input_dir + os.sep + d)

        for f in files:

            print "Setting Images..."
            
            print f

            # set images
            if "_nb.png" in f.lower():
                set_image(input_dir + os.sep + d + os.sep + f, "image1", )
                set_text("Looking NORTH on {}".format(doc_info['TRAVELWAY']), "text1")
                
            if "_wb.png" in f.lower():
                set_image(input_dir + os.sep + d + os.sep + f, "image1")
                set_text("Looking EAST on {}".format(doc_info['TRAVELWAY']), "text2")              
                  
            if "_sb.png" in f.lower():
                set_image(input_dir + os.sep + d + os.sep + f, "image2")
                set_text("Looking SOUTH on {}".format(doc_info['TRAVELWAY']), "text2")
                
            if "_eb.png" in f.lower():
                set_image(input_dir + os.sep + d + os.sep + f, "image2")
                set_text("Looking WEST on {}".format(doc_info['TRAVELWAY']), "text1")
                
            if "_cloud_w_meas.png" in f.lower():
                set_image(input_dir + os.sep + d + os.sep + f, "image3")
                set_text("Looking WEST on {}".format(doc_info['TRAVELWAY']), "meas")

            if "_cloud_e_meas.png" in f.lower():
                set_image(input_dir + os.sep + d + os.sep + f, "image3")
                set_text("Looking EAST on {}".format(doc_info['TRAVELWAY']), "meas")

            if "_cloud_n_meas.png" in f.lower():
                set_image(input_dir + os.sep + d + os.sep + f, "image3")
                set_text("Looking NORTH on {}".format(doc_info['TRAVELWAY']), "meas")

            if "_cloud_s_meas.png" in f.lower():
                set_image(input_dir + os.sep + d + os.sep + f, "image3")
                set_text("Looking SOUTH on {}".format(doc_info['TRAVELWAY']), "meas")
              
            print "Setting text fields..." 


            # set the fedid
            try:
                doc_info = info_dict[d]
                set_text("FED ID: {}".format(doc_info['FEDID']), 'fed')
            except:
                pass

            # set the structure
            try:
                set_text("STRUCTURE: {}".format(doc_info['STRUCTURE']), 'structure')
            except:
                pass

            # set the route
            try:
                set_text("ROUTE: {}".format(doc_info['TRAVELWAY']), 'route')
            except:
                pass

            # set the features
            try:
                doc_info = info_dict[d]
                set_text("FEATURES: {}".format(doc_info['FEATURE INTERSECTED']), 'feat')
            except:
                pass

            # set the date
            
            try:
                doc_info = info_dict[d]
                set_text("DATE: {}".format(doc_info['Date Measured']), 'Date')
            except:
                pass
	   
                
            # change title text
            set_text(title_text, "title")

            # export to pdf
            out_pdf = output_dir + os.sep + d + ".pdf"
            print out_pdf
            arcpy.mapping.ExportToPDF(mxd, out_pdf)                
    
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
    
