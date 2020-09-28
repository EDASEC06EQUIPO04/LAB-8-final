"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


#crimefile = 'crime-utf8.csv'
accidentFile='us_accidents_small.csv'



def printAccident(info, lista):
        aux=[]
        totalcounter=0
        #print (info['accidents'])
        info=lt.getElement(info['accidents'],0)
        
        iterator = it.newIterator(info['id'])

        while it.hasNext(iterator):
            accidente = it.next(iterator)
            totalcounter+=1
            aux.append(accidente["Severity"])
        for x in aux:
            result = controller.getIdInfo(cont, x)
            print(result['ID']['Severity']["Start_Time"])
        print ('Total de accidentes [ ', totalcounter, '] en el dia [', result["Start_Time"])
        


# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@") 
    print("@@@@@@@@@                         RETO 3. Seguridad en las vias                @@@@@@@@@@@")   
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@") 
    print("[1] Inicializar Analizador")
    print("[2] Cargar información de accidentes")
    print("[3] Requerimento 1: Conocer los accidentes en una fecha")
    print("[4] Requerimento 2: Conocer los accidentes anteriores a una fecha")
    print("[5] Requerimento 3: Conocer los accidentesen un rango de fechas")
    print("[6] Requerimento 4: Conocer el estado con mas accidentes")
    print("[7] Requerimento 5: Conocer los accidentes por rango de horas")
    print("[8] Requerimento 6: Conocer las zona geografica mas accidentada")
    print("[9] Requerimento 7: Usar el conjunto completo de datos")
    print("[0]- Salir")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@") 


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar >> ')

    if int(inputs[0]) == 1:

        print("\nInicializando lista Analyzer y mapa ordenado dateIndex....")
        cont = controller.init()
        #lt.addLast(cont['accidents'],"Dato de prueba de de la lista.. OKKKK")
        #dato=lt.getElement(cont['accidents'],0) 

        print (cont['accidents'])
        #print (dato)

        input("Ahora la mapa ordenado dateIndex")
        print (cont['dateIndex'])
        print ("")
        input("Se acaba de crear el Catalogo Analyzer con su respectiva lista y un mapa ordenado tipo BST")
        # cont es el controlador que se usará de acá en adelante
       

    elif int(inputs[0]) == 2:

        print("\n Cargando información de accidentes ....\n")

        controller.loadData(cont, accidentFile)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@") 
        print (lt.getElement(cont['accidents'],0))
        print (lt.getElement(cont['accidents'],controller.accidentSize(cont)))
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        #for i  in range (0,controller.accidentSize(cont)):
        #   print (lt.getElement(cont['accidents'],i))
        print ("")
        print('Accidentes cargados: ' + str(controller.accidentSize(cont)))
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))
        print("")
        input("Clic para continuar")
        ###
        input("Clic para continuar")

    elif int(inputs[0]) == 3:
        print("\nBuscando crimenes en un rango de fechas: ")
        initialDate = input("Rango Inicial (YYYY-MM-DD): ")       
        finalDate = input("Rango Final (YYYY-MM-DD): ")
        lst = controller.getAccidentsByRange(cont, initialDate,finalDate)
        print("\nTotal de llaves en el rango: " + str(lt.size(lst)))
        printAccident(cont,lst)



    elif int(inputs[0]) == 4:
        print("\nRequerimiento No 1 del reto 3: ")

    else:
        sys.exit(0)
sys.exit(0)
