#Elaborado por: Laura Coto Sarmiento
#Fecha de Creación: XX/XX/XXXX 10am
#Fecha de modificación: XX/XX/XXXX 1pm

#importación de librerías
import pickle
diccMenu = {}
def grabar(nomArchGrabar,lista):
    try:
        f=open(nomArchGrabar,"wb")
        print("1.Voy a grabar el archivo: ", nomArchGrabar)
        pickle.dump(lista,f)
        print("1.Voy a cerrar el archivo: ", nomArchGrabar)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)
def leer(nomArchLeer):
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
def agregarIngred():
    ingred=[]
    t=int(input("¿Cuántos ingredientes lleva?"))
    while t>0:
        ingred.append(input("Ingrese Ingrediente: "))
        t-=1
    return ingred
def agregarProd(diccMenu):
    codigo = input("Código")
    nombre = input("Nombre ")
    precio= int(input("Precio "))
    ingred= agregarIngred()
    datosComida = [nombre,precio,ingred]
    diccMenu[codigo] = datosComida
    grabar("inventario",diccMenu)
    return diccMenu
def mostrarComida(diccMenu,codigo):
    datosComida = diccMenu[codigo]
    print("Código",codigo)
    print("  Nombre",datosComida[0])
    print("  Precio",datosComida[1])
    print("  Ingredientes",datosComida[2])
    print ("-------------------")
def eliminarComida(diccMenu,codigo):
    del(diccMenu[codigo])
    grabar("Comidas ",diccMenu)
def modificarComida(diccMenu, codigo):
    eliminarComida(diccMenu,codigo)
    agregarProd(diccMenu)
def mostrarTodasComidas(diccMenu):
    valores = list(diccMenu.keys())
    for valor in valores:
        mostrarComida(diccMenu,valor)
    print ("********************")
def menu():
    diccMenu=leer ("inventario")
    while True:
        print("1-Insertar Comida")
        print("2-Modificar Comida")
        print("3-Eliminar Comida")
        print("4-Consultar Comida")
        print("5-Terminar")
        opcion = int(input("Opción:"))
        if opcion == 1:
            agregarProd(diccMenu)
        elif opcion == 2:
            codigo = input("Indique el código a modificar:")
            modificarComida(diccMenu, codigo)
        elif opcion == 3:
            codigo = input("Indique el código a eliminar")
            eliminarComida(diccMenu,codigo)
        elif opcion == 4:
            cond=int(input("Comida específica(1) o Todos los productos(2): "))
            if cond==1:
                codigo = input("Indique el código a mostrar:")
                mostrarComida(diccMenu,codigo)
            else:
                mostrarTodasComidas(diccMenu)
        elif opcion == 5:
            grabar("inventario",diccMenu)
            break
#Programa Principal
menu()
