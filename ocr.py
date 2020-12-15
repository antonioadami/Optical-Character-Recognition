
#Importando as bibliotecas
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
    Retorna o resultado de um Tesseract OCR
    """
    args = [image, 'txt', lang, config, nice, timeout]

    return {
        Output.BYTES: lambda: pytesseract.run_and_get_output(*(args + [True])),
        Output.DICT: lambda: {'text': pytesseract.run_and_get_output(*args)},
        Output.STRING: lambda: pytesseract.run_and_get_output(*args),
    }[output_type]()

# Lendo a imagem
image = cv2.imread('texto.jpg')

# Transformando imagem para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
gray = cv2.bitwise_not(img_bin)

# Convertendo para texto
text = image_to_string(gray)

print(text)

