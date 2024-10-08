import mysql.connector
import csv
import matplotlib.pyplot as plt
import numpy as np

# Configuración de conexión a la base de datos MySQL
conn = mysql.connector.connect(
    host="localhost",  # Cambia a tu host de MySQL
    user="root",       # Cambia a tu usuario de MySQL
    password="",  # Cambia a tu contraseña
    database="tienda01" # Cambia a tu base de datos
)
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS lenguajes_programacion (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    lenguaje VARCHAR(50),
                    uso INT)''')

# Función para capturar datos
def capturar_datos():
    lenguajes = ['Python', 'Java', 'C++', 'Visual Basic', 'C#', 'SQL']
    for lenguaje in lenguajes:
        uso = int(input(f'¿Cuántos estudiantes usan {lenguaje}?: '))
        cursor.execute("INSERT INTO lenguajes_programacion (lenguaje, uso) VALUES (%s, %s)", (lenguaje, uso))
    conn.commit()

# Función para obtener estadísticas
def obtener_datos():
    cursor.execute("SELECT lenguaje, uso FROM lenguajes_programacion")
    datos = cursor.fetchall()
    return datos

# Función para guardar datos en CSV
def guardar_en_csv(datos):
    with open('datos_estadisticos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Lenguaje', 'Uso'])
        writer.writerows(datos)
    print("Datos guardados en datos_estadisticos.csv")

# Función para generar la gráfica
def generar_grafica(datos):
    etiquetas = [fila[0] for fila in datos]
    usos = [fila[1] for fila in datos]
    
    y_pos = np.arange(len(etiquetas))
    plt.bar(y_pos, usos, align='center', alpha=0.5)
    plt.xticks(y_pos, etiquetas)
    plt.ylabel('Número de estudiantes')
    plt.title('Ranking de lenguajes de programación Uniremington')
    plt.show()

# Flujo del programa
def main():
    capturar_datos()
    datos = obtener_datos()
    guardar_en_csv(datos)
    generar_grafica(datos)

if __name__ == '__main__':
    main()
    plt.show()

# Cerrar la conexión con la base de datos
cursor.close()
conn.close()