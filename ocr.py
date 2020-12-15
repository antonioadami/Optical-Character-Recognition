# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 20:40:10 2020

@author: Antonio Adami
"""

# Importing the OCR library


#Importing the libraries
import cv2
import pytesseract

class Output:
    BYTES = 'bytes'
    DATAFRAME = 'data.frame'
    DICT = 'dict'
    STRING = 'string'
    

def image_to_string(
    image,
    lang=None,
    config='',
    nice=0,
    output_type=Output.STRING,
    timeout=0,
):
    """
    Returns the result of a Tesseract OCR run on the provided image to string
    """
    args = [image, 'txt', lang, config, nice, timeout]

    return {
        Output.BYTES: lambda: pytesseract.run_and_get_output(*(args + [True])),
        Output.DICT: lambda: {'text': pytesseract.run_and_get_output(*args)},
        Output.STRING: lambda: pytesseract.run_and_get_output(*args),
    }[output_type]()

# Specifying the path
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

# Reading the image 
image = cv2.imread('texto.jpg')

# Extraction of text from image
text = image_to_string(image)

# Printing the text
print(text)

