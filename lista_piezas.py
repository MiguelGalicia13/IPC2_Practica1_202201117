from pieza import pieza 
from nodo_pieza import nodo_pieza
class lista_piezas:
    def __init__(self):
        self.primero = None
        self.contador_piezas=0
        self.filas=0
        self.columnas=0
    def insertar_dato(self,pieza):
        if self.primero is None:
            self.primero=nodo_pieza(pieza=pieza)
            self.contador_piezas += 1
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo_pieza(pieza=pieza)
            self.contador_piezas += 1
    def recorrer(self):
        print("")
        print("")
        actual = self.primero
        print("=================================================================")
        while actual != None:
            print("Fila: ",actual.pieza.fila," Columna: ",actual.pieza.columna," Color: ",actual.pieza.color)
            actual = actual.siguiente
        print("================================================================= \n")
    def inicializar_tablero(self,filas,columnas):
        for i in range(1,filas+1):
            for j in range(1,columnas+1):
                self.insertar_dato(pieza(i,j,"White"))

    def actualizar_pieza(self,fila,columna,color):
        actual = self.primero
        while actual != None:
            if actual.pieza.fila == fila and actual.pieza.columna == columna:
                actual.pieza.color = color
                print("Ahora la pieza es de color: ",actual.pieza.color)
                return
            actual = actual.siguiente
        print("\npieza no encontrada")
        print("\n Intente nuevamente")

    def devolver_color_de_pieza(self,fila,columna):
        actual=self.primero
        while actual!=None:
            if actual.pieza.fila==fila and actual.pieza.columna==columna:
                return actual.pieza.color
        actual=actual.siguiente

    def imprimir_tablero_en_consola(self):
        for i in range(1,self.filas+1):
            for j in range(1,self.columnas+1):
                print(self.devolver_color_de_pieza(i,j),end="\t")
        print("")
        print("")