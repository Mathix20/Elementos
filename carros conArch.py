#Elaborado por: Laura Coto Sarmiento
#Fecha de Creación: XX/XX/XXXX 10am
#Fecha de modificación: XX/XX/XXXX 1pm

#importación de librerías
#Ejemplo de uso del Pickle
import pickle

#Inicialización de variables globales
diccCarros = {}

#Función que graba un archivo con una lista de estudiantes
def graba(nomArchGrabar,lista):
    try:
        f=open(nomArchGrabar,"wb")
        print("1.Voy a grabar el archivo: ", nomArchGrabar)
        pickle.dump(lista,f)
        print("1.Voy a cerrar el archivo: ", nomArchGrabar)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)

#Función que lee un archivo con una lista de estudiantes
def lee (nomArchLeer):
    dicc={}
    try:
        f=open(nomArchLeer,"rb")
        print("2. Voy a leer el archivo: ", nomArchLeer)
        dicc = pickle.load(f)
        print("2. Voy a cerrar el archivo: ", nomArchLeer)
        f.close()
    except:
        print("Error al leer el archivo: ", nomArchLeer)
    return dicc

#definición de Funciones
def agregarCarro(diccCarros):
    placa = input("Placa: ")
    marca = input("Marca: ")
    anno = int(input("Año: "))

    # Crea lista con datos del carro
    #datosCarro = []
    #datosCarro.append(marca)
    #datosCarro.append(anno)
    datosCarro = [marca,anno]
    #crea los valores como una lista

    # Agrega a diccionario el carro
    diccCarros[placa] = datosCarro

    #Guarda el diccionario en un archivo
    graba("inventario",diccCarros)
    return diccCarros

def mostrarCarro(diccCarros,placa):
    infoCarro = diccCarros[placa]
    print("Placa:",placa)
    print("  Marca:",infoCarro[0])
    print ("  Año:",infoCarro[1])
    print ("-------------------")

def eliminarCarro(diccCarros,placa):
    del(diccCarros[placa])
    #Guarda el diccionario en un archivo
    graba("inventario",diccCarros)

def mostrarTodosCarros(diccCarros):
    claves = list(diccCarros.keys())
    for clave in claves:
        mostrarCarro(diccCarros,clave)
    print ("********************")

def menu():
    diccCarros=lee ("inventario")
    while True:
        print("1-Agregar Carro")
        print("2-Mostrar Carro")
        print("3-Eliminar Carro")
        print("4-Mostrar Todos los Carros")
        print("5-Terminar")
        opcion = int(input("Opción:"))
        if opcion == 1:
            agregarCarro(diccCarros)
        elif opcion == 2:
            placa = input("Indique la placa a mostrar:")
            mostrarCarro(diccCarros,placa)
        elif opcion == 3:
            placa = input("Indique la placa a eliminar:")
            eliminarCarro(diccCarros,placa)
        elif opcion == 4:
            mostrarTodosCarros(diccCarros)
        elif opcion == 5:
            #Guarda el diccionario en un archivo
            graba("inventario",diccCarros)
            break
        
#Programa Principal
menu()
        
