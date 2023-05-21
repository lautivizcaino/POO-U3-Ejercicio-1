from clasefacultad import Facultad
from clasecarrera import Carrera
from manejadorFacultades import ManejadorFacultades
from menu import Menu
def test():
    lista=ManejadorFacultades()
    lista.leerArchivo()
    menu=Menu()
    menu.opciones(lista)

if __name__ =='__main__':
    test()