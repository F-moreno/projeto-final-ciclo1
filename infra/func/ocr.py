import re
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2
import pytesseract
import matplotlib.pyplot as plt
from pytesseract import Output
import os

diretorio = "tests/forms"

# Lista os arquivos de imagem no diretório
arquivos = [
    os.path.join(diretorio, f) for f in os.listdir(diretorio) if f.endswith(".png")
]


class TesseractOCR:
    def __init__(self):
        self.config_tesseract = "--tessdata-dir infra/func/tessdata"

    def read_text(self, img_path):
        return self.__get_text_from_img(img_path)

    def __get_text_from_img(self, img_path):
        img = self.__get_rgb_img(img_path)
        return img, pytesseract.image_to_string(
            img, lang="por", config=self.config_tesseract
        )

    def __get_rgb_img(self, img_path):
        img_bgr = cv2.imread(img_path)
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        self.__show_two_images(img_bgr, img_rgb)
        return img_rgb

    def __get_grayscale_img(self, img):
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return img_gray

    def __get_thresholded_img(self, img):
        img_gray = self.__get_grayscale_img(img)
        img_threshold = cv2.threshold(
            img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]
        return img_threshold

    def __get_medianblurred_img(self, img):
        img_median = cv2.medianBlur(img, 5)
        return img_median

    def __get_contrasted_img(self, img, alpha=1.5, beta=50):
        img_contrasted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
        return img_contrasted

    def __show_two_images(self, img1, img2):
        numpy_horizontal_concat = np.concatenate((img1, img2), axis=1)
        cv2.imshow("BGR -> RGB", numpy_horizontal_concat)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def __get_image_data(self, img_path):
        img = self.__get_rgb_img(img_path)
        return pytesseract.image_to_data(img, lang="por", config=self.config_tesseract)


# Configuração do Tesseract
config_tesseract = "--tessdata-dir infra/func/tessdata"


def teste(imagem):
    # Convertendo a imagem para escala de cinza
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplicando binarização (thresholding)
    _, imagem_binaria = cv2.threshold(imagem_cinza, 128, 255, cv2.THRESH_BINARY)

    # Aplicando um filtro para remover ruídos (opcional)
    imagem_sem_ruido = cv2.medianBlur(imagem_binaria, 5)

    # Ajustando o contraste (opcional)
    alpha = 1.5  # Fator de contraste
    beta = 50  # Fator de brilho
    imagem_processada = cv2.convertScaleAbs(imagem_sem_ruido, alpha=alpha, beta=beta)


def processar_imagem(img, config_tesseract):
    # Pré-processamento da imagem
    img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    img_lpc = cv2.Laplacian(img, cv2.CV_8UC1)

    img_gau = cv2.GaussianBlur(img, (5, 5), 0)

    # Aplicar thresholding para segmentar os objetos de interesse
    _, img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    img_med = cv2.medianBlur(img_bin, 5)

    # Ajustando o contraste (opcional)
    alpha = 1.5  # Fator de contraste
    beta = 50  # Fator de brilho
    img_fin = cv2.convertScaleAbs(img_lpc, alpha=alpha, beta=beta)

    # Encontrar contornos na imagem binarizada
    # contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Visualizar a máscara e os contornos sobrepostos na imagem original
    # img_contours = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    # cv2.drawContours(img, img_bin, -1, (255, 255, 255), 2)
    # Reconhecimento de texto usando OCR
    texto = pytesseract.image_to_string(
        cv2.bitwise_not(img_fin), lang="por", config=config_tesseract
    )

    cv2.imshow(
        "ENTRADA - LAPLACE - BINARIZADA - Gaussiana",
        cv2.hconcat([img, img_lpc, img_bin, img_gau, img_med, img_fin]),
    )
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return img, texto


def extrai_dados(texto):
    # Exibe a imagem processada
    texto = texto_reconhecido.split("\n")
    # texto = dict(texto[1:])
    json = {}
    for linha in texto:
        if ":" in linha:
            key, value = linha.split(":")
            json[key.lower()] = value.strip()

    return json


if __name__ == "__main__":
    # Processa cada imagem e exibe o texto reconhecido
    tesseract = TesseractOCR()

    for arquivo in arquivos:

        imagem_processada, texto_reconhecido = tesseract.read_text(arquivo)

        """imagem_processada, texto_reconhecido = processar_imagem(
            arquivo, config_tesseract
        )
        print(texto_reconhecido)
        print()
    """
        json = extrai_dados(texto_reconhecido)
        print(f"json:/n{json}")
        cv2.imshow("Imagem Processada", imagem_processada)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
