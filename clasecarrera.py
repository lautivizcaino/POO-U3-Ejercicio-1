class Carrera:
    __codigo : int
    __nombre : str
    __fecha = '9/12/2018'
    __duracion : str
    __titulo : str
    __facultad: object
    def __init__(self,codigo,nombre,duracion,titulo):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__duracion=duracion
        self.__titulo=titulo

    def getNombre(self):
        return self.__nombre
    def getDuracion(self):
        return self.__duracion
    def getCodigo(self):
        return self.__codigo

    def __str__(self):
        return '%s %s %s %s %s'%(self.__codigo,self.__nombre,self.__fecha,self.__duracion,self.__titulo)