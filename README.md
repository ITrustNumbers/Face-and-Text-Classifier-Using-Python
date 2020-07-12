# Image-adn-Text-Classifier

A simple approach to computer vision for differentiating between text and faces in an image using Opencv, Tesseract-OCR with python Wrapper Pytesseract and Pillow. In this project I used a dataset of 17 images of newspapers pages with various article and text, and then I used opencv to detect all the faces and pytesseract to extract the text and cached them in a global Data Structure to create a tool that given a "Keyword" will search through all the pages and return a contact sheet of all the faces from the pages in which the "Keyword" was found.

## How to use the Source Code Your Self

# Requriments:

   * Google Tesseract-OCR with Engling Language
   
   * Python3
   
   * Jupyter Notebook(Optional)
   
   * Pytesseract Python wrapper
   
   * OpenCV, python Library
   
   * Pillow, python Library
   
   * Additional if you want to use the PDF to PNG Converter:
     * pdf2image, python Library
     
 # Procedure:
   * First Run the Source Code or the Jupyter Notebook inside the Jupyter Notbook directory to ensure that the everthing is setup correctly
   * Match the output with the HTML fill provided inside the Notebook directory
   * Then if you want to use your own sample images then replace your .PNG images with mine inside the readonly/Images.zip directory and the run the Source code again
   * But to have better quality PNG download your sample images in pdf fromat from the internet and then first delete the Images.zip directory and then replace your pdfs inside readonly/pdf.zip with mine and then run the PDF-PNG.py script and it will conver all the pdf inside the pdf.zip into .PNG  images and store them inside the Images.zip directory and then run the Source Code
