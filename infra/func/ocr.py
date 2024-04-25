import re
import numpy as np
import cv2
import pytesseract
import matplotlib.pyplot as plt
from pytesseract import Output
import os
import datetime

diretorio = "tests/forms"

# Lista os arquivos de imagem no diretório
arquivos = [
    os.path.join(diretorio, f) for f in os.listdir(diretorio) if f.endswith(".png")
]


class TesseractOCR:
    """
    TesseractOCR Class:
    - read_text: Le o arquivo de imagem e retorna o texto
    - read_json: Le o arquivo de imagem e retorna o objeto JSON
    - read_image: Le o arquivo de imagem e retorna a imagem
    """

    nome_arquivo = None

    def __init__(self):
        self.config_tesseract = "--tessdata-dir infra/func/tessdata"

    def read_text(self, img_path):
        img = self.__get_rgb_img(img_path)
        return self.__get_text_from_img(img)

    def read_image(self, img_path):
        return self.__get_rgb_img(img_path)

    def read_json(self, text):
        return self.__get_json(text)

    def read_document(self, img_path):
        rg_info = self.__get_document(img_path)
        return self.__get_text_from_img(rg_info)

    def __get_text_from_img(self, img):

        # transforma a imagem caso ela venha em angulos diferentes de 0,90,180,270
        gray = self.__get_grayscale_img(img)
        thresh = self.__get_thresholded_img(gray)
        img = self.__get_fixed_img(thresh, gray)

        # corrige o angulo do texto para 0º
        img = self.__get_contrasted_img(img, beta=-50)
        angle = self.__get_angle_img(img)
        img = self.__get_rotated_img(img, angle)

        # leitura do texto
        text = pytesseract.image_to_string(
            img, lang="por", config=self.config_tesseract
        )
        return text

    def __get_text_from_img_handwriting(self, img):

        # transforma a imagem caso ela venha em angulos diferentes de 0,90,180,270
        gray = self.__get_grayscale_img(img)
        thresh = self.__get_thresholded_img(gray)
        img = self.__get_fixed_img(thresh, gray)

        # corrige o angulo do texto para 0º
        img = self.__get_contrasted_img(img, beta=-50)
        angle = self.__get_angle_img(img)
        img = self.__get_rotated_img(img, angle)

        # leitura do texto
        text = pytesseract.image_to_string(
            img, lang="por", config=self.config_tesseract
        )
        return text

    def __get_rgb_img(self, img_path):
        img_bgr = cv2.imread(img_path)
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        return img_rgb

    def __get_grayscale_img(self, img):
        print(img.shape)
        if len(img.shape) == 3:
            img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        else:
            img_gray = img
        return img_gray

    def __get_thresholded_img(self, img_gray):
        img_threshold = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY_INV)[1]
        return img_threshold

    def __get_corners_img(self, thresh, img):
        contours, _ = cv2.findContours(
            thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        # Encontrar o menor quadrado externo
        rect = cv2.minAreaRect(np.vstack(contours))
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        min_square_contours = []
        for point in box:
            min_square_contours.append((point[0], point[1]))

        # Desenhar o quadrado
        img_destacada = img.copy()
        cv2.drawContours(img_destacada, [box], 0, (0, 255, 0), 2)

        """# Salvar a imagem com a área destacada
        cv2.imwrite(
            f"Docs/imagens/destacada/{TesseractOCR.nome_arquivo}",
            img_destacada,
        )
        self.__show_img(img_destacada)"""
        return min_square_contours, rect

    '''
    #versao antiga
    def __get_fixed_img(self, thresh, img):

        external_points, rect = self.__get_corners_img(thresh, img)
        angle = rect[2]

        w = rect[1][0]
        h = rect[1][1]
        destined_points = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]])
        external_points = np.array(external_points, dtype=np.float32)

        M = cv2.getPerspectiveTransform(external_points, destined_points)
        img_fixed = cv2.warpPerspective(img, M, (w, h))
        img_fixed = cv2.flip(img_fixed, 1)

        """cv2.imwrite(
            f"Docs/imagens/rotacionada/{TesseractOCR.nome_arquivo}",
            img_fixed,
        )"""
        return img_fixed'''

    def __get_fixed_img(self, thresh, img):
        external_points, rect = self.__get_corners_img(thresh, img)
        angle = rect[2]

        # Obtém as dimensões exatas do retângulo (comprimento e largura)
        rotated_width = int(rect[1][0])
        rotated_height = int(rect[1][1])

        # Calcula a proporção para manter a largura máxima de 600 pixels
        if rotated_width > 600:
            scale_factor = 600 / rotated_width
            rotated_width = 600
            rotated_height = int(rotated_height * scale_factor)

        # Cria uma nova imagem com as dimensões da rotação calculada
        rotated_image = np.zeros((rotated_height, rotated_width), dtype=np.uint8)

        # Converte os pontos externos e os pontos de destino para np.float32
        external_points = np.array(external_points, dtype=np.float32)
        dest_points = np.array(
            [
                [0, 0],
                [0, rotated_height - 1],
                [rotated_width - 1, rotated_height - 1],
                [rotated_width - 1, 0],
            ],
            dtype=np.float32,
        )

        # Calcula a matriz de perspectiva (M) para corrigir a distorção de perspectiva
        M = cv2.getPerspectiveTransform(external_points, dest_points)

        # Aplica a matriz de perspectiva (M) à imagem original
        rotated_image = cv2.warpPerspective(
            img, M, (rotated_width, rotated_height), flags=cv2.INTER_LINEAR
        )

        rotated_image = cv2.flip(rotated_image, 1)

        """cv2.imwrite(
            f"Docs/imagens/rotacionada/{TesseractOCRNome_arquivo}",
            rotated_image,
        )"""
        return rotated_image

    def __get_angle_img(self, img_gray):
        try:
            osd = pytesseract.image_to_osd(img_gray)
            print(osd)
            # self.__show_img(cv2.resize(img_gray, (500, 500)))
            angulo = float(osd.split("\n")[1].split(":")[-1])
        except Exception as e:
            print(e)
            angulo = 0
        return angulo

    # corrige angulo
    def __get_rotated_img(self, img, angle):
        print(angle)
        rows, cols = img.shape[:2]
        if angle == 90 or angle == 270:
            cols, rows = rows, cols
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
        img_rotated = cv2.warpAffine(img, M, (cols, rows))

        """cv2.imwrite(
            f"Docs/imagens/alinhada/{TesseractOCR.nome_arquivo}",
            img_rotated,
        )"""

        return img_rotated

    def __get_enhanced_edges_img(self, gray):
        # Aplicar o filtro de mediana para suavizar a imagem
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        enhanced_gray = clahe.apply(gray)

        # Apply bilateral filter to smooth the image while preserving edges
        filtered_image = cv2.bilateralFilter(enhanced_gray, 9, 75, 75)

        binary_image = np.ones_like(filtered_image) * 255
        binary_image[(filtered_image < 90) or (filtered_image > 200)] = 0

        """filtered_image = cv2.threshold(
            filtered_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]"""

        return binary_image

    def __get_contrasted_img(self, img, alpha=1.5, beta=0):
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
                key, value = linha.split(":", 1) or linha.split(";", 1)
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

        ###  ÁRea 51 ###

    def __get_document(self, img_path):
        # busca filtro com mesmo nome em outra pasta gt
        img_name = img_path.split("/")[-1]
        filtro_path = os.path.join("/".join(img_path.split("/")[:-2]), "gt", img_name)

        rg = cv2.imread(img_path)  # , cv2.IMREAD_GRAYSCALE)
        gt = cv2.imread(filtro_path)  # , cv2.IMREAD_GRAYSCALE)

        infos = rg.copy()
        infos[gt == 0] = 255

        # infos = cv2.threshold(infos, 117, 255, cv2.THRESH_BINARY_INV)[1]

        return infos

    def teste(self, img_path):
        TesseractOCR.nome_arquivo = img_path.split("/")[-1]
        img = self.__get_rgb_img(img_path)
        # transforma a imagem caso ela venha em angulos diferentes de 0,90,180,270
        gray = self.__get_grayscale_img(img)
        thresh = self.__get_thresholded_img(gray)
        img = self.__get_fixed_img(thresh, gray)

        # corrige o angulo do texto para 0º
        img = self.__get_contrasted_img(img, beta=0)
        angle = self.__get_angle_img(img)
        img = self.__get_rotated_img(img, angle)

        text = pytesseract.image_to_string(
            img, lang="por", config=self.config_tesseract
        )
        return text


if __name__ == "__main__":
    # Processa cada imagem e exibe o texto reconhecido
    tesseract = TesseractOCR()
    arquivo_path = "/home/fermoreno/workspace/alpha/ciclo_01/Projeto_Final/Docs/imagens/formulario/Normal_225g.png"
    texto = tesseract.read_text(arquivo_path)
    print(tesseract.read_json(texto))

    arquivo_path = "/home/fermoreno/workspace/alpha/ciclo_01/Projeto_Final/Docs/imagens/rg/in/00025929.jpg"
    print(tesseract.read_document(arquivo_path))

    arquivo_path = "/home/fermoreno/workspace/alpha/ciclo_01/Projeto_Final/Docs/imagens/cpf/in/00010892.jpg"
    print(tesseract.read_document(arquivo_path))

    arquivo_path = "/home/fermoreno/workspace/alpha/ciclo_01/Projeto_Final/Docs/imagens/cnh/in/00003604.jpg"
    print(tesseract.read_document(arquivo_path))
