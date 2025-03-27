from keras.api.models import load_model

model = load_model("handwritten_0_1_classifier2.h5")

for i, layer in enumerate(model.layers):
    weights, biases = layer.get_weights()
    print(f"Layer {i+1}: {layer.name}")
    print(f"  Weights shape: {weights.shape}")
    print(f"  Biases shape: {biases.shape}")
    print(f"  Weights: {weights}")
    print(f"  Biases: {biases}\n")