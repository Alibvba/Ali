import numpy as np
import matplotlib.pyplot as plt

# Définir les valeurs de x
x = np.linspace(0, 2, 100)

# Calculer les valeurs de e^x
y = np.exp(x)  # exp(x) = e^x

# Tracer la courbe
plt.plot(x, y)
plt.title("Courbe exponentielle e^x")
plt.xlabel("x")
plt.ylabel("e^x")
plt.grid(True)

# Montrer le graphique
plt.show()
