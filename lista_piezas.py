from pieza import pieza 
from nodo_pieza import nodo_pieza

import sys
import os

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
        actual=self.primero
        while actual!=None:
            if actual.pieza.fila==fila and actual.pieza.columna==columna:
                actual.pieza.color=color
                print("Se pintó la pieza con éxito!")
                return
            actual=actual.siguiente
        print("Posición de pieza no encontrada, intente de nuevo!")

    def devolver_color_de_pieza(self,fila,columna):
        actual=self.primero
        while actual!=None:
            if actual.pieza.fila==fila and actual.pieza.columna==columna:
                return actual.pieza.color
            actual=actual.siguiente

    def imprimir_tablero_en_consola(self):
        print("===========Tablero=============")
        for i in range (1,self.filas+1):
            for j in range (1,self.columnas+1):
                print(self.devolver_color_de_pieza(i,j),end="\t")
            print("")
        print("")
    def generar_garfica(self):
        f = open('IPC2_Practica1_202201117/aa.dot','w')
        texto="digraph G {\nnode [shape=circle];\nlabel=\"Colorealo GuateMatel\";\nsome_node [\nlabel=<\n<table border=\"0\" cellborder=\"1\" cellspacing=\"1\" width=\"100%\" height=\"100%\">\n"
        texto+="<tr>\n"
        for a in range(0, self.columnas + 1):
            texto+="<td bgcolor=\"yellow\" width=\"10\" height=\"10\" >"+str(a)+"</td>\n"
        texto+="</tr>\n"
        for i in range(1, self.filas + 1):
            texto+="<tr>\n"
            texto+="<td bgcolor=\"yellow\" width=\"10\" height=\"10\" >"+str(i)+"</td>\n"
            for j in range(1, self.columnas + 1):
                texto+="<td bgcolor=\""+self.devolver_color_de_pieza(i,j)+"\" width=\"10\" height=\"10\">"+"</td>\n"
            texto+="</tr>\n"
        texto+="</table>>\n];\n}"
        f.write(texto)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system('dot -Tpng IPC2_Practica1_202201117/aa.dot -o IPC2_Practica1_202201117/Tablero.png')
        print("Se ha generado la Grafica")