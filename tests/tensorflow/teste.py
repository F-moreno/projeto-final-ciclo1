import os
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split


# Função para carregar imagens e rótulos
def load_data(data_dir):
    images = []
    labels = []
    for subdir, _, files in os.walk(data_dir):
        for file in files:
            image_path = os.path.join(subdir, file)
            label = os.path.basename(subdir)
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            img = cv2.resize(img, (28, 28))  # Redimensionar imagem para 28x28
            images.append(img)
            labels.append(label)
    return np.array(images), np.array(labels)


# Carregar dados
images, labels = load_data("dataset/img")

# Pré-processamento: normalização e divisão dos dados
images = images.astype("float32") / 255.0
labels = tf.keras.utils.to_categorical(labels)
x_train, x_test, y_train, y_test = train_test_split(
    images, labels, test_size=0.2, random_state=42
)

# Criar modelo CNN simples
model = models.Sequential(
    [
        layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.Flatten(),
        layers.Dense(64, activation="relu"),
        layers.Dense(
            38, activation="softmax"
        ),  # 38 classes: 26 letras + 10 números + 2 parênteses
    ]
)

# Compilar o modelo
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# Treinar o modelo
history = model.fit(
    x_train.reshape(-1, 28, 28, 1),
    y_train,
    epochs=10,
    validation_data=(x_test.reshape(-1, 28, 28, 1), y_test),
)

# Avaliar o modelo
test_loss, test_acc = model.evaluate(x_test.reshape(-1, 28, 28, 1), y_test)
print("Test accuracy:", test_acc)
