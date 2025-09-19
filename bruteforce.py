import time
import matplotlib.pyplot as plt
import numpy as np

mayusculas = 'ABCDEFGHIJKMNÑLOPQRSTUVWXYZ'
minusculas = 'abcdefghijklmnÑopqrstuvwxyz'
simbolos = ',./<>?;''\"{}[]\\|*-+=_-()&^%$#@!`~'
numeros = '1234567890'
caracteres = mayusculas + minusculas + simbolos + numeros
password = input("Ingresa una contraseña de maximo 3 caracteres: ")
if len(password) == 3:
    caracteres = mayusculas + minusculas + simbolos + numeros
    intentos = 0
    encontrada = False
    inicio = time.time()
    for caracter1 in caracteres:
        intentos += 1
        if caracter1 == password:
            encontrada = True
            intento = caracter1
            break

        for caracter2 in caracteres:
            intentos += 1
            if caracter1 + caracter2 == password:
                encontrada = True
                intento = caracter1 + caracter2
                break

            for caracter3 in caracteres:
                intentos += 1
                if caracter1 + caracter2 + caracter3 == password:
                    encontrada = True
                    intento = caracter1 + caracter2 + caracter3
                    break

            if encontrada:
                break
        if encontrada:
            break

    fin = time.time()

    print("Contraseña encontrada:", intento)
    print("Intentos realizados:", intentos)
    print("Tiempo transcurrido:", round(fin - inicio, 4), "segundos")
elif len(password) <= 2:
    print("La contraseña tiene menos caracteres")
else:
    print("La contraseña tiene mas caracteres")


longitudes = [1, 2, 3]
tiempos = []


test_char = caracteres[-1]

for l in longitudes:
    inicio = time.time()
    test = test_char * l
    encontrada = False
    for l1 in caracteres:
        if l == 1 and l1 == test:
            encontrada = True
            break
        for l2 in caracteres:
            if l == 2 and l1 + l2 == test:
                encontrada = True
                break
            for l3 in caracteres:
                if l == 3 and l1 + l2 + l3 == test:
                    encontrada = True
                    break
            if encontrada:
                break
        if encontrada:
            break
    fin = time.time()
    tiempos.append(fin - inicio)


x_nuevo = np.linspace(min(longitudes), max(longitudes), 300)
coef = np.polyfit(longitudes, tiempos, 2) 
y_nuevo = np.polyval(coef, x_nuevo)

plt.plot(x_nuevo, y_nuevo, '-', label="Curva suave")
plt.scatter(longitudes, tiempos, color='red', label="Puntos reales")
plt.xlabel("Longitud de la contraseña")
plt.ylabel("Tiempo (s)")
plt.title("Tiempo según longitud de la contraseña")
plt.legend()
plt.show()