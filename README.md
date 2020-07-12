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
   * First i have the images that i used in the readonly/Images directory and you can choose to use those if you want to just run and experiment with the code
   * To run the Soucre code first you have to compress the Images directory to Images.zip and save it in the readonly dirctory otherwise you can save it anywhere but you will have to change the source code to add the correct path to the Images.zip folder
   * If you are done setting up the Images.zip folder you are ready to go just run the source code and you will find results as shown in the HTML file in the jupyter notebook directory
     * More information about the source code inside the jupyter notebook directory README.md
   * Now, if you want to use your own images in the experiment just place your .PNG images inside the Images.zip directory and the run Source Code
   * But, you better image quality i would suggest download the images in .pdf format and then convert them into .PNG
   * You can convert .pdf file to .PNG images by using the PDF-PNG.py script i provided inside the readonly drictory
     * More Information about using .pdf file and PDF-PNG.py indside readonly/README.md
