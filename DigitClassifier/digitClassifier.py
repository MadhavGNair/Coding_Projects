import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


# train the model
def train_classifier(x_data, y_data):
    # normalize the input datasets
    x_data = tf.keras.utils.normalize(x_data, axis=1)

    # create the model
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(64, activation='relu'))
    model.add(tf.keras.layers.Dense(10, activation='softmax'))

    # compile the model
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    # train the model
    model.fit(x_data, y_data, epochs=5)

    # save the model
    model.save('digit_classifier.model')


# test the model
def test_classifier():
    # load the model
    model = tf.keras.models.load_model("digit_classifier.model")

    img_number = 1

    while os.path.isfile(f"test_images/digit_{img_number}.png"):
        try:
            img = cv2.imread(f"test_images/digit_{img_number}.png")[:, :, 0]
            img = np.invert(np.array([img]))
            prediction = model.predict(img)
            print(f"This digit is likely a {np.argmax(prediction)}")
            plt.imshow(img[0], cmap=plt.cm.binary)
            plt.show()
        except:
            print("Error!")
        finally:
            img_number += 1


if __name__ == "__main__":
    # load the dataset
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    goal = input("Do you want to train or test the model? ")
    if goal.lower() == "train":
        train_classifier(x_train, y_train)
    else:
        test_classifier()

# (!1)
