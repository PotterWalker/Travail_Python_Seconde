#TP concernant les fonctions 
#Version Disponible sur Github sous le pseudonyme de Giyu Tomioka
#Fait par Daniel CHICHINADZE 
from math import *
from random import *

#Coordonnées d'un vecteur
def coord_vecteur(xA, yA, xB, yB):
    return (xB - xA, yB - yA)

print(coord_vecteur(1, 2, 4, 6))

#Coordonnées d'un milieu de segment

def milieu_segment(xA, yA, xB, yB):
    return ((xA + xB) / 2, (yA + yB) / 2)

print(milieu_segment(2, 4, 6, 8))

#Distance entre deux points

def distance_points(xA, yA, xB, yB):
    return (sqrt((xB - xA)**2 + (yB - yA)**2))

print(distance_points(0, 0, 3, 4))

#Symétrique d'un point 

def symetrique_point(xA, yA, xB, yB):
    return (2 * xB - xA, 2 * yB - yA)

print(symetrique_point(2, 3, 5, 6))

#Exercice 2

def surface(L, M):
    s = (sqrt(L * M))/6
    return s

print(surface(1.75, 70))

#Exercice 3

print(random())

def reel_aleatoire(a, b):
    return randint(a, b)

print(reel_aleatoire(1, 10))

def lancerdes(): 
    nombre1 = randint(1, 6)
    nombre2 = randint(1, 6)
    return nombre1 + nombre2

print(lancerdes())

#Exercice 4

def temps_en_seconde(h, m, s):
    return h * 3600 + m * 60 + s

print(temps_en_seconde(1, 30, 45))