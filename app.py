from lista_piezas import lista_piezas
mi_tablero=lista_piezas()
def configurar_tablero(fila_ingresar,columna_ingresar):
    print("\n")
    print("==================================================")
    print("Configuracion de tablero")
    print("==================================================\n")
    mi_tablero.inicializar_tablero(fila_ingresar,columna_ingresar)
    mi_tablero.recorrer()
    print("\n==================================================")
    print("Configuracion de piezas")
    print("==================================================\n")
    nueva_pieza = True
    while nueva_pieza:
        fila=int(input("Ingrese la fila de la pieza: \n"))
        columna=int(input("Ingrese la columna de la pieza: \n"))
        color=input("Ingrese el color de la pieza: \n")
        mi_tablero.actualizar_pieza(fila,columna,color)
        print("")
        mi_tablero.imprimir_tablero_en_consola()
        seguir=input("\n Desea ingresar otra pieza? (s/n) \n")
        if seguir=="n":
            nueva_pieza=False
    print("Fin de la configuracion de piezas")
    mi_tablero.imprimir_tablero_en_consola()
    print("\n==================================================")
    print("Fin de la configuracion de tablero")
    print("==================================================\n")

def menu():
    print("\n")
    print("==================================================")
    print("Menu")
    print("==================================================")
    print("1. Crear tablero")   
    print("2. Datos del estudiante")
    print("3. Salir")
    opcion=input("Ingrese una opcion: \n")
    while True:
        match opcion:
            case "1":
                print(" \n ==================================================")
                print("Creando tablero")
                fila = int(input("Ingrese el numero de filas: \n"))
                columna = int(input("Ingrese el numero de columnas: \n"))
                configurar_tablero(fila,columna)
                mi_tablero.imprimir_tablero_en_consola()
                
                menu()
            case "2":
                print(" \n ==================================================")
                print("                        Datos del Estudiante                 ")
                print("==================================================")
                print("Miguel Ricardo Galicia Urrutia")
                print("202201117")
                print("Introduccion a la Programacion y Computacion 2 seccion \"A\"")
                print("Ingenieria en Ciencias y Sistemas")
                print("4to Semestre \n")
                menu()
            case "3":
                break
            case _:
                print("Opcion invalida")
                menu()
        return False
    
menu()
print("\n ------------------------")
print("Ejecucion finalizada")
print("------------------------\n")