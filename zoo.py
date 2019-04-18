# -*- coding: utf-8 -*-
# from habitat import *
# from animls import *
# miHabitat = None
# miAnimal = None
#habitat


# while True:
#     print('\n\t MENU \n')
#     print('1. Crear Habitat')
#     print('2. Modificar Habitat')
#     print('3. Crear Animal')
#     print('4. Modificar Animal')
#     print('5. Ver el Habitat') 
#     print('6. Ver el Animal')
#     print('7. Salir')
#     eleccion = input('Seleccionar una opcion: ')

#     if(eleccion == '1'):
#         print('Datos del habitat')
#         nombreHabitat = input('Nombre del Habitat: ')
#         extencion = input('extencion del Habitat')
#         miHabitat =  Habitat(nombreHabitat,extencion)

#     elif(eleccion == '2'):
#         print('\n\t Menu para modificar el habitat \n')
#         print('1. Modificar Nombre del Habitat: ')
#         print('2. Modificar extencion del Habitat: ')
#         print('3. Regresar al menu')
#         eleccion2 = input('Seleccionar una opcion: ')
#         if(eleccion2 == '1'):
#             nombreHabitat = input('Nombre del Habitat: ')
#             miHabitat.setnombreHabitat(nombreHabitat)
#         elif(eleccion2 == '2'):
#             extencion = input('extencion del Habitat')
#             miHabitat.setextencion(extencion)
#         elif(eleccion2 == '3'):
#             break
#         else:
#             print('OPCION INCORRECTA PRUEVA OTRA VEZ')

#     elif(eleccion == '3'):
#         print('Datos del Animal')
#         animal = input('El Animal es :')
#         especie = input("Especie del Animal:")
#         miAnimal = Animal(animal,especie)

#     elif(eleccion == '4'):
#         print('\n\t Menu para modificar los Datos del animal \n')
#         print('1. Modificar Nombre del Animal: ')
#         print('2. Modificar especie del animal: ')
#         print('3. Modificar comida:')
#         print('4. Modificar habilidad:')
#         print('5. Regresar al menu')
#         eleccion3 = input('Seleccionar una opcion: ')
#         if(eleccion3 == '1'):
#             animal= input('Nombre del Animal:')
#             miAnimal.setanimal(animal)
#         elif(eleccion3 == '2'):
#             especie = input("Especie del Animal:")
#             miAnimal.setespecie(especie)
#         elif(eleccion3 == '3'):
#             comida = input("comida del Animal:")
#             miAnimal.setcomida(comida)
#         elif(eleccion3 == '4'):
#             habilidad = input('habilidad del Animal:')
#             miAnimal.sethabilidad(habilidad)
#         elif(eleccion2 == '5'):
#             break
#         else:
#             print('OPCION INCORRECTA PRUEVA OTRA VEZ')

#     elif(eleccion == '5'):
#         print('\n\t Habitat\n')
#         print('Habitat:' + miHabitat.getnombreHabitat())
#         print('extencion:' + miHabitat.getextencion())

#     elif(eleccion == '6'):
#         print('\n\t Animal\n')
#         print('Animal:' + miAnimal.getanimal())
#         print('Especie:' + miAnimal.getespecie())
#         print('comida:' + miAnimal.getcomida())
#         print('habilidad:' + miAnimal.gethabilidad())

#     elif(eleccion == '7'):
#         print('Gracias por su visita')
#         break

#     else:
#         print('OPCION INCORRECTA PRUEVA OTRA VEZ')
