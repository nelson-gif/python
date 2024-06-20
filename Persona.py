class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido (self, apellido):
        self._apellido = apellido

    @property
    def edad (self):
        return self._edad

    @edad.setter
    def edad (self, edad):
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: nombre: {self._nombre}, apellido: {self.apellido}, edad: {self.edad}')

    def __del__(self):
        print(f' Objeto eliminado: Persona {self._nombre} {self.apellido} {self.edad}')

if __name__ == '__main__':
    persona1 = Persona('Juan', 'perez', 23)
    persona1.mostrar_detalle()

    print(persona1._nombre)
    print(persona1.nombre)

    persona1.nombre = 'nuevo nombre'
    print(persona1.nombre)

    print(__name__)

