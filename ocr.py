
#Importando as bibliotecas
import cv2
import pytesseract

# Lendo a imagem
image = cv2.imread('texto.jpg')

# Transformando imagem para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
gray, img_bin = cv2.threshold(gray,128,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)
gray = cv2.bitwise_not(img_bin)

# Convertendo para texto
text = pytesseract.image_to_string(gray)

print(text)

