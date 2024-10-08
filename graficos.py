import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Conectar a la base de datos MySQL
def conectar_bd():
    return mysql.connector.connect(
        host="localhost",  # Cambia por tu host si es diferente
        user="root",  # Cambia por tu usuario de MySQL
        password="",  # Cambia por tu contraseña de MySQL
        database="tienda01"  # Cambia por el nombre de tu base de datos
    )

# Función para capturar los datos
def capturar_datos():
    conn = conectar_bd()
    cursor = conn.cursor()
    
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    salario = float(input("Ingrese el salario: "))
    
    cursor.execute("INSERT INTO datos (nombre, edad, salario) VALUES (%s, %s, %s)", (nombre, edad, salario))
    conn.commit()
    
    cursor.close()
    conn.close()

# Función para consultar los datos y obtener estadísticas
def obtener_estadisticas():
    conn = conectar_bd()
    cursor = conn.cursor()
    
    # Consulta de todos los datos
    cursor.execute("SELECT edad, salario FROM datos")
    data = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    # Convertir los datos a un DataFrame de pandas para generar estadísticas
    df = pd.DataFrame(data, columns=["Edad", "Salario"])
    
    # Generar estadísticas básicas
    estadisticas = df.describe()
    print(estadisticas)
    
    # Guardar los datos en un archivo CSV
    df.to_csv('datos_estadisticos.csv', index=False)
    
    return df

# Función para generar la gráfica
def generar_grafica(df):
    # Crear un gráfico de dispersión de Edad vs Salario
    plt.scatter(df["Edad"], df["Salario"], color='blue')
    plt.title('Edad vs Salario')
    plt.xlabel('Edad')
    plt.ylabel('Salario')
    plt.grid(True)
    plt.savefig('grafico_edad_salario.png')
    plt.show()

# Función principal
def main():
    while True:
        print("1. Capturar datos")
        print("2. Obtener estadísticas y generar gráfica")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            capturar_datos()
        elif opcion == '2':
            df = obtener_estadisticas()
            generar_grafica(df)
        elif opcion == '3':
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
