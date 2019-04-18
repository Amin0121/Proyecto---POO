class Animal():
    def __init__(self, animal,especie,nombre):
        self.animal = animal
        self.especie = especie
        self.nombre = nombre

class Habitat():
    def __init__(self, nombre, extencion):
        self.nombre = nombre
        self.extencion = extencion
        self.animales = [ ]

    def agregarAnimal(self):
        nombreAnimal = input('Ingresa el nombre del animal:')
        nombreEspecie = input('Ingresa la especie del animal:')
        nombrePila = input('ingresa el nombre de pila:')
        nuevoAnimal = Animal(nombreAnimal,nombreEspecie,nombrePila)
        self.animales.append(nuevoAnimal)

class Zoo():
    def __init__(self):
        self.habitats = []
    
    def agregarHabitat(self):
        nombreHabitat = input("Ingrese el nombre de habitat")
        extencionHabitat = input("Ingrese la extencion del habitat")
        nuevoHabitat = Habitat(nombreHabitat, extencionHabitat)
        self.habitats.append(nuevoHabitat)
    
    def verhabitat(self):
        for i in self.habitats:
            print(i.nombre, i.extencion, "\n")
        
zoo1 = Zoo()
zoo1.agregarHabitat()
print(zoo1.habitats[0].__dict__)

Habitat1 = Habitat(1,2)
Habitat1.agregarAnimal()
print(Habitat1.animales[0].__dict__)





