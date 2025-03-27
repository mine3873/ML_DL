import numpy as np
import tensorflow as tf
from keras.api.layers import Dense
from keras.api.models import Sequential
from keras.src.datasets import mnist



vecLen = 28 * 28

(x_train, y_train), (_, _) = mnist.load_data()

x_train = x_train / 255.0
x_train = x_train.reshape(-1, vecLen)

model = Sequential([
    Dense(units=25, activation='relu'),
    Dense(units = 15, activation='relu'),
    Dense(units=10, activation='softmax'),
])

from keras.api.losses import SparseCategoricalCrossentropy

model.compile(loss=SparseCategoricalCrossentropy())

model.fit(x_train, y_train, epochs=100)

model.save("handwritten_0_1_classifier3.keras") 

