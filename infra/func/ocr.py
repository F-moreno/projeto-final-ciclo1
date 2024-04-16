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

    def read_json(self, text):
        return self.__get_json(text)

    def __get_text_from_img(self, img_path):
        # transforma a imagem caso ela venha em angulos diferentes de 0,90,180,270
        img = self.__get_rgb_img(img_path)
        self.__show_img(img)
        gray = self.__get_grayscale_img(img)
        thresh = self.__get_thresholded_img(gray)
        img = self.__get_fixed_img(thresh, img)
        self.__show_img(img)

        # rotaciona caso o texto possua angulo diferente de 0
        angle = self.__get_angle_img(img)
        print(angle)
        img = self.__get_rotated_img(img, angle)
        self.__show_img(img)
        # self.__show_img(gray)
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
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        return img_gray

    def __get_thresholded_img(self, img_gray):
        eq = cv2.equalizeHist(img_gray)
        img_threshold = cv2.threshold(
            eq, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
        )[1]
        return img_threshold

    def __get_medianblurred_img(self, img):
        img_median = cv2.medianBlur(img, 5)
        return img_median

    def __get_corners_img(self, thresh):
        # Encontrar os contornos na imagem binarizada
        # thresh = cv2.bitwise_not(thresh)

        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )
        # Encontrar o maior quadrado externo
        max_area = 0
        max_square_corners = None
        """for contour in contours:
            # Aproximar o contorno para um polígono com menos vértices
            approx = cv2.approxPolyDP(
                contour, 0.04 * cv2.arcLength(contour, True), True
            )

            # Verificar se o polígono tem 4 vértices (quadrado)
            if len(approx) == 4:
                # Calcular a área do quadrado
                area = cv2.contourArea(approx)
                if area > max_area:
                    max_area = area
                    max_square_corners = approx.reshape(-1, 2)"""

        # novo
        rect = cv2.minAreaRect(np.vstack(contours))
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        min_square_contours = []
        for point in box:
            min_square_contours.append((point[0], point[1]))
        external_contour = np.vstack(contours)
        x, y, w, h = cv2.boundingRect(external_contour)
        max_square_corners = np.float32(
            [[x, y], [x, y + h], [x + w, y + h], [x + w, y]]
        )
        print(min_square_contours)
        return min_square_contours

    def __get_fixed_img(self, thresh, img):

        external_points = self.__get_corners_img(thresh)

        h, w = img.shape[:2]
        destined_points = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]])
        external_points = np.array(external_points, dtype=np.float32)

        M = cv2.getPerspectiveTransform(external_points, destined_points)
        img_fixed = cv2.warpPerspective(img, M, (w, h))
        img_fixed = cv2.flip(img_fixed, 1)

        return img_fixed

    def __get_angle_img(self, img_gray):

        osd = pytesseract.image_to_osd(img_gray)
        angulo = float(osd.split("\n")[2].split(":")[-1])
        return angulo

    # corrige angulo
    def __get_rotated_img(self, img, angle):
        rows, cols = img.shape[:2]
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
        img_rotated = cv2.warpAffine(img, M, (cols, rows))
        return img_rotated

    def __get_medianblurred_img(self, img):
        img_gau = cv2.GaussianBlur(img, (5, 5), 0)
        return img_gau

    def __get_contrasted_img(self, img, alpha=1.5, beta=-50):
        img_contrasted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
        return img_contrasted

    def __get_laplacian_img(self, img):
        img_lpc = cv2.Laplacian(img, cv2.CV_8UC1)
        return img_lpc

    def __show_img(self, img):
        cv2.imshow("Imagem", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def __show_two_images(self, img1, img2):
        numpy_horizontal_concat = np.concatenate((img1, img2), axis=1)
        cv2.imshow("BGR -> RGB", numpy_horizontal_concat)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def __get_image_data(self, img_path):
        img = self.__get_rgb_img(img_path)
        return pytesseract.image_to_data(img, lang="por", config=self.config_tesseract)

    def __get_json(self, txt):
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
    arquivo = "/home/fermoreno/workspace/alpha/ciclo_01/Projeto_Final/Docs/imagens/formulario/Normal.png"
    img = tesseract.read_image(arquivo)
    texto_reconhecido = tesseract.read_text(arquivo)
    print(texto_reconhecido)
    json = tesseract.read_json(texto_reconhecido)

    # print(f"json:\n{json}")
    cv2.imshow("Imagem Processada", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
