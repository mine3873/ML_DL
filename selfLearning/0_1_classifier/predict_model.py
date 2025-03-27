import matplotlib.pyplot as plt
from keras.src.datasets import mnist
from keras.api.models import load_model
import tensorflow as tf
import numpy as np

vecLen = 28 * 28

(_, _), (x_test, y_test) = mnist.load_data()

x_test = x_test / 255.0
x_test = x_test.reshape(-1, vecLen)

model = load_model("handwritten_0_1_classifier3.keras")

predictions = model.predict(x_test)


num_samples = 20
plt.figure(figsize=(10, 4))

for i in range(num_samples):
    plt.subplot(4, 5, i + 1)
    plt.subplots_adjust(hspace=1)
    plt.imshow(x_test[i].reshape(28, 28), cmap="gray")
    predicted_label = np.argmax(predictions[i])
    
    plt.title(f"True: {y_test[i]}\nPred: {predicted_label}")
    plt.axis("off")

plt.show()