from pdf2image import convert_from_path
import zipfile
import os

def zipextract(pth_zip):
    pt = []
    zipf = zipfile.ZipFile(pth_zip)
    for fl in zipf.infolist():
        pt.append(zipf.extract(fl))
    return pt

pth = zipextract("pdf.zip")

with zipfile.ZipFile('Images.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
    for pt,i in zip(pth,range(1,len(pth) + 1)):
        images = convert_from_path(pt)
        for img in images:
            img.save('Page no-' + str(i)+ '.PNG','PNG')
            zipf.write('Page no-' + str(i)+ '.PNG')
        os.remove(pt)
        os.remove('Page no-' + str(i)+ '.PNG')
