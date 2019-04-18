# -*- coding: utf-8 -*-
class Habitat():
    nombreHabitat = ''
    extencion = ''

    def __init__(self,nombreHabitat,extencion):
        self.nombreHabitat= nombreHabitat
        self.extencion = extencion
        self.animales = []

    def getnombreHabitat(self):
        return self.nombreHabitat

    def getextencion(self):
        return self.extencion

    def setnombreHabitat(self,nuevoNombreHabitat):
        self.nombreHabitat = nuevoNombreHabitat

    def setextencion(self,nuevoextencion):
        self.extencion = nuevoextencion
