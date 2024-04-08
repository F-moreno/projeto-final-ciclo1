import re
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2
import pytesseract
import matplotlib.pyplot as plt
from pytesseract import Output
import os


os.system("clear" if os.name == "posix" else "cls")
# Define o caminho para o diretório contendo as imagens do formulário
diretorio = "tests/forms"

# Lista os arquivos de imagem no diretório
arquivos = [
    os.path.join(diretorio, f) for f in os.listdir(diretorio) if f.endswith(".png")
]

# Configuração do Tesseract
config_tesseract = "--tessdata-dir infra/func/tessdata --psm 6"


def processar_imagem(img, config_tesseract):
    # Pré-processamento da imagem
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

    # Aplicar thresholding para segmentar os objetos de interesse
    _, img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Encontrar contornos na imagem binarizada
    contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Criar uma máscara em branco do mesmo tamanho da imagem
    mask = np.zeros_like(img)

    # Preencher os contornos na máscara
    cv2.drawContours(mask, contours, -1, (255, 255, 255), 2)

    # Visualizar a máscara e os contornos sobrepostos na imagem original
    # img_contours = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(img, contours, -1, (255, 255, 255), 2)
    # Reconhecimento de texto usando OCR
    texto = pytesseract.image_to_string(
        cv2.bitwise_not(img), lang="por", config=config_tesseract
    )

    cv2.imshow("Mask", mask)
    cv2.imshow("Contours", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return cv2.bitwise_not(img), texto


if __name__ == "__main__":
    # Processa cada imagem e exibe o texto reconhecido
    for arquivo in arquivos:
        imagem_processada, texto_reconhecido = processar_imagem(
            arquivo, config_tesseract
        )

        # Exibe a imagem processada
        print(texto_reconhecido)
        cv2.imshow("Imagem Processada", imagem_processada)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
