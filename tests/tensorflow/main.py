import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import keras.datasets.mnist as mnist


def ex1():
    model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer="sgd", loss="mean_squared_error")

    xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0], dtype=float)
    ys = np.array([0.0, 1.0, 1.0, 2.0, 3.0, 5.0, 8.0, 13.0, 21.0, 34.0], dtype=float)

    model.fit(xs, ys, epochs=1000)

    print(model.predict(np.array([11.0])))


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

    (training_images, training_labels), (test_images, test_labels) = mnist.load_data()
    training_images = training_images.reshape(60000, 28, 28, 1)
    training_images = training_images / 255.0
    test_images = test_images.reshape(10000, 28, 28, 1)
    test_images = test_images / 255.0
    model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Conv2D(
                64, (3, 3), activation="relu", input_shape=(28, 28, 1)
            ),
            tf.keras.layers.MaxPooling2D(2, 2),
            tf.keras.layers.Conv2D(64, (3, 3), activation="relu"),
            tf.keras.layers.MaxPooling2D(2, 2),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation="relu"),
            tf.keras.layers.Dense(10, activation="softmax"),
        ]
    )
    model.compile(
        optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
    )
    model.summary()
    model.fit(training_images, training_labels, epochs=5)
    test_loss = model.evaluate(test_images, test_labels)

    print(test_labels[:100])
    f, axarr = plt.subplots(3, 4)
    FIRST_IMAGE = 0
    SECOND_IMAGE = 7
    THIRD_IMAGE = 26
    CONVOLUTION_NUMBER = 1
    layer_outputs = [layer.output for layer in model.layers]
    activation_model = tf.keras.models.Model(inputs=model.input, outputs=layer_outputs)
    for x in range(0, 4):
        f1 = activation_model.predict(test_images[FIRST_IMAGE].reshape(1, 28, 28, 1))[x]
        axarr[0, x].imshow(f1[0, :, :, CONVOLUTION_NUMBER], cmap="inferno")
        axarr[0, x].grid(False)
        f2 = activation_model.predict(test_images[SECOND_IMAGE].reshape(1, 28, 28, 1))[
            x
        ]
        axarr[1, x].imshow(f2[0, :, :, CONVOLUTION_NUMBER], cmap="inferno")
        axarr[1, x].grid(False)
        f3 = activation_model.predict(test_images[THIRD_IMAGE].reshape(1, 28, 28, 1))[x]
        axarr[2, x].imshow(f3[0, :, :, CONVOLUTION_NUMBER], cmap="inferno")
        axarr[2, x].grid(False)
    plt.show()


if __name__ == "__main__":
    main()
