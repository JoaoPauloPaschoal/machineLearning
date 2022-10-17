from math import sqrt
import numpy as np

z = 0
x_linha = 0
media = 0
sigma = 0
raiz_n = 0

x_linha = float(input("Informe valor de X linha: "))
media = float(input("Informe valor médio: "))
sigma = float(input("Informe valor sigma: "))
raiz_n = float(input("Informe valor de N: "))
raiz = np.sqrt(raiz_n)
z = (x_linha - media) / (sigma / raiz)
print(f"O valor de Z é igual a: {(z):.2f}")