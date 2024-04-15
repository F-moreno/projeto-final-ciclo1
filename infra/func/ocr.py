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

    def read_image(self, img_path):
        return self.__get_rgb_img(img_path)

    def __get_text_from_img(self, img_path):
        img = self.__get_rgb_img(img_path)
        text = pytesseract.image_to_string(
            img, lang="por", config=self.config_tesseract
        )
        return text

    def __get_rgb_img(self, img_path):
        img_bgr = cv2.imread(img_path)
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        # self.__show_two_images(img_bgr, img_rgb)
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

    def __get_medianblurred_img(self, img):
        img_gau = cv2.GaussianBlur(img, (5, 5), 0)
        return img_gau

    def __get_contrasted_img(self, img, alpha=1.5, beta=50):
        img_contrasted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
        return img_contrasted

    def __get_laplacian_img(self, img):
        img_lpc = cv2.Laplacian(img, cv2.CV_8UC1)
        return img_lpc

    def __show_two_images(self, img1, img2):
        numpy_horizontal_concat = np.concatenate((img1, img2), axis=1)
        cv2.imshow("BGR -> RGB", numpy_horizontal_concat)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def __get_image_data(self, img_path):
        img = self.__get_rgb_img(img_path)
        return pytesseract.image_to_data(img, lang="por", config=self.config_tesseract)

    def extrair_dados(self, txt):
        # Exibe a imagem processada
        texto = txt.split("\n")
        # texto = dict(texto[1:])
        json = {}
        for linha in texto:
            if ":" in linha:
                key, value = linha.split(":")
                key = (
                    key.lower()
                    .replace(" ", "")
                    .replace("ç", "c")
                    .replace("ã", "a")
                    .replace("é", "e")
                    .replace("ê", "e")
                    .replace("õ", "o")
                    .replace("ú", "u")
                )
                json[key.strip()] = value.strip()

        return json


if __name__ == "__main__":
    # Processa cada imagem e exibe o texto reconhecido
    tesseract = TesseractOCR()

    for arquivo in arquivos:

        imagem_processada = tesseract.read_image(arquivo)
        texto_reconhecido = tesseract.read_text(arquivo)
        json = tesseract.extrair_dados(texto_reconhecido)

        print(f"json:\n{json}")
        cv2.imshow("Imagem Processada", imagem_processada)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
