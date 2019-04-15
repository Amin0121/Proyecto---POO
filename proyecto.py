class Zoo():
  def __init__(self, habitats = []):
    self.__habitats = habitats

class habitat():
  def __init__(self, limite, animalesActuales, listaEspera,animlesQuetiene):
    self.__limite = limite
    self.__animalesActuales = len(animlesQuetiene)
    self.__listaEspera = listaEspera        
    self.__animlesQuetiene = animlesQuetiene


  def estado(self):
    print("Limite de animales:", self.__limite,'\nAnimales actuales:',self.__animalesActuales,'\nLista de espera:',self.__listaEspera,'\nAnimales que tiene:',self.__animlesQuetiene)

class Animal():
  
  def __init__(self, animal, especie, comida, nombre, habilidad):
    self.__animal = animal
    self.__especie = especie
    self.__comida = comida
    self.__nombre = nombre
    self.__habilidad = habilidad


  def est(self):
    print("\nAnimal:",self.__animal,"\nEspecie: ",self.__especie,"\nComida favorita:",self.__comida,'\nNombre:',self.__nombre,'\nHabilidad:',self.__habilidad)



