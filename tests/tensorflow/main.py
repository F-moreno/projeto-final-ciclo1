import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import keras.datasets.mnist as mnist


def ex1():
    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer="sgd", loss="mean_squared_error")

    xs = np.array([1.0, 2.0, 3.0], dtype=float)
    ys = np.array([150.0, 200.0, 250.0], dtype=float)

    model.fit(xs, ys, epochs=1000)

    print(model.predict(np.array([8.0, 9.0, 10.0])))


def fashion_mnist():
    """
    Label	Classe
    0	Camisetas/Top (T-shirt/top)
    1	Calça (Trouser)
    2	Suéter (Pullover)
    3	Vestidos (Dress)
    4	Casaco (Coat)
    5	Sandálias (Sandal)
    6	Camisas (Shirt)
    7	Tênis (Sneaker)
    8	Bolsa (Bag)
    9	Botas (Ankle boot)
    """

    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

    print(train_images.shape)
    print(len(train_labels))
    print(train_labels)
    print(test_images.shape)
    print(len(test_labels))
    class_names = [
        "T-shirt/top",
        "Trouser",
        "Pullover",
        "Dress",
        "Coat",
        "Sandal",
        "Shirt",
        "Sneaker",
        "Bag",
        "Ankle boot",
    ]

    plt.figure()
    plt.imshow(train_images[0])
    plt.colorbar()
    plt.grid(False)
    plt.show()

    train_images = train_images / 255.0
    test_images = test_images / 255.0
    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i]])
    plt.show()


def main():

    (train_images, train_labels), (test_images, test_labels) = mnist.load_data()

    print(train_images.shape)
    print(len(train_labels))
    print(train_labels)
    print(test_images.shape)
    print(len(test_labels))

    plt.figure()
    plt.imshow(train_images[0])
    plt.colorbar()
    plt.grid(False)
    plt.show()

    train_images = train_images / 255.0
    test_images = test_images / 255.0
    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i + 1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(train_labels[i])
    plt.show()


if __name__ == "__main__":
    main()
