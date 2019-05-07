class Animal():
    def __init__(self, animal,especie,nombre):
        self.animal = animal
        self.especie = especie
        self.nombre = nombre

class Habitat():
    def __init__(self, nombre, extencion):
        self.nombre = nombre
        self.extencion = extencion
        self.animales = []

    def agregarAnimal(self):
        nombreAnimal = input('Ingresa el nombre del animal:')
        nombreEspecie = input('Ingresa la especie del animal:')
        nombrePila = input('ingresa el nombre de pila:') 
        nuevoAnimal = Animal(nombreAnimal,nombreEspecie,nombrePila)
        self.animales.append(nuevoAnimal)

    def verAnimal(self):
        for recorer in self.animales:
            print ("Animal:", recorer.animal,'\nEspecie:', recorer.especie,"\nNombre:", recorer.nombre)


class Zoo():
    def __init__(self):
        self.habitats = []
    
    def agregarHabitat(self):
        nombreHabitat = input("Ingrese el nombre de habitat:")
        extencionHabitat = input("Ingrese la extencion del habitat:")
        nuevoHabitat = Habitat(nombreHabitat, extencionHabitat)
        self.habitats.append(nuevoHabitat)                                    

    def verhabitat(self):
        for i in self.habitats:
            print('Nombre:',i.nombre,'\nExtencion:', i.extencion)


zoo1 = Zoo()
Habitat1 = Habitat(1,2)

while True:
    print('\n\t MENU \n'
    '1. Crear Habitat\n' 
    '2. Crear Animal\n'
    '3. Ver el Habitat\n' 
    '4. Ver el Animal\n'
    '5. Salir')  
    eleccion = input('Seleccionar una opcion:')

    if (eleccion == '1'):
        print('\n\t Creacion del Habitat \n')
        zoo1.agregarHabitat()

    elif(eleccion == '2'): 
        print('\n\t Creacion del Animal \n')
        Habitat1.agregarAnimal() 

    elif(eleccion == '3'):
        print('\n\t Datos del habitat \n')
        zoo1.verhabitat()
        Habitat1.verAnimal()  
        
    elif(eleccion == '4'):
        print('\n\t Datos del animal \n')
        Habitat1.verAnimal()

    elif(eleccion == '5'):
        print('\n \t Gracias por su visita \n')
        break
    
    else:
        print('\n \t OPCION INCORRECTA PRUEVA OTRA VEZ \n')

   





