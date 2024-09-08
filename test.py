import matplotlib.pyplot as plt
from tensorflow.keras import datasets

# Charger les données MNIST
(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()

# Afficher les 5 premières images du jeu de données d'entraînement
for i in range(5):
    plt.imshow(x_train[i], cmap='gray')  # Affiche l'image en niveaux de gris
    plt.title(f"Étiquette : {y_train[i]}")  # Affiche le chiffre correspondant
    plt.show()
