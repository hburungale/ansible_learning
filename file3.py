import os
import shutil
pdfname=os.environ.get('CTMS_URL')
pdffilename = f"{pdfname}_PIR.pdf" 
destination_folder = "../reports/"
destination_path = os.path.join(destination_folder, pdffilename)
shutil.copy(pdffilename, destination_path)