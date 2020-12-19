# Optical-Character-Recognition
## C209 - Laboratório

|Nome|Matrícula|Curso|
|---------|---------|---------|
|Antonio Adami Palma|1477|Eng. Computação|
|Gustavo Alves Esteves|1534|Eng. Computação|
|João Vítor Carvalho de Paula Dutra|1535|Eng. Computação|

---
## Introdução

Este projeto tem o objetivo de demonstrar os conhecimentos adquiridos na disciplina aplicando em um OCR (Optical-Character-Recognition), que identifica textos em imagens.

---
## Instruções para a execução
Este projeto foi feito em Python e utiliza as bibliotecas OpenCV e PyTesseract, que precisam estar instaladas. Para isso execute os seguintes comandos no terminal:

```
$ pip install opencv-python
$ pip install pytesseract
```

Pronto. Agora o projeto está preparado para ser executado. Execute o seguinte comando para iniciar:

```
$ python ocr.py
```

---
## Programa
Quando executado o código irá ler a imagem a seguir, transformá-la para escala de cinza, e então fazer o ORC retornando o texto *"KEEP CALM"*:

![Janela da Aplicação](/texto.jpg)

### Encerramento da aplicação
Para encerrar a aplicação precione `ctrl + c` no terminal.
