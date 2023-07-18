import random
import tkinter as tk
from tkinter import messagebox

def generar_matriz_cuadrada(tamano):
    matriz = [[random.randint(0, 9) for _ in range(tamano)] for _ in range(tamano)]
    return matriz

def calcular_suma_filas_columnas(matriz):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    sumas_filas = [0] * num_filas
    sumas_columnas = [0] * num_columnas

    for i in range(num_filas):
        for j in range(num_columnas):
            sumas_filas[i] += matriz[i][j]
            sumas_columnas[j] += matriz[i][j]

    return sumas_filas, sumas_columnas

def imprimir_matriz_en_interfaz(matriz):
    matriz_str = ""
    for fila in matriz:
        matriz_str += " ".join(str(num) for num in fila) + "\n"
    return matriz_str

def mostrar_resultados_interfaz(sumas_filas, sumas_columnas):
    resultado_str = "Suma de cada fila:\n"
    for i, suma in enumerate(sumas_filas):
        resultado_str += f"Fila {i+1}: {suma}\n"

    resultado_str += "\nSuma de cada columna:\n"
    for j, suma in enumerate(sumas_columnas):
        resultado_str += f"Columna {j+1}: {suma}\n"

    messagebox.showinfo("Resultados", resultado_str)

def generar_matriz_y_calcular_sumas():
    try:
        N = int(entry_N.get())
        if N <= 0:
            raise ValueError("N debe ser un número entero positivo.")

        matriz = generar_matriz_cuadrada(N)
        matriz_str = imprimir_matriz_en_interfaz(matriz)

        label_matriz.config(text=matriz_str)

        sumas_filas, sumas_columnas = calcular_suma_filas_columnas(matriz)
        mostrar_resultados_interfaz(sumas_filas, sumas_columnas)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Generador de Matriz y Suma de Filas/Columnas")
ventana.geometry("400x400")

# Etiqueta e Input para ingresar N
label_N = tk.Label(ventana, text="Ingrese el valor de N para crear la matriz cuadrada:")
label_N.pack()

entry_N = tk.Entry(ventana)
entry_N.pack()

# Botón para generar matriz y calcular sumas
boton_generar = tk.Button(ventana, text="Generar Matriz y Calcular Sumas", command=generar_matriz_y_calcular_sumas)
boton_generar.pack()

# Etiqueta para mostrar la matriz generada
label_matriz = tk.Label(ventana, text="")
label_matriz.pack()

# Ejecutar la ventana
ventana.mainloop()
