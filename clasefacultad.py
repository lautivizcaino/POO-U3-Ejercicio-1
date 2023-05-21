from clasecarrera import Carrera
import csv
class Facultad:
    __codigo : int
    __nombre: str
    __direccion : str
    __localidad = 'San Juan'
    __telefono : str
    __carreras : list

    def __init__(self,codigo,nombre,direccion,telefono):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__carreras=[]

    def getFacultad(self):
        return self
    def agregarCarrera(self,codigo,nombre,titulo,duracion):
        self.__carreras.append(Carrera(codigo,nombre,titulo,duracion))

    def getCodigo(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre
    def getLista(self):
        return self.__carreras
    def getLocalidad(self):
        return self.__localidad
    def getdireccion(self):
        return self.__direccion
    def __del__(self):
        for carrera in self.__carreras:
            print('BOOM')
            del carrera
    
    def __str__(self):
        s=''
        for carrera in self.__carreras:
            s+=str(carrera) + '\n'
        return '%s %s %s %s %s \n%s'%(self.__codigo,self.__nombre,self.__direccion,self.__localidad,self.__telefono,s)
