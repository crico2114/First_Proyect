# crear una clase que contenga varios empleado
# esta clase debe terner varios propiedades Nombre, salario,y puesto de trabajo
# Calcular el salario después de un aumento (el aumento es un valor pasado como parámetro al método)
#Cambiar el puesto del empleado
# Mostrar la información del empleado devolviendo una cadena que muestre el nombre, el salario y el puesto del empleado.
# Crea una subclase Gerente que herede de Empleado y tenga un método adicional para asignar bonos. Crea instancias de Empleado y Gerente y prueba los métodos.
#Nota: llama lo métodos como mejor te parezca

class empleados:
    def __init__(self, nombre, puesto, salario):
        self.__nombre = nombre
        self.__puesto = puesto
        self.__salario = salario

    # metodo nuevo puesto
    def  cambiarpuesto(self, nuevopuesto):
        self.__puesto = nuevopuesto

#metodo nuevo salario
    def cambiarsalario(self, nuevosalario):
        self.__salario += nuevosalario
# metodo de bono
    def nuevobono (self, nuevobono):
        self.__bono = bonosalario

#como obtener la informacion
    def information(self):
        return f"nombre: {self.__nombre},puesto:{self.__puesto},salario:{self.__salario}"

# mostrar la informacion del empleado devolviendo una cadena que muestre el nombre , el salario, y el puesto del empleado

#clase de gerente bajo empleado
class Gerente(empleados):
    def __init__(self, nombre, puesto, salario):
        #super que es?


#variable?
employee1 = empleados( "Christian","Associate Product manager", 3000)
Gerente1 = Gerente("Paula", "gerente comercial", 7000)
print(employee1.information())
print(Gerente1.information())

#cambio de puesto y aumento/cambiar salario
employee1.cambiarsalario(3000)
employee1.cambiarpuesto("regional Product Manager")

#asignar bono a gerente
Gerente1.nuevobono(3000)

#como asignar el bono o quien?