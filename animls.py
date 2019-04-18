# -*- coding: utf-8 -*-
class Animal():
    animal = ''
    especie = ''
    comida = ''
    habilidad = ''

    def __init__(self,animal,especie):
        self.animal = animal
        self.especie = especie


    def getanimal(self):
        return self.animal

    def getespecie(self):
        return self.especie

    def getcomida(self):
        return self.comida

    def gethabilidad(self):
        return self.habilidad



    def setanimal(self,nuevoAnimal):
        self.animal = nuevoAnimal

    def setespecie(self,nuevaEspecie):
        self.especie = nuevaEspecie 

    def setcomida(self,nuevaComida):
        self.comida = nuevaComida

    def sethabilidad(self,nuevaHabilidad):
        self.habilidad =  nuevaHabilidad
