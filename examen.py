# Christian Romero Oliva 1º DAW
# Este programa devuelve las tablas de multiplicar correspondientes a un mes y un rango de edad.

"""
Esta función toma un parámetro mínimo y otro máximo para escribir las tablas de multiplicar
y un valor adicional para especificar si nos queremos quedar con las tablas pares, impares o ambas.

Argumentos:
    num1: Tabla por la que empieza
    num2: Tabla - 1 por la que acaba
    parimpar: 1 para impar, 2 para par, 0 para ambos.
"""
def tablas(num1, num2, parimpar):
    for n in range(num1, num2):

        if parimpar == 1:
            if n % 2 == 0:
                continue
        if parimpar == 2:
            if n % 2 != 0:
                continue
        if parimpar == 0:
            n = n

        for i in range(10):
            if i == 0:
                print("\n", "TABLA DEL", n, "\n"
                                            "****************")
            resultado = i * n
            print(i, "x", n, "=", resultado)

"""
Esta función comprueba en que rango se encuentra la edad y el mes, luego devuelve un valor que
 asigna un caso que se pasa a la función tabla_corresponde().
 
 Argumentos: edad, mes
 Devuelve: [0,4]
"""
def comprueba_rango(edad, mes):
    if 10 < edad <= 12:
        return 0

    elif 8 < edad <= 10 and mes % 2 == 0:
        return 1

    elif 8 < edad <= 10 and mes % 2 != 0:
        return 2

    elif 6 <= edad <= 8 and mes % 2 == 0:
        return 3

    elif 6 <= edad <= 8 and mes % 2 != 0:
        return 4

"""Esta función va a recibir la edad y va a comprobar si se encuentra en un rango posible.

Argumentos: edad
Devuelve: False o None
"""

def comprueba_edad(edad):
    try:
        if int(edad) < 0:
            return False
        elif int(edad) < 6:
            return False
        elif int(edad) > 12:
            return False

    except ValueError:
        return False

"""Esta función va a recibir el mes y va a comprobar si se encuentra en un valor posible.

Argumentos: mes
Devuelve: False o None
"""
def comprueba_mes(mes):
    try:
        if int(mes) < 0:
            return False
        elif int(mes) > 12:
            return False

    except ValueError:
        return False


"""Ésta función toma el valor del caso asignado por comprueba_rango() y devuelve un valor del 0 al 4. 
  Ese valor se le pasa a imprime_tabla()
  
  Argumentos: caso
  Devuelve: [0,4]
  """

def tabla_corresponde(caso):
    if caso == 0:
        return 0
    elif caso == 1:
        return 1
    elif caso == 2:
        return 2
    elif caso == 3:
        return 3
    elif caso == 4:
        return 4

"""Ésta función toma el caso asignado por tabla_corresponde() y en función a el imprime las tablas deseadas
mediante la funcion tablas().

  Argumentos: tabla
  Devuelve: Una impresion por pantalla de las tablas deseadas

  """
def imprime_tabla(tabla):
    if tabla == 0:
        tablas(11, 14, 0)
        return "11,12,13"
    elif tabla == 1:
        tablas(6, 11, 2)
        return "6,8,10"
    elif tabla == 2:
        tablas(7, 10, 1)
        return "7,9"
    elif tabla == 3:
        tablas(1, 6, 2)
        return "2,4"
    elif tabla == 4:
        tablas(1, 6, 2)
        return "1,3,5"


if __name__ == "__main__":
    print("▄" * 64) # Para que de un poco impresión de interfaz gráfica.
    alumno = input("Introduzca su nombre: ")
    titulo = f"PROGRAMA DE GENERACIÓN DE TABLAS: {alumno}"
    print("─" * len(titulo) + "\n" + titulo + "\n" + "─" * len(titulo))

    print("▄" * 64)

    while True:
        edad = input("Introduce tu edad: ")

        if comprueba_edad(edad) == False:
            print("No se contempla esa edad")

        mes = input("Introduce el mes: ")

        if comprueba_mes(mes) == False:
            print("Mes no válido")

        if comprueba_edad(edad) == False or comprueba_mes(mes) == False:
            print("Fallo al introducir los datos.")
            continue
        else:
            break

    # Cree estas dos variables para hacer los pases entre funciones de forma más cómoda
    caso = comprueba_rango(int(edad), int(mes))
    tabla = tabla_corresponde(caso)
    print(f"{alumno}, le corresponden las siguientes tablas", imprime_tabla(tabla))

    comprueba_rango(int(edad), int(mes))

    print("▄" * 64)






