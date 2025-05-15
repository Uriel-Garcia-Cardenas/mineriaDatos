from scipy import stats

# ------------------------------------------------------------
# Problema 1: Control de Calidad en una Fábrica de Tornillos
# ------------------------------------------------------------
print("\n--- Problema 1: Diámetro de Tornillos ---")
print("Una fábrica afirma que el diámetro promedio de sus tornillos es de 10 mm.")
print("Se toma una muestra de 49 tornillos con media 9.7 mm y desviación estándar de 0.5 mm.")
print("Nivel de significancia: 1%")

# Datos
n = 49
x_bar = 9.7
mu_0 = 10
s = 0.5
alpha = 0.01

# Estadístico Z
z_stat = (x_bar - mu_0) / (s / (n ** 0.5))

# Valor p
p_value = stats.norm.cdf(z_stat)

# Resultados
print(f"Estadístico Z: {z_stat:.4f}")
print(f"Valor p: {p_value:.4f}")

if p_value < alpha:
    print(" Rechazamos la hipótesis nula: el diámetro promedio es menor a 10 mm.")
else:
    print("No hay evidencia suficiente para rechazar la hipótesis nula.")

# ------------------------------------------------------------
# Problema 2: Duración de Baterías de Celulares
# ------------------------------------------------------------
print("\n--- Problema 2: Duración de Baterías ---")
print("Se afirma que la duración promedio de baterías es de 20 horas.")
print("Muestra de 30 baterías con media de 18.5 horas y desviación estándar de 2.5 horas.")
print("Nivel de significancia: 5%")

# Datos
n = 30
x_bar = 18.5
mu_0 = 20
s = 2.5
alpha = 0.05

# Estadístico t
t_stat = (x_bar - mu_0) / (s / (n ** 0.5))

# Valor p
p_value = stats.t.cdf(t_stat, df=n - 1)

# Resultados
print(f"Estadístico t: {t_stat:.4f}")
print(f"Valor p: {p_value:.4f}")

if p_value < alpha:
    print(" Rechazamos la hipótesis nula: la duración de las baterías es menor a 20 horas.")
else:
    print(" No hay evidencia suficiente para rechazar la hipótesis nula.")

# ------------------------------------------------------------
# Problema 3: Control de Peso en una Planta de Alimentos
# ------------------------------------------------------------
print("\n--- Problema 3: Peso de Bolsas de Harina ---")
print("El productor indica que el peso promedio de las bolsas es de 1000 gramos.")
print("Muestra de 40 bolsas con media de 990 g y desviación estándar de 12 g.")
print("Nivel de significancia: 2%")

# Datos
n = 40
x_bar = 990
mu_0 = 1000
s = 12
alpha = 0.02

# Estadístico t
t_stat = (x_bar - mu_0) / (s / (n ** 0.5))

# Valor p
p_value = stats.t.cdf(t_stat, df=n - 1)

# Resultados
print(f"Estadístico t: {t_stat:.4f}")
print(f"Valor p: {p_value:.4f}")

if p_value < alpha:
    print(" Rechazamos la hipótesis nula: el peso promedio de las bolsas es menor a 1000 g.")
else:
    print(" No hay evidencia suficiente para rechazar la hipótesis nula.")
