import math
import matplotlib.pyplot as plt
import numpy as np

# Função de distância
def distancia(x, a):
    return math.sqrt(x**2 + a**2)

# Integral usando substituição trigonométrica
def integral_distancia(x, a):
    return math.log(x + math.sqrt(x**2 + a**2))

# Parâmetros
a = float(input("Altura da câmera (a): "))
x_ini = float(input("Posição inicial do objeto (x_ini): "))
x_fim = float(input("Posição final do objeto (x_fim): "))

# Cálculo da distância total acumulada (integral definida)
D = integral_distancia(x_fim, a) - integral_distancia(x_ini, a)

print(f"\nDistância acumulada (visual/perceptiva): {D:.4f} unidades")

# Geração de gráfico
x_vals = np.linspace(x_ini, x_fim, 100)
d_vals = [math.sqrt(x**2 + a**2) for x in x_vals]

plt.figure(figsize=(10, 5))
plt.plot(x_vals, d_vals, label=r'$d(x) = \sqrt{x^2 + a^2}$')
plt.fill_between(x_vals, d_vals, alpha=0.2, color='skyblue', label='Área ≈ distância acumulada')
plt.title("Distância entre câmera e objeto em movimento (2D)")
plt.xlabel("Posição do objeto no eixo X")
plt.ylabel("Distância da câmera")
plt.grid(True)
plt.legend()
plt.savefig("grafico_distancia.png")
print("Gráfico salvo como 'grafico_distancia.png'.")

