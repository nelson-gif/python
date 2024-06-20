from Persona import Persona

print('creacion del objeto'.center(30, '-'))
persona1 = Persona('karla', 'Gomez', 30)
print(persona1.nombre)
print(__name__)

print('eliminacion del objeto'.center(30, '-'))
del persona1
