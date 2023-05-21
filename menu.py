from manejadorFacultades import ManejadorFacultades
class Menu:
    __opcion=int
    def __init__(self):
        self.__opcion=3
    def opciones(self,lista):
        while self.__opcion!=0:
            print('1 - Mostrar Facultad\n2 - Mostrar Carrera\n3 - ELIMINAR FACULTAD\n0 - Salir\n')
            self.__opcion=int(input('Ingrese la opcion a ejecutar: '))
            if self.__opcion==1:
                print('\nPUNTO 1')
                lista.ingresarCodigo(int(input('Ingrese codigo de Facultad: ')))

            elif self.__opcion==2:
                print('\nPUNTO 2')
                lista.ingresarNombre(input('Ingrese nombre de carrera: '))
            elif self.__opcion==3:
                print('PUNTO 3')
                lista.eliminar(int(input('Ingrese codigo de Facultad a eliminar: ')))
            
        else:
            print('\nHa salido del sistema')
