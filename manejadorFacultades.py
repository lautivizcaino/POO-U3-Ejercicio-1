from clasefacultad import Facultad
from clasecarrera import Carrera
import csv
class ManejadorFacultades:
    __listaFacultades= list
    def __init__(self):
        self.__listaFacultades=[]
    
    def añadirFacultad(self,facultad):
        self.__listaFacultades.append(facultad)

    def leerArchivo(self):
        file = open('carreras.csv',encoding='utf-8')
        reader = csv.reader(file,delimiter=',')
        i=0
        for row in reader:
            if int(row[0])>i:
                codigo=int(row[0])
                nombre=row[1]
                direccion=row[2]
                telefono=row[4]
                self.añadirFacultad(Facultad(codigo,nombre,direccion,telefono))
                i+=1
            elif int(row[0])==i:
                codigo=int(row[1])
                nombre=row[2]
                titulo=row[3]
                duracion=row[4]
                unaFacultad=self.__listaFacultades[int(row[0])-1].getFacultad()
                unaFacultad.agregarCarrera(codigo,nombre,duracion,titulo)

    def ingresarCodigo(self,codigo):
        i= 0
        while i!= -1:
            if codigo==self.__listaFacultades[i].getCodigo():
                facultad=self.__listaFacultades[i].getFacultad()
                print('Nombre: %s\n'%self.__listaFacultades[i].getNombre())
                listaCarreras=self.__listaFacultades[i].getLista()
                for carrera in listaCarreras:
                    print('Nombre: %s Duracion: %s'%(carrera.getNombre(),carrera.getDuracion()))
                i=-1
            else:
                i+=1
    def ingresarNombre(self,nombre):
        i= 0
        while i<len(self.__listaFacultades):
            listaCarreras=self.__listaFacultades[i].getLista()
            j=0
            while j<len(listaCarreras):
                if listaCarreras[j].getNombre()==nombre:
                    print('Codigo: %s,%s'%(self.__listaFacultades[i].getCodigo(),listaCarreras[j].getCodigo()))
                    print('Nombre: %s Localidad: %s'%(self.__listaFacultades[i].getNombre(),self.__listaFacultades[i].getLocalidad()))
                    i=len(self.__listaFacultades)
                    j=len(listaCarreras)
                j+=1
            else:
                i+=1
    
    def eliminar(self,codigo):
        del self.__listaFacultades[codigo-1]
        print('Se eliminó la Facultad %d\n'%codigo)

    def __str__(self):
        s=''
        for facultad in self.__listaFacultades:
            s+=str(facultad) + '\n'
        return s