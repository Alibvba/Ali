import tensorflow as tf
from tensorflow.keras import datasets, layers, models

# Charger les données MNIST
(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# Créer un modèle simple
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compiler le modèle
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Entraîner le modèle sur un GPU
model.fit(x_train, y_train, epochs=5)

# Évaluer le modèle
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f"Précision sur les données de test : {test_acc}")
