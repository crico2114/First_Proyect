# crear una clase que contenga varios empleado
# esta clase debe terner varios propiedades Nombre, salario,y puesto de trabajo
# Calcular el salario después de un aumento (el aumento es un valor pasado como parámetro al método)
#Cambiar el puesto del empleado
# Mostrar la información del empleado devolviendo una cadena que muestre el nombre, el salario y el puesto del empleado.
# Crea una subclase Gerente que herede de Empleado y tenga un método adicional para asignar bonos. Crea instancias de Empleado y Gerente y prueba los métodos.
#Nota: llama lo métodos como mejor te parezca

class Empleados:
    def __init__(self, nombre, puesto, salario):
        self.__nombre = nombre
        self.__puesto = puesto
        self.__salario = salario

    # metodo nuevo puesto
    def cambiarpuesto(self, nuevopuesto):
        self.__puesto = nuevopuesto

#metodo nuevo salario
    def cambiarsalario(self, nuevosalario):
        self.__salario += nuevosalario

#como obtener la informacion
    def information(self):
        return f"nombre: {self.__nombre},puesto:{self.__puesto},salario:{self.__salario}"
    def nuevo_bono (self, nuevo_bono):
        self.__salario += nuevo_bono

# mostrar la informacion del empleado devolviendo una cadena que muestre el nombre , el salario, y el puesto del empleado

#clase de gerente bajo empleado
class Gerente(Empleados):
    def __init__(self, nombre, puesto, salario):
        Empleados.__init__(self, nombre, puesto, salario)



#variable?
employee1 = Empleados( "Christian","Associate Product manager", 3000)
print(employee1.information())


gerente1 = Gerente("Paula", "gerente comercial", 4000)
print(gerente1.information())

#cambio de puesto y aumento/cambiar salario
employee1.cambiarsalario(10000)
employee1.cambiarpuesto("Regional Product Manager")
print(employee1.information())



gerente1.cambiarpuesto("Regional comercial manager")
gerente1.nuevo_bono(8000)
#como asignar el bono o quien?



print(gerente1.information())
