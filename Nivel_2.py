import pygame
from io import open
from pygame import mixer
import random
import math
import time
import sys
import Cinematica_1_1

pygame.init()
linea1 = ''
linea2 = ''
contadordialogo = 0
contadorcinematica = 0
cinematicadialogo1estado = True
cinematicadialogo2estado = False
cinematicadialogo3estado = False
cinematicadialogo4estado = False
cinematicadialogo5estado = False
cinematicadialogo6estado = False
cinematicadialogo7estado = False
escribiendosonidoestado = "listo"
fase2 = False
fase3 = False
fondo1x = 0
fondo2x = 2560
cinematicadialogo1 = ['L', 'u', 'e', 'g', 'o', ' ', 'd', 'e', ' ', 'm', 'e', 's', 'e', 's', ' ', 'd', 'e', ' ', 'd',
                    'u', 'r', 'o', ' ', 't', 'r', 'a', 'b', 'a', 'j', 'o', ',', ' ', 'l', 'o', 'g', 'r', 'a', 'm',
                    'o', 's', ' ', 'e', 'n', 'c', 'o', 'n', 't', 'r', 'a', 'r', ' ', 'e', 'l', ' ', 'l', 'a', 'b',
                    'o',
                    'r', 'a', 't', 'o', 'r', 'i', 'o', ' ', 's', 'e', 'c', 'r', 'e', 't', 'o', ' ', 'd', 'e', ' ',
                    'l',
                    'a', ' ', 'F', '.', 'A', '.', 'R', '.', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
cinematicadialogo2 = ['S', 'e', ' ', 't', 'r', 'a', 't', 'a', ' ', 'd', 'e', ' ', 'u', 'n', 'a', ' ', 'b', 'a', 's',
                    'e',
                    ' ', 'o', 'c', 'u', 'l', 't', 'a', ' ', 'e', 'n', ' ', 'u', 'n', ' ', 'p', 'e', 'q', 'u', 'e', 'ñ', 'o', ' ', 'p', 'l', 'a', 'n', 'e',
                    't','a', ',', ' ', 'd',
                    'o', 'n', 'd', 'e', ' ', 's', 'e', ' ', 'c', 'r', 'e', 'e', ',', ' ', 'v', 'i', 'v', 'e', 'n',
                    ' ',
                    's', 'o', 'l', 'o', ' ', 'm', 'i', 'e', 'm', 'b', 'r', 'o', 's', ' ', 'd', 'e', ' ', 'l', 'a',
                    ' ',
                    'F', '.', 'A', '.', 'R', '.', ' ', 'o', 'c', 'u', 'l', 't', 'o', 's', ' ', 'c', 'o', 'm', 'o',
                    ' ',
                    'c', 'i', 'v', 'i', 'l', 'e', 's', '.', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'A', 'd', 'e', 'm', 'á', 's', ',', ' ',
                    'h',
                    'a', 'y', ' ', 'r', 'u', 'm', 'o', 'r', 'e', 's', ' ', 'd', 'e', ' ', 'q', 'u', 'e', ' ', 's',
                    'e',
                    ' ', 'e', 'x', 'p', 'e', 'r', 'i', 'm', 'e', 'n', 't', 'a', ' ', 'c', 'o', 'n', ' ', 'a', 'n',
                    'i',
                    'm', 'a', 'l', 'e', 's', ' ', 'p', 'a', 'r', 'a', ' ', 't', 'r', 'a', 'n', 's', 'f', 'o', 'r',
                    'm',
                    'a', 'r', 'l', 'o', 's', ' ', 'e', 'n', ' ', 'h', 'o', 'r', 'r', 'i', 'b', 'l', 'e', 's', ' ',
                    'm',
                    'a', 'q', 'u', 'i', 'n', 'a', 's', ' ', 'd', 'e', ' ', 'g', 'u', 'e', 'r', 'r', 'a', '.', '.',
                    '.', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
cinematicadialogo3 = ['T', 'u', ' ', 'o', 'b', 'j', 'e', 't', 'i', 'v', 'o', ' ', 's', 'e', 'r', 'á', ' ', 'i', 'n', 'f',
                    'i', 'l', 't', 'r', 'a', 'r', 't', 'e', ' ', 'y', ' ', 'd', 'a', 'r', 'l', 'e', ' ', 'u', 'n', ' ',
                    'a', 't', 'a', 'q', 'u', 'e', ' ', 's', 'o', 'r', 'p', 'r', 'e', 's', 'a', ' ', 'a', 'l', ' ', 'e',
                    'n', 'e', 'm', 'i', 'g', 'o', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
cinematicadialogo4 = ['B', 'o', 'm', 'b', 'a', ':', ' ', 'I', 'd', 'e', 'a', 'l', ' ', 'p', 'a', 'r', 'a', ' ', 'd', 'e',
                    's', 't', 'r', 'u', 'i', 'r', ' ', 'e', 'd', 'i', 'f', 'i', 'c', 'i', 'o', 's', ' ', 'y', ' ', 'o', 'b',
                    'j', 'e', 't', 'i', 'v', 'o', 's', ' ', 't', 'e', 'r', 'r', 'e', 's', 't', 'r', 'e', 's', ' ', 'c', 'o', 'n', ' ', 'g', 'r',
                    'a', 'n', ' ', 'b', 'l', 'i', 'n', 'd', 'a', 'j', 'e', '.', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                    'L', 'a', 'n', 'z', 'a', ' ', 'c', 'o', 'h', 'e', 't', 'e', 's', ':', ' ', 'U', 'n', ' ', 'a', 'p',
                    'o', 'y', 'o', ' ', 't', 'e', 'r', 'r', 'e', 's', 't', 'r', 'e', ' ', 'e', 's', ' ', 'b', 'u', 'e',
                    'n', 'o', ' ', 'c', 'u', 'a', 'n', 'd', 'o', ' ', 'l', 'a', ' ', 's', 'i', 't', 'u', 'a', 'c', 'i',
                    'o', 'n', ' ', 's', 'e',' ', 'c', 'o', 'm', 'p', 'l', 'i', 'c', 'a','.']
cinematicadialogo5 = ['E', 's', 'e', ' ', 'd', 'í', 'a', ' ', 'm', 'a', 'r', 'c', 'ó', ' ', 'u', 'n', ' ', 'a', 'n', 't', 'e', 's',
                    ' ', 'y', ' ', 'u', 'n', ' ', 'd', 'e', 's', 'p', 'u', 'é', 's', ' ', 'e', 'n', ' ', 'e', 's', 't', 'a', ' ',
                    'l', 'a', 'r', 'g', 'a', ' ', 'g', 'u', 'e', 'r', 'r', 'a', '.', ' ', 'A', 'd', 'e', 'm', 'a', 's', ',',
                    ' ', 'l', 'o', 'g', 'r', 'a', 'm', 'o', 's', ' ', 'v', 'e', 'n', 'g', 'a', 'r', ' ', 'a', ' ', 'n', 'u', 'e', 's', 't', 'r', 'o', ' ',
                    'c', 'o', 'm', 'a', 'n', 'd', 'a', 'n', 't', 'e', '.', '.', '.', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
cinematicadialogo6 = ['C', 'o', 'n', ' ', 'e', 's', 't', 'e', ' ', 'l', 'o', 'g', 'r', 'o', ' ', 'e', 's', 't', 'a', 'm', 'o', 's',' ',
                    'c', 'a', 'd', 'a', ' ', 'v', 'e', 'z', ' ', 'm', 'á', 's', ' ', 'c', 'e', 'r', 'c', 'a', ' ', 'd', 'e',
                    ' ', 'l', 'a', ' ', 'p', 'a', 'z', ' ', 'e', 'n', ' ', 'e', 'l', ' ', 's', 'i', 's', 't', 'e', 'm', 'a',
                    ' ', 's', 'o', 'l', 'a', 'r', '.', ' ', ' ', ' ', '!', 'L', 'a', ' ', 'v', 'i', 'c', 't', 'o', 'r', 'a',
                    ' ', 's', 'e', 'r', 'á', ' ', 'n', 'u', 'e', 's', 't', 'r', 'a', '!', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
cinematicadialogo7 = ['B', 'a', 'j', 'a', 's', ' ', 't', 'e', 'r', 'r', 'o', 'r', 'i', 's', 't', 'a', 's', ' ', 't', 'o',
                    't', 'a', 'l', 'e', 's', ':', ' ', '5', '7', '6', '3', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
sb = 0
by = 200
slc = 0
spritetorrecontrol = 0
jugadorx = 25
jugadory = 360
jugadormovx,jugadormovx1 = 0,0
jugadormovy,jugadormovy1 = 0,0
spritejugador = 0
spritemunicionbomba = 10
bombas = spritemunicionbomba
bombax = []
bombay = []
bombaestado = []
spritebomba = []
cbombas = 0
for i in range(0, bombas):
    bombax.append(0)
    bombay.append(0)
    bombaestado.append("listo")
    spritebomba.append(0)

misilx = []
misily = []
misilsprite = 0
misilestado = []
misiles = 20
cmisiles = 0
recargandomisil = "no"
recargandobomba = "no"
spriterecargamisil = 0
spritemunicionmisil = misiles
spriterecargabomba = 0
destruccion = 0

spritetorrecontrol = 0
dialogo1estado = True
dialogo2estado = False
dialogo3estado = False
dialogo4estado = False
dialogo5estado = False
dialogo6estado = False
dialogo7estado = False
dialogo8estado = False
dialogo9estado = False
dialogo10estado = False
dialogo1 = ['', '', '', '', '!', 'J', 'e', 'f', 'e', '!', ' ' 'N', 'u', 'e', 's', 't', 'r', 'a', ' ', 'm', 'i',
            's', 'i', 'o', 'n', ' ', 'e', 's', ' ', 'd', 'e', 's', 't', 'r', 'u', 'i', 'r', ' ', 'e', 's', 't', 'a',
            ' ', 'c', 'i',
            'u', 'd', 'a', 'd', '', ' ', 'l', 'l', 'e', 'n', 'a', ' ', 'd', 'e', ' ', 'm', 'i', 'e', 'm', 'b', 'r', 'o',
            's', ' ', 'd', 'e', ' ', 'l', 'a'
    , ' ', 'F', '.', 'A', '.', 'R', '.', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dialogo2 = ['H', 'e', 'm', 'o', 's', ' ', 'i', 'n', 's', 't', 'a', 'l', 'a', 'd', 'o', ' ', 'u', 'n', 'a', ' ', 'b',
            'o',
            'm', 'b', 'a', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't', 'a', ' ', 'p', 'a', 'r', 'a', ' ', 'e', 'l', '', '',
            '', '', '', '', '', '', '', '', '', '', '', '', '', '', 't', 'r', 'a', 'b', 'a', 'j', 'o', ' ', '[', 'E',
            ']', '', '', '', '',
            '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dialogo3 = ['!', 'E', 's', ' ', 'h', 'o', 'r', 'a', ' ', 'd',
            'e', ' ', 'v', 'e', 'n', 'g', 'a', 'r', ' ', 'a', 'l', ' ','p', 'a', 'd', 'r', 'e', ' ', 'd', 'e', 'l', ' ', 'm', 'a', 'y', 'o', 'r', ' ', 'R', 'i', 'u',
            'b', 'e', '!', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'D', 'e', 's', 't',
            'r', 'u', 'y', 'e', ' ', 'e', 'l', ' ', 'p', 'u', 'e', 'b', 'l', 'o', '[', 'E', ']', '', '', '', '', '', '', '', '', '',
            '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dialogo4 = ['!', 'A', 's', 'í', ' ', 'e', 's', ' ', 'c', 'o', 'm', 'o', ' ', 's', 'e', ' ', 'g', 'a', 'n', 'a', ' ',
            'l', 'a',
            ' ', 'g', 'u', 'e', 'r', 'r', 'a', '!', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
            '', '', '', '', '', '', '!', 'G', 'r', 'a', 'n', ' ', 't', 'r', 'a', 'b', 'a', 'j', 'o', '!', '', '', '',
            '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dialogo5 = ['.', ' ', '.', ' ', '.', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
            '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dialogo6 = ['!', 'J', 'e', 'f', 'e', '!', ' ', 'T', 'e', 'n', ' ', 'c', 'u', 'i', 'd', 'a', 'd', 'o', '!', ' ', 'M',
            'e', ' ', 'i', 'n', 'f', 'o', 'r', 'm', 'a', 'n', ' ', 'q', 'u', 'e', ' ',
            'u', 'n', 'a', ' ', 'd', 'e', ' ', 'l', 'a', 's', '', '', '', '', 'c', 'r', 'i', 'a', 't', 'u', 'r', 'a',
            's', ' ', 'h', 'a', ' ' 'e', 's', 'c', 'a', 'p', 'a', 'd', 'o', '', '', '', '', '', '', '', '', '', '', '',
            '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dialogo7 = ['!', 'H', 'a', 'y', ' ', 'q', 'u', 'e', ' ', 's', 'a', 'l', 'i', 'r', ' ', 'd', 'e', ' ', 'a', 'q', 'u',
            'i', '!', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dialogo8 = ['L', 'a', ' ', 'c', 'r', 'i', 'a', 't', 'u', 'r', 'a', ' ', 's', 'e', ' ', 'a', 'c', 'e', 'r', 'c', 'a',
            ' ', 'r', 'a', 'p', 'i', 'd', 'a', 'm', 'e', 'n', 't', 'e', '', '', '', '', '', '', '', '', '', '', '', '',
            '', '', '', '', '', '', '', '', '', '', '', '',
            '!', 'H', 'a', 'y', ' ', 'q', 'u', 'e', ' ', 'd', 'e', 's', 't', 'r', 'u', 'i', 'r', 'l', 'a', '!', '', '',
            '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dialogo9 = ['T', 'e', 'n', 'e', 'm', 'o', 's', ' ', 'a', 'y', 'u', 'd', 'a', ' ', 't', 'e', 'r', 'r', 'e', 's', 't',
            'r', 'e', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
            '', '', '', '', '', '','!', 'L', 'a', 'n', 'z', 'a', ' ', 'c', 'o', 'h', 'e', 't', 'e', 's', ' ', 'l', 'i',
            's', 't', 'o', ' ', 'p', 'a', 'r', 'a', ' ', 'a', 't', 'a', 'c', 'a', 'r', '!', ' ', '[', 'E', ']', '', '',
            '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dialogo10 = ['!', 'A', 's', 'í', ' ', 's', 'e', ' ', 'h', 'a', 'c', 'e', '!', ' ', 'H', 'o', 'r', 'a', ' ', 'd', 'e',
            ' ', 'v', 'o', 'l', 'v', 'e', 'r', '', 'a', ' ', 'c', 'a', 's', 'a', '!', '', '', '', '', '', '', '', '',
            '', '', '', '', '', '', '', '', '', '',
            '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
nenemigos1 = 3
nenemigos2 = 3
helicopterox = []
helicopteroy = []
helicopteromovy = []
helicopteromovx = []
spritehelicoptero = 0
helicopteroestado = []
cdaño = []
vidahelicoptero = 3
spriteexplosion = 0
misilhelicopterox = []
misilhelicopteroy = []
spritemisilhelicoptero = 0
misilhelicopteroestado = []
misilhelicopteromovx = 20

for i in range(0, nenemigos2):
    helicopterox.append(random.randint(1280, 1599))
    helicopteroy.append(random.randint(0, 550))
    helicopteromovy.append(0)  # random.randint(2, 5)
    helicopteromovx.append(0)  # -random.randint(2, 5)
    helicopteroestado.append(True)
    cdaño.append(0)
    misilhelicopterox.append(0)
    misilhelicopteroy.append(0)
    misilhelicopteroestado.append("listo")

    cambiodiestado = []
cambioidestado = []
tanquedireccion = []
spritemisiltanque = 0
spritetanque = []
spritecambio = []
tanquex = []
tanquey = 570
tanquemovx = []
tanqueestado = []
tanquemisilx = []
tanquemisily = []
tanquemisilmovx = []
tanquemisilmovy = []
tanquemisilestado = []
tanquemisila = []
for i in range(0, nenemigos1):
    tanqueestado.append(True)
    tanquex.append(random.randint(1280, 1599))
    tanquemovx.append(0)
    tanquemisilestado.append("listo")
    tanquemisilx.append(0)
    tanquemisily.append(720)
    cambiodiestado.append(False)
    cambioidestado.append(False)
    tanquedireccion.append("")
    spritecambio.append(0)
    tanquemisilmovx.append(0)
    tanquemisilmovy.append(0)
    spritetanque.append(0)
    tanquemisila.append(False)
    spritejefebomba = 0
spritejefe = 0
jefex = 1500
jefey = 50
jefemovx = 0
jefeestado = False
jefevida = 1
jefeataque = False
jefedaño = False
funcionjefebomba = 0
funcionjefebombap = 0
funcionjefebombaestado = False
jefebombax = jefex + 150
jefebombay = jefey + 213
jefebombamovx = random.randint(7, 12)
jefebombaestado = "listo"
dañoa = 0
dañoabomba = 0
jefebombacolision = False
casax11 = [165, 275, 385, 680, 860, 965, 1140, 1245, 1330, 1488, 1605, 1737, 2058, 2177, 2288]
casax12 = [274, 384, 505, 826, 951, 1075, 1231, 1315, 1422, 1598, 1702, 1883, 2176, 2286, 2396]
casax11a = [165, 275, 385, 680, 860, 965, 1140, 1245, 1330, 1488, 1605, 1737, 2058, 2177, 2288]
casax12a = [274, 384, 505, 826, 951, 1075, 1231, 1315, 1422, 1598, 1702, 1883, 2176, 2286, 2396]
casax21 = []
casax22 = []
casax21a = []
casax22a = []
fuegoestado = []
spritefuego = []
for i in range(0, 15):
    fuegoestado.append(False)
    spritefuego.append(0)
    casax21.append(casax11[i] + 2560)
    casax22.append(casax12[i] + 2560)
    casax21a.append(casax11[i] + 2560)
    casax22a.append(casax12[i] + 2560)
info = open("Guardado.txt", "r")
text=info.readline().replace("\n","")
info.close()
info=open(text+".txt","r")
nombre = str(info.readline()).replace("\n","")
puntaje = int(info.readline().replace("\n",""))
info.close()
texto = pygame.font.Font('Nivel 2/freesansbold.ttf', 32)
nombreimg = texto.render(nombre, True, (255, 255, 255))
jugadorestado = True
muerte = False
ganaste = False
spritemuerte = 0
corazones = 6
corazonx = []
corazony = []
corazonestado = []
spritecorazon = 0
spritegameover = 0
spriteganaste = 0
for i in range(0, corazones):
    corazonx.append(random.randint(1280, 3500))
    corazony.append(random.randint(0, 400))
    corazonestado.append(False)
spritemisillanzamisiles = []
misillanzamisilesx = []
misillanzamisilesmovx = []
misillanzamisilesy = []
misillanzamisilesestado = []
misillanzamisilesfuncion = []
misillanzamisilesp = []
spritelanzamisiles = 0
lanzamisilesx = -80
lanzamisilesy = 525
lanzamisilesestado = "listo"
misileslanzamisiles = 10
for i in range(0, misileslanzamisiles):
    misillanzamisilesestado.append("listo")
    misillanzamisilesx.append(random.randint(-45, 30))
    misillanzamisilesmovx.append(random.randint(10, 30))
    misillanzamisilesy.append(0)
    spritemisillanzamisiles.append(0)
    misillanzamisilesfuncion.append(0)
    misillanzamisilesp.append(0)
misillanzamisilesestado[0] = "listo"
spritevida = 0
################################################################################################################
################################################################################################################
################################################################################################################
def niv_2():
    global nombre
    global puntaje
    global text
    info = open("Guardado.txt", "r")
    text=info.readline().replace("\n","")
    info.close()
    info=open(text+".txt","r")
    nombre = str(info.readline()).replace("\n","")
    puntaje = int(info.readline().replace("\n",""))
    nvl=int(info.readline().replace("\n",""))
    scorei=int(info.readline().replace("\n",""))
    info.close()
    global spriterecargamisil
    global spritemunicionmisil
    global misilestado
    global recargandomisil
    global bombas
    global spritebomba
    global bombax
    global bombay
    global jefeestado
    global recargandobomba
    global jefevida
    global jefex
    global jefey
    global jefedaño
    global dañoa
    global jefemovx
    global tanquex
    global tanquey
    global nenemigos1
    global bombaestado
    global tanqueestado
    global spritetanque
    global casax11
    global casax12
    global casax21
    global casax22
    global fuegoestado
    global spritefuego
    global destruccion
    global lanzamisilesestado
    global lanzamisilesx
    global lanzamisilesy
    global spritelanzamisiles
    global misillanzamisilesx
    global misillanzamisilesmovx
    global misillanzamisilesy
    global misillanzamisilesfuncion
    global misillanzamisilesestado
    global spritemisillanzamisiles
    global misillanzamisilesp
    global misileslanzamisiles
    global recargandobomba
    global jefeataque
    global spriterecargabomba
    global spritemunicionbomba
    global spritejefe
    global jefebombax
    global jefebombay
    global recargandomisil
    global recargandobomba
    global spriterecargamisil
    global cmisiles
    global cbombas
    global bombas
    global misiles
    global muerte
    global spritevida
    global jugadorestado
    global texto
    global destruccion
    global dialogo1estado
    global dialogo2estado
    global dialogo3estado
    global dialogo4estado 
    global dialogo5estado 
    global dialogo6estado
    global dialogo7estado 
    global dialogo8estado
    global dialogo9estado
    global dialogo10estado
    global jefeestado
    global jugadorx
    global jugadory
    global fase2
    global fase3
    global jugadormovx
    global jugadormovy
    global jugadormovx1
    global jugadormovy1
    global contadordialogo
    global spritebomba
    global vidahelicoptero
    global contadorcinematica
    global ganaste
    global spriteganaste

    pygame.font.init()
    screen = pygame.display.set_mode((1280,720))
    screen.fill((0, 0, 0))
    pygame.display.set_caption("Shut 'em all")
    Icono = pygame.image.load('Imagenes/Icono.png')
    pygame.display.set_icon(Icono)
    fuentedialogo = pygame.font.Font('Nivel 2/Open 24 Display St.ttf', 24)

    mixer.init()
    mixer.set_num_channels(24)
    canal0 = mixer.Channel(0)
    canal1 = mixer.Channel(1)
    canal2 = mixer.Channel(2)
    canal3 = mixer.Channel(3)
    canal4 = mixer.Channel(4)
    canal5 = mixer.Channel(5)
    canal6 = mixer.Channel(6)
    canal7 = mixer.Channel(7)
    canal8 = mixer.Channel(8)
    canal9 = mixer.Channel(9)
    canal10 = mixer.Channel(10)
    canal11 = mixer.Channel(11)
    canal12 = mixer.Channel(12)
    canal13 = mixer.Channel(13)
    canal14 = mixer.Channel(14)
    canal15 = mixer.Channel(15)
    canal16 = mixer.Channel(16)
    canal17 = mixer.Channel(17)
    canal18 = mixer.Channel(18) 
    canal19 = mixer.Channel(19)
    canal20 = mixer.Channel(20)
    canal21 = mixer.Channel(21)
    canalpausa=mixer.Channel(22)
    fuegosonido = mixer.Sound("Nivel 2/Sonidos/Fuego.wav")
    helicopterosonido = mixer.Sound("Nivel 2/Sonidos/Helicoptero.wav")
    bombasonido = mixer.Sound("Nivel 2/Sonidos/Bomba.wav")
    balasonido = mixer.Sound("Nivel 2/Sonidos/Bala.wav")
    recargasonido = mixer.Sound("Nivel 2/Sonidos/Recarga.wav")
    explosionsonido = mixer.Sound("Nivel 2/Sonidos/Explosion.wav")
    hitsonido = mixer.Sound("Nivel 2/Sonidos/Hit.wav")
    recarga2sonido = mixer.Sound("Nivel 2/Sonidos/Recarga2.wav")
    misiltanquesonido = mixer.Sound("Nivel 2/Sonidos/MisilTanque.wav")
    repararsonido = mixer.Sound("Nivel 2/Sonidos/Reparar.wav")
    dañosonido = mixer.Sound("Nivel 2/Sonidos/Daño.wav")
    bombajefeexplosionsonido = mixer.Sound("Nivel 2/Sonidos/BombaExplosionJefe.wav")
    bombaexplosionsonido = mixer.Sound("Nivel 2/Sonidos/BombaExplosion.wav")
    muertesonido = mixer.Sound("Nivel 2/Sonidos/Muerte.wav")
    escribiendosonido = mixer.Sound("Nivel 2/Sonidos/Escribiendo.wav")
    explosionjefesonido = mixer.Sound("Nivel 2/Sonidos/ExplosionJefe.wav")
    fondo2sonido = mixer.Sound("Nivel 2/Sonidos/Fondo2.wav")
    superataquesonido = mixer.Sound("Nivel 2/Sonidos/SuperAtaque.wav")
    cinematicasonido = mixer.Sound("Nivel 2/Sonidos/Cinematica.wav")
    Spausa=mixer.Sound("Sonidos\\SpacyLoop.ogg")
    # Introduccion
    cinematicaimg = [pygame.image.load("Nivel 2/Introduccion/1.png"), pygame.image.load("Nivel 2/Introduccion/2.png"),
                    pygame.image.load("Nivel 2/Introduccion/3.png"), pygame.image.load("Nivel 2/Introduccion/4.png"),
                    pygame.image.load("Nivel 2/Introduccion/5.png"), pygame.image.load("Nivel 2/Introduccion/6.png"),
                    pygame.image.load("Nivel 2/Introduccion/7.png"), pygame.image.load("Nivel 2/Introduccion/8.png"),
                    pygame.image.load("Nivel 2/Introduccion/9.png"), pygame.image.load("Nivel 2/Introduccion/10.png"),
                    pygame.image.load("Nivel 2/Introduccion/11.png"), pygame.image.load("Nivel 2/Introduccion/12.png"),
                    pygame.image.load("Nivel 2/Introduccion/13.png"), pygame.image.load("Nivel 2/Introduccion/14.png"),
                    pygame.image.load("Nivel 2/Introduccion/15.png"), pygame.image.load("Nivel 2/Introduccion/16.png")]

    def fade():
        global contadorcinematica

        fade = pygame.Surface((1280, 720))
        fade.fill((0, 0, 0))
        opacidad = 0
        for i in range(0, 51):
            opacidad += 5
            fade.set_alpha(opacidad)
            redraw()
            screen.blit(fade, (0, 0))
            pygame.time.delay(4)
            pygame.display.update()
        contadorcinematica += 1
        for i in range(0, 51):
            opacidad -= 5
            fade.set_alpha(opacidad)
            redraw()
            screen.blit(fade, (0, 0))
            pygame.time.delay(4)
            pygame.display.update()


    def cambioescena():
        global contadorcinematica

        opacidad1 = 0
        img = cinematicaimg[contadorcinematica+1]
        img = img.convert()
        img.set_alpha(opacidad1)
        for i in range(0, 51):
            opacidad1 += 5
            redraw()
            img.set_alpha(opacidad1)
            x = img.get_alpha()
            screen.blit(img, (0, 0))
            pygame.display.update()
            pygame.time.delay(4)
        contadorcinematica += 1


    def redraw():
        global contadorcinematica

        screen.blit(cinematicaimg[contadorcinematica], (0, 0))


    def cinematica():
        global spritejugador
        global contadorcinematica
        global jugadorx
        global sb
        global by
        global slc
        global cinematicadialogo4estado
        screen.blit(cinematicaimg[contadorcinematica], (0, 0))
        if contadorcinematica == 8:
            jugadorx += 3
            screen.blit(jugadorimg[spritejugador], (jugadorx, 350))
            if jugadorx >= 1000:
                jugadorx = 25
                fade()
                cinematicadialogo4estado = True
                spritejugador = 0
            if spritejugador >= 59:
                spritejugador = 0
            else:
                spritejugador += 1
        if contadorcinematica == 9:
            screen.blit(jugadorimg[spritejugador], (400, 200))
            if sb <= 6:
                screen.blit(especialimg[int(sb)], (400, by + 20))
                sb += 0.25
            else:
                if by < 450:
                    screen.blit(especialimg[int(sb)], (400, by + 20))
                    by += 10
            if by >= 450:
                if sb >= 30:
                    sb = 0
                    by = 200
                else:
                    screen.blit(especialimg[int(sb+1)], (400 - 40, by - 60))
                    sb += 0.5

            screen.blit(jugadorimg[spritejugador], (800, 200))
            screen.blit(lanzamisilesimg[int(slc)], (800, 400))
            if slc >= 19:
                slc = 0
            else:
                slc += 0.25

            if spritejugador >= 59:
                spritejugador = 0
            else:
                spritejugador += 1


    def cinematicadialogo():
        global cinematicadialogo1
        global cinematicadialogo2
        global cinematicadialogo3
        global cinematicadialogo4
        global cinematicadialogo5
        global cinematicadialogo6
        global cinematicadialogo7
        global cinematicadialogo1estado
        global cinematicadialogo2estado
        global cinematicadialogo3estado
        global cinematicadialogo4estado
        global cinematicadialogo5estado
        global cinematicadialogo6estado
        global cinematicadialogo7estado
        global contadordialogo
        global linea1
        global linea2
        global linea1img
        global linea2img

        if cinematicadialogo1estado:
            if contadordialogo < len(cinematicadialogo1):
                linea1img = fuentedialogo.render(linea1, True, (255, 255, 255))
                screen.blit(linea1img, (25, 625))
                linea2img = fuentedialogo.render(linea2, True, (255, 255, 255))
                screen.blit(linea2img, (25, 675))
                if contadordialogo <= 130:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea1 += cinematicadialogo1[int(contadordialogo)]

                if contadordialogo > 130:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea2 += cinematicadialogo1[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                fade()
                cinematicadialogo1estado = False
                cinematicadialogo2estado = True
                contadordialogo = 0
                linea1 = ''
                linea2 = ''

        if cinematicadialogo2estado:
            if contadordialogo < len(cinematicadialogo2):
                linea1img = fuentedialogo.render(linea1, True, (255, 255, 255))
                screen.blit(linea1img, (25, 625))
                linea2img = fuentedialogo.render(linea2, True, (255, 255, 255))
                screen.blit(linea2img, (25, 675))
                if contadordialogo <= 130:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea1 += cinematicadialogo2[int(contadordialogo)]

                if contadordialogo > 130:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea2 += cinematicadialogo2[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                fade()
                cambioescena()
                cambioescena()
                cambioescena()
                cinematicadialogo2estado = False
                cinematicadialogo3estado = True
                contadordialogo = 0
                linea1 = ''
                linea2 = ''

        if cinematicadialogo3estado:
            if contadordialogo < len(cinematicadialogo3):
                linea1img = fuentedialogo.render(linea1, True, (255, 255, 255))
                screen.blit(linea1img, (25, 625))
                linea2img = fuentedialogo.render(linea2, True, (255, 255, 255))
                screen.blit(linea2img, (25, 675))
                if contadordialogo <= 130:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea1 += cinematicadialogo3[int(contadordialogo)]

                if contadordialogo > 130:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea2 += cinematicadialogo3[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                cambioescena()
                cambioescena()
                fade()
                cinematicadialogo3estado = False
                contadordialogo = 0
                linea1 = ''
                linea2 = ''

        if cinematicadialogo4estado:
            if contadordialogo < len(cinematicadialogo4):
                linea1img = fuentedialogo.render(linea1, True, (255, 255, 255))
                screen.blit(linea1img, (25, 625))
                linea2img = fuentedialogo.render(linea2, True, (255, 255, 255))
                screen.blit(linea2img, (25, 675))
                if contadordialogo <= 130:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea1 += cinematicadialogo4[int(contadordialogo)]

                if contadordialogo > 130:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea2 += cinematicadialogo4[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                screen.blit(linea1img, (25, 625))
                screen.blit(linea2img, (25, 675))
                screen.blit(omitirimg, (350, 350))

        if cinematicadialogo5estado:
            if contadordialogo < len(cinematicadialogo5):
                linea1img = fuentedialogo.render(linea1, True, (255, 255, 255))
                screen.blit(linea1img, (25, 625))
                linea2img = fuentedialogo.render(linea2, True, (255, 255, 255))
                screen.blit(linea2img, (25, 675))
                if contadordialogo <= 130:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea1 += cinematicadialogo5[int(contadordialogo)]

                if contadordialogo > 130:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea2 += cinematicadialogo5[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                cinematicadialogo5estado = False
                cambioescena()
                pygame.time.delay(1600)
                cambioescena()
                pygame.time.delay(1600)
                cambioescena()
                cinematicadialogo6estado = True
                contadordialogo = 0
                linea1 = ''
                linea2 = ''

        if cinematicadialogo6estado:
            if contadordialogo < len(cinematicadialogo6):
                linea1img = fuentedialogo.render(linea1, True, (255, 255, 255))
                screen.blit(linea1img, (25, 625))
                linea2img = fuentedialogo.render(linea2, True, (255, 255, 255))
                screen.blit(linea2img, (25, 675))
                if contadordialogo <= 130:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea1 += cinematicadialogo6[int(contadordialogo)]

                if contadordialogo > 130:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea2 += cinematicadialogo6[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                fade()
                cinematicadialogo6estado = False
                cinematicadialogo7estado = True
                contadordialogo = 0
                linea1 = ''
                linea2 = ''


        if cinematicadialogo7estado:
            if contadordialogo < len(cinematicadialogo7):
                linea1img = fuentedialogo.render(linea1, True, (255, 255, 255))
                screen.blit(linea1img, (25, 625))
                linea2img = fuentedialogo.render(linea2, True, (255, 255, 255))
                screen.blit(linea2img, (25, 675))
                if contadordialogo <= 130:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea1 += cinematicadialogo7[int(contadordialogo)]

                if contadordialogo > 130:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea2 += cinematicadialogo7[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                screen.blit(linea1img, (25, 625))
                screen.blit(linea2img, (25, 675))


    fondo1 = pygame.image.load("Nivel 2/fondo.png")
    global fondo1x
    global fondo2x
    barraestado = pygame.image.load("Nivel 2/barraestado.png")
    municionmisilimg = [pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/1.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/2.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/3.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/4.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/5.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/6.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/7.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/8.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/9.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/10.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/11.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/12.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/13.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/14.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/15.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/16.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/17.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/18.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/19.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/20.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Misil/Municion/21.png").convert_alpha()
                        ]
    municionbombaimg = [pygame.image.load("Nivel 2/NaveSprite/Bomba/Municion/1.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Bomba/Municion/2.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Bomba/Municion/3.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Bomba/Municion/4.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Bomba/Municion/5.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Bomba/Municion/6.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Bomba/Municion/7.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Bomba/Municion/8.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Bomba/Municion/9.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Bomba/Municion/10.png").convert_alpha(),
                        pygame.image.load("Nivel 2/NaveSprite/Bomba/Municion/11.png").convert_alpha()]
    recargamisilimg = [pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/1.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/2.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/3.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/4.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/5.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/6.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/7.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/8.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/9.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/10.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/11.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/12.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/13.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/14.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/15.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/16.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/17.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/18.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/19.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/20.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/21.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/22.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Misil/Recarga/23.png").convert_alpha()]
    recargabombaimg = [pygame.image.load("Nivel 2/NaveSprite/Bomba/Recarga/1.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Bomba/Recarga/2.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Bomba/Recarga/3.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Bomba/Recarga/4.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Bomba/Recarga/5.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Bomba/Recarga/6.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Bomba/Recarga/7.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Bomba/Recarga/8.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Bomba/Recarga/9.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Bomba/Recarga/10.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Bomba/Recarga/11.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Bomba/Recarga/12.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Bomba/Recarga/13.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Bomba/Recarga/14.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Bomba/Recarga/15.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Bomba/Recarga/16.png").convert_alpha(),
                    pygame.image.load("Nivel 2/NaveSprite/Bomba/Recarga/17.png").convert_alpha()]
    corazonimg = [pygame.image.load("Nivel 2/Corazon/1.png").convert_alpha(), pygame.image.load("Nivel 2/Corazon/2.png").convert_alpha(),
                pygame.image.load("Nivel 2/Corazon/3.png").convert_alpha(), pygame.image.load("Nivel 2/Corazon/4.png").convert_alpha(),
                pygame.image.load("Nivel 2/Corazon/5.png").convert_alpha(), pygame.image.load("Nivel 2/Corazon/6.png").convert_alpha(),
                pygame.image.load("Nivel 2/Corazon/7.png").convert_alpha(), pygame.image.load("Nivel 2/Corazon/8.png").convert_alpha()]
    gameoverimg = [pygame.image.load("Nivel 2/Muerte/1.png").convert_alpha(), pygame.image.load("Nivel 2/Muerte/2.png").convert_alpha(),
                pygame.image.load("Nivel 2/Muerte/3.png").convert_alpha(), pygame.image.load("Nivel 2/Muerte/4.png").convert_alpha(),
                pygame.image.load("Nivel 2/Muerte/5.png").convert_alpha(), pygame.image.load("Nivel 2/Muerte/6.png").convert_alpha(),
                pygame.image.load("Nivel 2/Muerte/7.png").convert_alpha(), pygame.image.load("Nivel 2/Muerte/8.png").convert_alpha(),
                pygame.image.load("Nivel 2/Muerte/9.png").convert_alpha(), pygame.image.load("Nivel 2/Muerte/10.png").convert_alpha(),
                pygame.image.load("Nivel 2/Muerte/11.png").convert_alpha()]
    ganasteimg = [pygame.image.load("Nivel 2/Ganaste/1.png").convert_alpha(), pygame.image.load("Nivel 2/Ganaste/2.png").convert_alpha(),
                pygame.image.load("Nivel 2/Ganaste/3.png").convert_alpha(), pygame.image.load("Nivel 2/Ganaste/4.png").convert_alpha(),
                pygame.image.load("Nivel 2/Ganaste/5.png").convert_alpha(), pygame.image.load("Nivel 2/Ganaste/6.png").convert_alpha(),
                pygame.image.load("Nivel 2/Ganaste/7.png").convert_alpha(), pygame.image.load("Nivel 2/Ganaste/8.png").convert_alpha(),
                pygame.image.load("Nivel 2/Ganaste/9.png").convert_alpha(), pygame.image.load("Nivel 2/Ganaste/10.png").convert_alpha(),
                pygame.image.load("Nivel 2/Ganaste/11.png").convert_alpha()]
    muerteimg = [pygame.image.load("Nivel 2/NaveSprite/Muerte/1.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Muerte/2.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Muerte/3.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Muerte/4.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Muerte/5.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Muerte/6.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Muerte/7.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Muerte/8.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Muerte/9.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Muerte/10.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Muerte/11.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Muerte/12.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Muerte/13.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Muerte/14.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Muerte/15.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Muerte/16.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Muerte/17.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Muerte/18.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Muerte/19.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Muerte/20.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Muerte/21.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Muerte/22.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Muerte/23.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Muerte/24.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Muerte/25.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Muerte/26.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Muerte/27.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Muerte/28.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Muerte/29.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Muerte/30.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Muerte/31.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Muerte/32.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Muerte/33.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Muerte/34.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Muerte/35.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Muerte/36.png").convert_alpha()]

    # jugador
    jugadorimg = [pygame.image.load("Nivel 2/NaveSprite/1.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/2.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/3.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/4.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/5.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/6.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/7.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/8.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/9.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/10.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/11.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/12.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/13.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/14.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/15.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/16.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/17.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/18.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/19.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/20.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/21.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/22.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/23.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/24.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/25.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/26.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/27.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/28.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/29.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/30.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/31.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/32.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/33.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/34.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/35.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/36.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/37.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/38.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/39.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/40.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/41.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/42.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/43.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/44.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/45.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/46.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/47.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/48.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/49.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/50.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/51.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/52.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/53.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/54.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/55.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/56.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/57.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/58.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/59.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/60.png").convert_alpha(),
                ]
    especialimg = [pygame.image.load("Nivel 2/NaveSprite/Bomba/1.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Bomba/2.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Bomba/3.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Bomba/4.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Bomba/5.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Bomba/6.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Bomba/7.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Bomba/8.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Bomba/9.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Bomba/10.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Bomba/11.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Bomba/12.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Bomba/13.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Bomba/14.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Bomba/15.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Bomba/16.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Bomba/17.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Bomba/18.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Bomba/19.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Bomba/20.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Bomba/21.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Bomba/22.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Bomba/23.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Bomba/24.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Bomba/25.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Bomba/26.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Bomba/27.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Bomba/28.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Bomba/29.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Bomba/30.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Bomba/31.png").convert_alpha()]
    misilimg = [pygame.image.load("Nivel 2/NaveSprite/Misil/1.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Misil/2.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Misil/3.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Misil/4.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Misil/5.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Misil/6.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Misil/7.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Misil/8.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Misil/9.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Misil/10.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Misil/11.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Misil/12.png").convert_alpha(),
                pygame.image.load("Nivel 2/NaveSprite/Misil/13.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Misil/14.png").convert_alpha()]
    lanzamisilesimg = [pygame.image.load("Nivel 2/LanzaMisiles/1.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/2.png").convert_alpha(),
                    pygame.image.load("Nivel 2/LanzaMisiles/3.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/4.png").convert_alpha(),
                    pygame.image.load("Nivel 2/LanzaMisiles/5.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/6.png").convert_alpha(),
                    pygame.image.load("Nivel 2/LanzaMisiles/7.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/8.png").convert_alpha(),
                    pygame.image.load("Nivel 2/LanzaMisiles/9.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/10.png").convert_alpha(),
                    pygame.image.load("Nivel 2/LanzaMisiles/11.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/12.png").convert_alpha(),
                    pygame.image.load("Nivel 2/LanzaMisiles/13.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/14.png").convert_alpha(),
                    pygame.image.load("Nivel 2/LanzaMisiles/15.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/16.png").convert_alpha(),
                    pygame.image.load("Nivel 2/LanzaMisiles/17.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/18.png").convert_alpha(),
                    pygame.image.load("Nivel 2/LanzaMisiles/19.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/20.png").convert_alpha()]
    misillanzamisilesimg = [pygame.image.load("Nivel 2/LanzaMisiles/Misil/1.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/Misil/2.png").convert_alpha(),
                            pygame.image.load("Nivel 2/LanzaMisiles/Misil/3.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/Misil/4.png").convert_alpha(),
                            pygame.image.load("Nivel 2/LanzaMisiles/Misil/5.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/Misil/6.png").convert_alpha(),
                            pygame.image.load("Nivel 2/LanzaMisiles/Misil/7.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/Misil/8.png").convert_alpha(),
                            pygame.image.load("Nivel 2/LanzaMisiles/Misil/9.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/Misil/10.png").convert_alpha(),
                            pygame.image.load("Nivel 2/LanzaMisiles/Misil/11.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/Misil/12.png").convert_alpha(),
                            pygame.image.load("Nivel 2/LanzaMisiles/Misil/13.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/Misil/14.png").convert_alpha(),
                            pygame.image.load("Nivel 2/LanzaMisiles/Misil/15.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/Misil/16.png").convert_alpha(),
                            pygame.image.load("Nivel 2/LanzaMisiles/Misil/17.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/Misil/18.png").convert_alpha(),
                            pygame.image.load("Nivel 2/LanzaMisiles/Misil/19.png").convert_alpha(), pygame.image.load("Nivel 2/LanzaMisiles/Misil/20.png").convert_alpha()]
    vidaimg = [pygame.image.load("Nivel 2/NaveSprite/Vida/1.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Vida/2.png").convert_alpha(),
            pygame.image.load("Nivel 2/NaveSprite/Vida/3.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Vida/4.png").convert_alpha(),
            pygame.image.load("Nivel 2/NaveSprite/Vida/5.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Vida/6.png").convert_alpha(),
            pygame.image.load("Nivel 2/NaveSprite/Vida/7.png").convert_alpha(), pygame.image.load("Nivel 2/NaveSprite/Vida/8.png").convert_alpha()]
    torrecontrolimg = [pygame.image.load("Nivel 2/TorreControl/1.png").convert_alpha(), pygame.image.load("Nivel 2/TorreControl/2.png").convert_alpha(),
                    pygame.image.load("Nivel 2/TorreControl/3.png").convert_alpha(), pygame.image.load("Nivel 2/TorreControl/4.png").convert_alpha(),
                    pygame.image.load("Nivel 2/TorreControl/5.png").convert_alpha(), pygame.image.load("Nivel 2/TorreControl/6.png").convert_alpha(),
                    pygame.image.load("Nivel 2/TorreControl/7.png").convert_alpha(), pygame.image.load("Nivel 2/TorreControl/8.png").convert_alpha(),
                    pygame.image.load("Nivel 2/TorreControl/9.png").convert_alpha(), pygame.image.load("Nivel 2/TorreControl/10.png").convert_alpha()]
    omitir = "Pulsa ENTER para omitir o continuar"
    omitirimg = texto.render(omitir, True, (255, 255, 255))
    # dialogo torre control
    global linea1
    global linea2
    linea1img = fuentedialogo.render(linea1, True, (0, 255, 0))
    linea2img = fuentedialogo.render(linea2, True, (0, 255, 0))

    def fondo():
        global destruccion
        global fondo1x
        global fondo2x
        global cmisiles
        global spritegameover
        global jefeestado
        global nombreimg
        global fase3
        global ganaste
        global jugadorx
        global jugadorestado
        global spriteganaste
        global cbombas
        global casax11
        global casax12
        global casax21
        global casax22
        global fase3

        if not fase3:
            fondo1x -= 2
            fondo2x -= 2
            for i in range(0, 15):
                casax11[i] -= 2
                casax12[i] -= 2
                casax21[i] -= 2
                casax22[i] -= 2
            if fondo1x <= -2560:
                fondo1x = 2560
                for i in range(0, 15):
                    casax11[i] = casax21a[i]
                    casax12[i] = casax22a[i]

            if fondo2x <= -2560:
                fondo2x = 2560
                for i in range(0, 15):
                    casax21[i] = casax21a[i]
                    casax22[i] = casax22a[i]

        else:
            fondo1x += 2
            fondo2x += 2
            for i in range(0, 15):
                casax11[i] += 2
                casax12[i] += 2
                casax21[i] += 2
                casax22[i] += 2
            if fondo1x >= 2560:
                fondo1x = -2560
                for i in range(0, 15):
                    casax11[i] = -casax21a[i]
                    casax12[i] = -casax22a[i]

            if fondo2x >= 2560:
                fondo2x = -2560
                for i in range(0, 15):
                    casax21[i] = -casax21a[i]
                    casax22[i] = -casax22a[i]

        screen.blit(fondo1, (fondo1x, 0))
        screen.blit(fondo1, (fondo2x, 0))
        # Barra estado
        screen.blit(barraestado, (0, 648))
        if recargandomisil == "no":
            screen.blit(municionmisilimg[cmisiles], (25, 685))
        if recargandobomba == "no":
            screen.blit(municionbombaimg[cbombas], (250, 685))
        puntajeimg = texto.render("Puntaje: " + str(puntaje), True, (255, 255, 255))
        destruccionimg = texto.render("Destrucción: " + str(int(destruccion)) + "%", True, (255, 255, 255))
        screen.blit(puntajeimg, (380, 657))
        screen.blit(destruccionimg, (380, 690))
        screen.blit(vidaimg[spritevida], (25, 657))
        screen.blit(nombreimg, (25, 25))

        if ganaste:
            jugadorestado = False
            screen.blit(ganasteimg[int(spriteganaste)], (0, 0))
            screen.blit(puntajeimg, (450, 500))
            if spriteganaste < 10:
                spriteganaste += 0.5
            else:
                screen.blit(omitirimg, (350, 150))
                spriteganaste += 0
        elif not jugadorestado:
            screen.blit(gameoverimg[int(spritegameover)], (0, 0))
            screen.blit(puntajeimg, (450, 500))
            if spritegameover < 10:
                spritegameover += 0.5
            else:
                screen.blit(omitirimg, (350, 150))
                spritegameover += 0


    def dialogo():
        global linea1
        global linea2
        global dialogo1estado
        global dialogo2estado
        global dialogo3estado
        global dialogo4estado
        global dialogo5estado
        global dialogo6estado
        global dialogo7estado
        global dialogo8estado
        global dialogo9estado
        global dialogo10estado
        global linea1img
        global linea2img
        global contadordialogo
        global helicopteromovx
        global helicopteromovy
        global tanquemovx
        global nenemigos1
        global nenemigos2
        global spritetorrecontrol
        global escribiendosonidoestado
        global jefeestado
        global ganaste
        global jugadorestado
        global fase2
        global fase3

        if jugadorestado:
            screen.blit(torrecontrolimg[int(spritetorrecontrol)], (1150, 555))
        if 0 <= spritetorrecontrol <= 9:
            spritetorrecontrol += 0.25

        if escribiendosonidoestado == "escribiendo":
            canal19.play(escribiendosonido)
            escribiendosonidoestado = "nolisto"

        if dialogo1estado:
            if escribiendosonidoestado == "listo":
                escribiendosonidoestado = "escribiendo"
            if contadordialogo < len(dialogo1):
                screen.blit(omitirimg, (500, 250))
                linea1img = fuentedialogo.render(linea1, True, (0, 255, 0))
                screen.blit(linea1img, (675, 650))
                linea2img = fuentedialogo.render(linea2, True, (0, 255, 0))
                screen.blit(linea2img, (675, 675))
                if contadordialogo <= 49:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea1 += dialogo1[int(contadordialogo)]

                if contadordialogo > 49:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea2 += dialogo1[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                dialogo1estado = False
                dialogo2estado = True
                contadordialogo = 0
                linea1 = ''
                linea2 = ''
                escribiendosonidoestado = "listo"

        if dialogo2estado:
            if escribiendosonidoestado == "listo":
                escribiendosonidoestado = "escribiendo"
            if contadordialogo < len(dialogo2):
                linea1img = fuentedialogo.render(linea1, True, (0, 255, 0))
                screen.blit(linea1img, (675, 650))
                linea2img = fuentedialogo.render(linea2, True, (0, 255, 0))
                screen.blit(linea2img, (675, 675))
                if contadordialogo <= 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea1 += dialogo2[int(contadordialogo)]

                if contadordialogo > 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea2 += dialogo2[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                dialogo2estado = False
                dialogo3estado = True
                contadordialogo = 0
                linea1 = ''
                linea2 = ''
                escribiendosonidoestado = "listo"
                for i in range(0, nenemigos2):
                    helicopteromovy[i] = random.randint(-3, 3)
                    helicopteromovx[i] = random.randint(1, 2)
                for i in range(0, nenemigos1):
                    tanquemovx[i] = random.randint(1, 5)

        if dialogo3estado:
            if escribiendosonidoestado == "listo":
                escribiendosonidoestado = "escribiendo"
            if contadordialogo < len(dialogo3):
                linea1img = fuentedialogo.render(linea1, True, (0, 255, 0))
                screen.blit(linea1img, (675, 650))
                linea2img = fuentedialogo.render(linea2, True, (0, 255, 0))
                screen.blit(linea2img, (675, 675))
                if contadordialogo <= 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea1 += dialogo3[int(contadordialogo)]

                if contadordialogo > 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea2 += dialogo3[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                linea1img = fuentedialogo.render(linea1, True, (0, 255, 0))
                screen.blit(linea1img, (675, 650))
                linea2img = fuentedialogo.render(linea2, True, (0, 255, 0))
                screen.blit(linea2img, (675, 675))

        if dialogo4estado:
            if escribiendosonidoestado == "listo":
                escribiendosonidoestado = "escribiendo"
            if contadordialogo < len(dialogo4):
                linea1img = fuentedialogo.render(linea1, True, (0, 255, 0))
                screen.blit(linea1img, (675, 650))
                linea2img = fuentedialogo.render(linea2, True, (0, 255, 0))
                screen.blit(linea2img, (675, 675))
                if contadordialogo <= 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea1 += dialogo4[int(contadordialogo)]

                if contadordialogo > 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea2 += dialogo4[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                dialogo4estado = False
                dialogo5estado = True
                contadordialogo = 0
                linea1 = ''
                linea2 = ''
                escribiendosonidoestado = "listo"

        if dialogo5estado:
            if escribiendosonidoestado == "listo":
                escribiendosonidoestado = "escribiendo"
            if contadordialogo < len(dialogo5):
                linea1img = fuentedialogo.render(linea1, True, (0, 255, 0))
                screen.blit(linea1img, (675, 650))
                linea2img = fuentedialogo.render(linea2, True, (0, 255, 0))
                screen.blit(linea2img, (675, 675))
                if contadordialogo <= 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea1 += dialogo5[int(contadordialogo)]

                if contadordialogo > 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea2 += dialogo5[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                dialogo5estado = False
                dialogo6estado = True
                contadordialogo = 0
                linea1 = ''
                linea2 = ''
                escribiendosonidoestado = "listo"

        if dialogo6estado:
            if escribiendosonidoestado == "listo":
                escribiendosonidoestado = "escribiendo"
            if contadordialogo < len(dialogo6):
                linea1img = fuentedialogo.render(linea1, True, (0, 255, 0))
                screen.blit(linea1img, (675, 650))
                linea2img = fuentedialogo.render(linea2, True, (0, 255, 0))
                screen.blit(linea2img, (675, 675))
                if contadordialogo <= 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea1 += dialogo6[int(contadordialogo)]

                if contadordialogo > 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea2 += dialogo6[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                screen.blit(linea1img, (675, 650))
                screen.blit(linea2img, (675, 675))
                dialogo6estado = False
                dialogo7estado = True
                contadordialogo = 0
                linea1 = ''
                linea2 = ''
                escribiendosonidoestado = "listo"

        if dialogo7estado:
            if escribiendosonidoestado == "listo":
                escribiendosonidoestado = "escribiendo"
            if contadordialogo < len(dialogo7):
                linea1img = fuentedialogo.render(linea1, True, (0, 255, 0))
                screen.blit(linea1img, (675, 650))
                linea2img = fuentedialogo.render(linea2, True, (0, 255, 0))
                screen.blit(linea2img, (675, 675))
                if contadordialogo <= 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea1 += dialogo7[int(contadordialogo)]

                if contadordialogo > 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea2 += dialogo7[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                dialogo7estado = False
                dialogo8estado = True
                contadordialogo = 0
                linea1 = ''
                linea2 = ''
                escribiendosonidoestado = "listo"
                if not fase3:
                    canal21.play(fondo2sonido, loops=-1)
                    fase3 = True

        if dialogo8estado:
            if escribiendosonidoestado == "listo":
                escribiendosonidoestado = "escribiendo"
            if contadordialogo < len(dialogo8):
                linea1img = fuentedialogo.render(linea1, True, (0, 255, 0))
                screen.blit(linea1img, (675, 650))
                linea2img = fuentedialogo.render(linea2, True, (0, 255, 0))
                screen.blit(linea2img, (675, 675))
                if contadordialogo <= 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea1 += dialogo8[int(contadordialogo)]

                if contadordialogo > 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea2 += dialogo8[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                dialogo8estado = False
                dialogo9estado = True
                contadordialogo = 0
                linea1 = ''
                linea2 = ''
                escribiendosonidoestado = "listo"
                if not jefeestado:
                    jefeestado = True

        if dialogo9estado:
            if escribiendosonidoestado == "listo":
                escribiendosonidoestado = "escribiendo"
            if contadordialogo < len(dialogo9):
                linea1img = fuentedialogo.render(linea1, True, (0, 255, 0))
                screen.blit(linea1img, (675, 650))
                linea2img = fuentedialogo.render(linea2, True, (0, 255, 0))
                screen.blit(linea2img, (675, 675))
                if contadordialogo <= 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea1 += dialogo9[int(contadordialogo)]

                if contadordialogo > 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea2 += dialogo9[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                dialogo9estado = False
                contadordialogo = 0
                linea1 = ''
                linea2 = ''
                escribiendosonidoestado = "listo"

        if dialogo10estado:
            if escribiendosonidoestado == "listo":
                escribiendosonidoestado = "escribiendo"
            if contadordialogo < len(dialogo10):
                linea1img = fuentedialogo.render(linea1, True, (0, 255, 0))
                screen.blit(linea1img, (675, 650))
                linea2img = fuentedialogo.render(linea2, True, (0, 255, 0))
                screen.blit(linea2img, (675, 675))
                if contadordialogo <= 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea1 += dialogo10[int(contadordialogo)]

                if contadordialogo > 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea2 += dialogo10[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                dialogo10estado = False
                ganaste = True
                contadordialogo = 0
                linea1 = ''
                linea2 = ''
                escribiendosonidoestado = "listo"


    for i in range(0, misiles):
        misilx.append(0)
        misily.append(0)
        misilestado.append("listo")


    def corazon():
        global corazonx
        global corazony
        global spritecorazon
        global corazonestado
        global spritevida
        global jugadorx
        global jugadory
        global corazones
        global puntaje

        for i in range(0, corazones):
            if corazonestado[i]:
                corazonx[i] -= 5
                screen.blit(corazonimg[int(spritecorazon)], (corazonx[i], corazony[i]))
                if corazonx[i] <= random.randint(-1000, -500):
                    corazonx[i] = random.randint(1500, 2500)
                    corazony[i] = random.randint(0, 400)
                if colision(jugadorx, jugadory, corazonx[i], corazony[i]):
                    canal12.play(repararsonido)
                    if spritevida == 0:
                        spritevida = 0
                        puntaje += 500
                    else:
                        spritevida -= 1
                    corazonx[i] = random.randint(3000, 4000)
                    corazony[i] = random.randint(0, 400)
        if spritecorazon >= 7:
            spritecorazon = 0
        else:
            spritecorazon += 0.5


    def jugador():
        global spritejugador
        global jugadorestado
        global spritevida
        global muerte
        global jugadorx
        global jugadory
        global jugadormovx
        global jugadormovy
        global jefeestado
        global jugadormovx1
        global jugadormovy1
        screen.blit(jugadorimg[spritejugador], (jugadorx, jugadory))
        jugadory += jugadormovy+jugadormovy1
        jugadorx += jugadormovx+jugadormovx1
        if not jefeestado:
            if jugadorx <= 0:
                jugadormovx1 = 0
                jugadorx = 0
            elif jugadorx >= 1240:
                jugadormovx = 0
                jugadorx = 1240
        else:
            if jugadorx <= 0:
                jugadormovx1 = 0
                jugadorx = 0
            elif jugadorx >= 600:
                jugadormovx = 0
                jugadorx = 600

        if jugadory <= 0:
            jugadormovy1 = 0
            jugadory = 0
        elif jugadory >= 400:
            jugadormovy = 0
            jugadory = 400
        if spritejugador >= 59:
            spritejugador = 0
        else:
            spritejugador += 1
        if not muerte:
            if spritevida >= 7:
                canal16.play(muertesonido)
                muerte = True



    def amuerte():
        global jugadorx
        global jugadory
        global jugadorestado
        global spritemuerte
        if muerte:
            screen.blit(muerteimg[int(spritemuerte)], (jugadorx, jugadory))
            if spritemuerte >= 35:
                jugadorestado = False
            else:
                spritemuerte += 0.75


    def bomba():
        global bombas
        global spritebomba
        global bombax
        global bombay
        global jefeestado
        global recargandobomba
        global jefevida
        global jefex
        global jefey
        global jefedaño
        global dañoa
        global jefemovx
        global tanquex
        global tanquey
        global nenemigos1
        global bombaestado
        global tanqueestado
        global spritetanque
        global casax11
        global casax12
        global casax21
        global casax22
        global fuegoestado
        global spritefuego
        global destruccion
        global puntaje
        global lanzamisilesestado
        global lanzamisilesx
        global lanzamisilesy
        global spritelanzamisiles
        global misillanzamisilesx
        global misillanzamisilesmovx
        global misillanzamisilesy
        global misillanzamisilesfuncion
        global misillanzamisilesestado
        global spritemisillanzamisiles
        global misillanzamisilesp
        global misileslanzamisiles
        global recargandobomba
        global jefeataque
        global spriterecargabomba
        global spritemunicionbomba
        global spritejefe
        global jefebombax
        global jefebombay
        if not jefeestado:
            for i in range(0, bombas):
                if bombaestado[i] == "disparando":
                    if spritebomba[i] <= 6:
                        screen.blit(especialimg[int(spritebomba[i])], (bombax[i], bombay[i] + 20))
                        spritebomba[i] += 0.25
                    else:
                        screen.blit(especialimg[int(spritebomba[i])], (bombax[i], bombay[i] + 20))
                        for j in range(0, nenemigos1):
                            if bombay[i] <= tanquey + 10:
                                bombay[i] += 10
                            else:
                                canal15.play(bombaexplosionsonido)
                                bombaestado[i] = "explosion"
                            if colision(tanquex[j], tanquey, bombax[i], bombay[i]) and tanqueestado[j]:
                                tanqueestado[j] = False
                                spritetanque[j] = 29
                                puntaje += 2000
                        for j in range(0, 15):
                            if (casax11[j] <= bombax[i] <= casax12[j] or casax21[j] <= bombax[i] <= casax22[j]) and bombay[
                                i] >= 570:
                                canal0.play(fuegosonido, loops=-1)
                                if destruccion < 100 and not fuegoestado[j]:
                                    destruccion += 5
                                fuegoestado[j] = True
                                puntaje += 1000
                                spritefuego[j] = 0

                if bombaestado[i] == "explosion":
                    if spritebomba[i] >= 30:
                        bombaestado[i] = "nolisto"
                    else:
                        spritebomba[i] += 0.5
                        screen.blit(especialimg[int(spritebomba[i])], (bombax[i] - 40, bombay[i] - 60))

                if bombaestado[i] == "nolisto":
                    bombax[i] = 0
                    bombay[i] = 0
        else:

            if lanzamisilesestado == "disparando":
                screen.blit(lanzamisilesimg[int(spritelanzamisiles)], (lanzamisilesx, lanzamisilesy))
                if lanzamisilesx <= 30:
                    lanzamisilesx += 2
                if spritelanzamisiles <= 19:
                    spritelanzamisiles += 0.25
                else:
                    for i in range(0, misileslanzamisiles):
                        if misillanzamisilesestado[i] == "listo":
                            canal11.play(misiltanquesonido)
                            misillanzamisilesp[i] = random.randint(20, 50)
                            misillanzamisilesestado[i] = "disparando"
                        if misillanzamisilesestado[i] == "disparando":
                            misillanzamisilesx[i] += misillanzamisilesmovx[i]
                            misillanzamisilesfuncion[i] = -math.sqrt(
                                4 * misillanzamisilesp[i] * (misillanzamisilesx[i] + 75 - 30)) + 580
                            misillanzamisilesy[i] = misillanzamisilesfuncion[i]
                            screen.blit(misillanzamisilesimg[int(spritemisillanzamisiles[i])],
                                        (misillanzamisilesx[i] + 75, int(misillanzamisilesy[i])))
                            if spritemisillanzamisiles[i] <= 9:
                                spritemisillanzamisiles[i] += 0.20
                        if misillanzamisilesx[i] >= jefex + random.randint(50, 100):
                            misillanzamisilesmovx[i] = 10
                            if spritemisillanzamisiles[i] < 9:
                                spritemisillanzamisiles[i] = 10
                            canal7.play(hitsonido)
                            if spritemisillanzamisiles[i] <= 19:
                                spritemisillanzamisiles[i] += 0.99
                            else:
                                misillanzamisilesx[i] = random.randint(-45, 30)
                                misillanzamisilesy[i] = 0
                                misillanzamisilesestado[i] = "listo"
                                spritemisillanzamisiles[i] = 0
                                misillanzamisilesmovx[i] = random.randint(10, 40)
                                if dañoa <= 20:
                                    dañoa += 0.5
                                else:
                                    if not jefedaño and not jefeataque:
                                        spritejefe = 0
                                        jefedaño = True
                                        jefevida += int(dañoa)
                                    dañoa = 0
                                    lanzamisilesestado = "retirada"
                                    for j in range(0, misileslanzamisiles):
                                        misillanzamisilesestado[j] = "nolisto"
                                        misillanzamisilesx[j] = random.randint(-45, 30)
                                        misillanzamisilesy[j] = 0

            if lanzamisilesestado == "retirada":
                screen.blit(lanzamisilesimg[int(spritelanzamisiles)], (lanzamisilesx, lanzamisilesy))
                if spritelanzamisiles >= 0:
                    spritelanzamisiles -= 0.20
                if lanzamisilesx >= -80:
                    lanzamisilesx -= 2
                else:
                    recargandobomba = "si"
                    spriterecargabomba = 0
                    spritemunicionbomba = bombas
                    lanzamisilesestado = "nolisto"


    def misil():
        global misilsprite
        global misilx
        global misily
        global cmisiles
        global misilestado
        for i in range(0, misiles):
            if misilx[i] >= 1280:
                misilestado[i] = "listo"
                misilx[i] = 0
                misily[i] = 0
            if misilestado[i] == "disparando":
                misilx[i] += 40
                screen.blit(misilimg[misilsprite], (misilx[i], misily[i] + 20))
                if misilsprite >= 13:
                    misilsprite = 0
                else:
                    misilsprite += 1
            elif misilestado[i] == "nolisto":
                misilx[i] = 0
                misily[i] = 0


    def recargabomba():
        global spriterecargabomba
        global spritemunicionbomba
        global bombaestado
        global recargandobomba
        global bombas
        global jefeestado
        global misileslanzamisiles
        global misillanzamisilesestado
        global spritemisillanzamisiles
        global lanzamisilesestado
        global spritelanzamisiles
        global misillanzamisilesx
        global misillanzamisilesy
        global misillanzamisilesmovx

        if not jefeestado:
            if recargandobomba == "si":
                screen.blit(municionbombaimg[spritemunicionbomba], (250, 685))
                screen.blit(recargabombaimg[int(spriterecargabomba)], (340, 685))
                if spriterecargabomba >= 16:
                    canal8.play(recarga2sonido)
                    spritemunicionbomba -= 1
                    spriterecargabomba = 0

                else:
                    spriterecargabomba += 0.5
                if spritemunicionbomba <= 0:
                    recargandobomba = "no"
                    for i in range(0, bombas):
                        bombaestado[i] = "listo"
                        spritebomba[i] = 0
        else:
            if recargandobomba == "si":
                screen.blit(municionbombaimg[spritemunicionbomba], (250, 685))
                screen.blit(recargabombaimg[int(spriterecargabomba)], (340, 685))
                if spriterecargabomba >= 16:
                    canal8.play(recarga2sonido)
                    spritemunicionbomba -= 1
                    spriterecargabomba = 0

                else:
                    spriterecargabomba += 0.5
                if spritemunicionbomba <= 0:
                    recargandobomba = "no"
                    lanzamisilesestado = "listo"
                    for i in range(0, misileslanzamisiles):
                        misillanzamisilesestado[i] = "listo"
                        spritemisillanzamisiles[i] = 0
                        spritelanzamisiles = 0
                        misillanzamisilesx[i] = random.randint(-45, 30)
                        misillanzamisilesy[i] = 0
                        misillanzamisilesmovx[i] = random.randint(10, 40)


    def recargamisil():
        global spriterecargamisil
        global spritemunicionmisil
        global misilestado
        global recargandomisil

        if recargandomisil == "si":
            screen.blit(recargamisilimg[int(spriterecargamisil)], (210, 685))
            screen.blit(municionmisilimg[spritemunicionmisil], (25, 685))
            if spriterecargamisil >= 22:
                canal5.play(recargasonido)
                spritemunicionmisil -= 1
                spriterecargamisil = 0
            else:
                spriterecargamisil += 1.5

            if spritemunicionmisil <= 0:
                recargandomisil = "no"
                for i in range(0, misiles):
                    misilestado[i] = "listo"


    def colision(x1, y1, x2, y2):
        proximidad = math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
        if proximidad < 40:
            return True
        else:
            return False


    # Enemigos
    misilhelicopteroimg = [pygame.image.load("Nivel 2/Enemigo2/Misil/1.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Misil/2.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Enemigo2/Misil/3.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Misil/4.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Enemigo2/Misil/5.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Misil/6.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Enemigo2/Misil/7.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Misil/8.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Enemigo2/Misil/9.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Misil/10.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Enemigo2/Misil/11.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Misil/12.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Enemigo2/Misil/13.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Misil/14.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Enemigo2/Misil/15.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Misil/16.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Enemigo2/Misil/14.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Misil/18.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Enemigo2/Misil/19.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Misil/20.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Enemigo2/Misil/21.png").convert_alpha()]
    helicopteroimg = [pygame.image.load("Nivel 2/Enemigo2/1.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/2.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/3.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/4.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/5.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/6.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/7.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/8.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/9.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/10.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/11.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/12.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/13.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/14.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/15.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/16.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/14.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/18.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/19.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/20.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/21.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/22.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/23.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/24.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/25.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/26.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/27.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/28.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/29.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/30.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/31.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/32.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/33.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/34.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/35.png").convert_alpha()]
    helicopteroimg1 = [pygame.image.load("Nivel 2/Enemigo2/Daño1/1.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño1/2.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño1/3.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño1/4.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño1/5.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño1/6.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño1/7.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño1/8.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño1/9.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño1/10.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño1/11.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño1/12.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño1/13.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño1/14.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño1/15.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño1/16.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño1/14.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño1/18.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño1/19.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño1/20.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño1/21.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño1/22.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño1/23.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño1/24.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño1/25.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño1/26.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño1/27.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño1/28.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño1/29.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño1/30.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño1/31.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño1/32.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño1/33.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño1/34.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño1/35.png").convert_alpha()]
    helicopteroimg2 = [pygame.image.load("Nivel 2/Enemigo2/Daño2/1.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño2/2.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño2/3.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño2/4.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño2/5.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño2/6.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño2/7.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño2/8.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño2/9.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño2/10.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño2/11.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño2/12.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño2/13.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño2/14.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño2/15.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño2/16.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño2/14.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño2/18.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño2/19.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño2/20.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño2/21.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño2/22.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño2/23.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño2/24.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño2/25.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño2/26.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño2/27.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño2/28.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño2/29.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño2/30.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño2/31.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño2/32.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño2/33.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño2/34.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño2/35.png").convert_alpha()]
    helicopteroimg3 = [pygame.image.load("Nivel 2/Enemigo2/Daño3/1.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño3/2.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño3/3.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño3/4.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño3/5.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño3/6.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño3/7.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño3/8.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño3/9.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño3/10.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño3/11.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño3/12.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño3/13.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño3/14.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño3/15.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño3/16.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño3/14.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño3/18.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño3/19.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño3/20.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño3/21.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño3/22.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño3/23.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño3/24.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño3/25.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo2/Daño3/26.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo2/Daño3/27.png").convert_alpha()]

    humoimg = [pygame.image.load("Nivel 2/Enemigo/Humo/1.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Humo/2.png").convert_alpha(),
            pygame.image.load("Nivel 2/Enemigo/Humo/3.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Humo/4.png").convert_alpha(),
            pygame.image.load("Nivel 2/Enemigo/Humo/5.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Humo/6.png").convert_alpha(),
            pygame.image.load("Nivel 2/Enemigo/Humo/7.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Humo/8.png").convert_alpha(),
            pygame.image.load("Nivel 2/Enemigo/Humo/9.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Humo/10.png").convert_alpha(),
            pygame.image.load("Nivel 2/Enemigo/Humo/11.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Humo/12.png").convert_alpha(),
            pygame.image.load("Nivel 2/Enemigo/Humo/13.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Humo/14.png").convert_alpha()]
    spritehumo = 0


    def helicoptero():
        global nenemigos2
        global helicopteroestado
        global spritehelicoptero
        global helicopterox
        global helicopteroy
        global cdaño
        global spriteexplosion
        global puntaje
        global fase2

        for i in range(0, nenemigos2):

            if helicopteroestado[i]:
                if cdaño[i] == 0:
                    screen.blit(helicopteroimg[spritehelicoptero], (helicopterox[i], helicopteroy[i]))
                elif cdaño[i] == 1:
                    screen.blit(helicopteroimg1[spritehelicoptero], (helicopterox[i], helicopteroy[i]))
                elif cdaño[i] == 2:
                    screen.blit(helicopteroimg2[spritehelicoptero], (helicopterox[i], helicopteroy[i]))
            else:
                if spriteexplosion >= 26:
                    helicopterox[i] = -200
                    helicopteroy[i] = 0
                    if not fase2:
                        helicopteroestado[i] = True
                        helicopterox[i] = random.randint(1280, 2000)
                        helicopteroy[i] = random.randint(0, 550)
                        cdaño[i] = 0
                    else:
                        helicopteroestado[i] = False
                else:
                    spriteexplosion += 1
                    screen.blit(helicopteroimg3[spriteexplosion], (helicopterox[i], helicopteroy[i]))

            helicopterox[i] += helicopteromovx[i]
            helicopteroy[i] += helicopteromovy[i]
            if helicopteroestado[i]:
                if misilhelicopteroestado[i] == "listo" and helicopterox[i] <= 1280:
                    misilhelicopteroestado[i] = "disparando"
                    misilhelicopterox[i] = helicopterox[i]
                    misilhelicopteroy[i] = helicopteroy[i]
                for j in range(0, misiles):
                    if colision(misilx[j], misily[j], helicopterox[i], helicopteroy[i]):
                        spriteexplosion = 0
                        puntaje += 1000
                        canal7.play(hitsonido)
                        misilx[j] = 0
                        misilx[j] = 0
                        misilestado[j] = "nolisto"
                        cdaño[i] += 1
                        if cdaño[i] == 3:
                            canal6.play(explosionsonido)
                            helicopteroestado[i] = False
                            helicopteromovx[i] = -3
                            helicopteromovy[i] = 0
                            spriteexplosion = 0

                if helicopterox[i] >= 1600:
                    helicopteromovx[i] = -random.randint(2, 5)
                elif helicopterox[i] <= 400:
                    helicopteromovx[i] = random.randint(2, 5)
                if helicopteroy[i] >= 400:
                    helicopteromovy[i] = -random.randint(3, 6)
                elif helicopteroy[i] <= 0:
                    helicopteromovy[i] = random.randint(3, 6)

        if spritehelicoptero >= 34:
            spritehelicoptero = 0
        else:
            spritehelicoptero += 1


    def misilhelicoptero():
        global nenemigos2
        global misilhelicopterox
        global misilhelicopteroy
        global spritemisilhelicoptero
        global misilhelicopteroestado
        global jugadorx
        global jugadory
        global spritevida
        global corazonestado
        global corazones
        global misilhelicopteromovx
        global helicopterox
        global helicopteroestado

        for i in range(0, nenemigos2):
            if helicopteroestado[i]:
                misilhelicopterox[i] += -misilhelicopteromovx
                if misilhelicopterox[i] <= random.randint(-1000, -500) and helicopterox[i] <= 1280:
                    misilhelicopteroestado[i] = "listo"

                if misilhelicopteroestado[i] == "disparando":
                    screen.blit(misilhelicopteroimg[spritemisilhelicoptero],
                                (misilhelicopterox[i], misilhelicopteroy[i] + 30))
                    if colision(jugadorx, jugadory, misilhelicopterox[i], misilhelicopteroy[i]):
                        canal13.play(dañosonido)
                        for j in range(0, corazones):
                            corazonestado[j] = True
                        misilhelicopterox[i] = -20
                        misilhelicopteroy[i] = 20
                        misilhelicopteroestado[i] = "nolisto"
                        if spritevida < 7:
                            spritevida += 1

        if spritemisilhelicoptero >= 20:
            spritemisilhelicoptero = 0
        else:
            spritemisilhelicoptero += 1


    tanqueiimg = [pygame.image.load("Nivel 2/Enemigo/Izquierda/1.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/2.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/3.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/4.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/5.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/6.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/7.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/8.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/9.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/10.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/11.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/12.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/13.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/14.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/15.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/16.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/17.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/18.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/19.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/20.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/21.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/22.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/23.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/24.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/25.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/26.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/27.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/28.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/29.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/30.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/31.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/32.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/33.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/34.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/35.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/36.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/37.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/38.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/39.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/40.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/41.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/42.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/43.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/44.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/45.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/46.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/47.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/48.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/49.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/50.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/51.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Izquierda/52.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Izquierda/53.png").convert_alpha()]
    tanquedimg = [pygame.image.load("Nivel 2/Enemigo/Derecha/1.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/2.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/3.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/4.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/5.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/6.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/7.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/8.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/9.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/10.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/11.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/12.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/13.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/14.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/15.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/16.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/17.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/18.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/19.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/20.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/21.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/22.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/23.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/24.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/25.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/26.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/27.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/28.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/29.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/30.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/31.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/32.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/33.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/34.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/35.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/36.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/37.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/38.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/39.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/40.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/41.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/42.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/43.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/44.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/45.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/46.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/47.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/48.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/49.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/50.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/51.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/Derecha/52.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/Derecha/53.png").convert_alpha()]
    cambiodiimg = [pygame.image.load("Nivel 2/Enemigo/CambioDI/1.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/CambioDI/2.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/CambioDI/3.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/CambioDI/4.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/CambioDI/5.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/CambioDI/6.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/CambioDI/7.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/CambioDI/8.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/CambioDI/9.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/CambioDI/10.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/CambioDI/11.png").convert_alpha()]
    cambioidimg = [pygame.image.load("Nivel 2/Enemigo/CambioID/1.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/CambioID/2.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/CambioID/3.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/CambioID/4.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/CambioID/5.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/CambioID/6.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/CambioID/7.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/CambioID/8.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/CambioID/9.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/CambioID/10.png").convert_alpha(),
                pygame.image.load("Nivel 2/Enemigo/CambioID/11.png").convert_alpha()]
    tanquemisiliimg = [pygame.image.load("Nivel 2/Enemigo/MisilI/1.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilI/2.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilI/3.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilI/4.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilI/5.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilI/6.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilI/7.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilI/8.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilI/9.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilI/10.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilI/11.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilI/12.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilI/13.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilI/14.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilI/15.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilI/16.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilI/14.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilI/18.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilI/19.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilI/20.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilI/21.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilI/22.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilI/23.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilI/24.png").convert_alpha()]
    tanquemisildimg = [pygame.image.load("Nivel 2/Enemigo/MisilD/1.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilD/2.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilD/3.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilD/4.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilD/5.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilD/6.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilD/7.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilD/8.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilD/9.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilD/10.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilD/11.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilD/12.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilD/13.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilD/14.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilD/15.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilD/16.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilD/14.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilD/18.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilD/19.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilD/20.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilD/21.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilD/22.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Enemigo/MisilD/23.png").convert_alpha(), pygame.image.load("Nivel 2/Enemigo/MisilD/24.png").convert_alpha()]


    def tanque():
        global tanquex
        global tanquemovx
        global spritetanque
        global nenemigos1
        global tanquemisilestado
        global tanquemisilmovx
        global tanquemisilmovy
        global tanquedireccion
        global cambioidestado
        global cambiodiestado
        global spritecambio
        global tanquey
        global tanquemisila
        global misilx
        global misily
        global misilestado
        global misiles
        global fase2

        for i in range(0, nenemigos1):
            if tanqueestado[i]:
                tanquex[i] += tanquemovx[i]
                if not cambioidestado[i] or not cambiodiestado[i]:
                    if tanquedireccion[i] == "izquierda":
                        screen.blit(tanqueiimg[int(spritetanque[i])], (tanquex[i], tanquey))
                    if tanquedireccion[i] == "derecha":
                        screen.blit(tanquedimg[int(spritetanque[i])], (tanquex[i], tanquey))
                if tanquex[i] <= 0:
                    tanquemovx[i] = random.randint(1, 2)
                    cambioidestado[i] = True
                    spritecambio[i] = 0
                if tanquex[i] >= 1600:
                    tanquemovx[i] = -random.randint(1, 2)
                    cambiodiestado[i] = True
                    spritecambio[i] = 0

                if cambioidestado[i]:
                    tanquemisilestado[i] = "nolisto"
                    cambiodiestado[i] = False
                    if spritecambio[i] >= 10:
                        tanquedireccion[i] = "derecha"
                        cambioidestado[i] = False
                        tanquemisilestado[i] = "listo"
                    else:
                        screen.blit(cambioidimg[int(spritecambio[i])], (tanquex[i], tanquey))
                        spritecambio[i] += 0.5
                if cambiodiestado[i]:
                    tanquemisilestado[i] = "nolisto"
                    cambioidestado[i] = False
                    if spritecambio[i] >= 10:
                        tanquedireccion[i] = "izquierda"
                        cambiodiestado[i] = False
                        tanquemisilestado[i] = "listo"
                    else:
                        screen.blit(cambiodiimg[int(spritecambio[i])], (tanquex[i], tanquey))
                        spritecambio[i] += 0.5
                if tanquemisilestado[i] != "disparando":
                    if spritetanque[i] >= 17:
                        spritetanque[i] = 0
                else:
                    if spritetanque[i] >= 27:
                        spritetanque[i] = 0
                spritetanque[i] += 0.25
                if tanquemisila[i]:
                    spritetanque[i] = 18
                    tanquemisila[i] = False
            else:
                if fase3:
                    tanquex[i] += 2
                else:
                    tanquex[i] -= 2

                if tanquedireccion[i] == "izquierda":
                    screen.blit(tanqueiimg[int(spritetanque[i])], (tanquex[i], tanquey))
                if tanquedireccion[i] == "derecha":
                    screen.blit(tanquedimg[int(spritetanque[i])], (tanquex[i], tanquey))

                if spritetanque[i] <= 52:
                    spritetanque[i] += 0.5
                if tanquex[i] <= -random.randint(-100, 0):
                    tanqueestado[i] = True
                    tanquex[i] = random.randint(1280, 1600)
                    spritetanque[i] = 0


    def misiltanque():
        global tanquemisilestado
        global tanquemisilx
        global tanquemisily
        global tanquemisilmovx
        global tanquemisilmovy
        global spritemisiltanque
        global tanquedireccion
        global cambiodiestado
        global cambioidestado
        global tanquemisila
        global tanqueestado
        global jugadorx
        global jugadory
        global spritevida

        for i in range(0, nenemigos1):
            if tanqueestado[i]:
                if tanquex[i] <= 1280 and tanquemisilestado[i] == "listo":
                    tanquemisilx[i] = tanquex[i]
                    tanquemisily[i] = tanquey
                    tanquemisilestado[i] = "disparando"
                    canal11.play(misiltanquesonido)
                    tanquemisila[i] = True

                if tanquemisilestado[i] == "disparando":
                    tanquemisilx[i] += tanquemisilmovx[i]
                    tanquemisily[i] += tanquemisilmovy[i]
                    if tanquedireccion[i] == "izquierda":
                        tanquemisilmovx[i] = -16
                        tanquemisilmovy[i] = -8
                        screen.blit(tanquemisiliimg[spritemisiltanque], (tanquemisilx[i], tanquemisily[i]))
                    if tanquedireccion[i] == "derecha":
                        tanquemisilmovx[i] = 16
                        tanquemisilmovy[i] = -8
                        screen.blit(tanquemisildimg[spritemisiltanque], (tanquemisilx[i] + 20, tanquemisily[i]))
                if colision(jugadorx, jugadory, tanquemisilx[i], tanquemisily[i]):
                    if spritevida < 7:
                        spritevida += 1
                    tanquemisilestado[i] = "listo"
                    canal13.play(dañosonido)

                if tanquemisily[i] <= random.randint(-400, -250) and (not cambioidestado[i] or not cambiodiestado[i]):
                    tanquemisilestado[i] = "listo"

        if spritemisiltanque >= 23:
            spritemisiltanque = 0
        else:
            spritemisiltanque += 1


    fuegoimg = [pygame.image.load("Nivel 2/Fuego/1.png").convert_alpha(), pygame.image.load("Nivel 2/Fuego/2.png").convert_alpha(),
                pygame.image.load("Nivel 2/Fuego/3.png").convert_alpha(), pygame.image.load("Nivel 2/Fuego/4.png").convert_alpha(),
                pygame.image.load("Nivel 2/Fuego/5.png").convert_alpha(), pygame.image.load("Nivel 2/Fuego/6.png").convert_alpha(),
                pygame.image.load("Nivel 2/Fuego/7.png").convert_alpha(), pygame.image.load("Nivel 2/Fuego/8.png").convert_alpha(),
                pygame.image.load("Nivel 2/Fuego/9.png").convert_alpha(), pygame.image.load("Nivel 2/Fuego/10.png").convert_alpha(),
                pygame.image.load("Nivel 2/Fuego/11.png").convert_alpha(), pygame.image.load("Nivel 2/Fuego/12.png").convert_alpha(),
                pygame.image.load("Nivel 2/Fuego/13.png").convert_alpha(), pygame.image.load("Nivel 2/Fuego/14.png").convert_alpha(),
                pygame.image.load("Nivel 2/Fuego/15.png").convert_alpha(), pygame.image.load("Nivel 2/Fuego/16.png").convert_alpha(),
                pygame.image.load("Nivel 2/Fuego/17.png").convert_alpha(), pygame.image.load("Nivel 2/Fuego/18.png").convert_alpha(),
                pygame.image.load("Nivel 2/Fuego/19.png").convert_alpha(), pygame.image.load("Nivel 2/Fuego/20.png").convert_alpha(),
                pygame.image.load("Nivel 2/Fuego/21.png").convert_alpha(), pygame.image.load("Nivel 2/Fuego/22.png").convert_alpha(),
                pygame.image.load("Nivel 2/Fuego/23.png").convert_alpha(), pygame.image.load("Nivel 2/Fuego/24.png").convert_alpha(),
                pygame.image.load("Nivel 2/Fuego/25.png").convert_alpha(), pygame.image.load("Nivel 2/Fuego/26.png").convert_alpha(),
                pygame.image.load("Nivel 2/Fuego/27.png").convert_alpha(), pygame.image.load("Nivel 2/Fuego/28.png").convert_alpha(),
                pygame.image.load("Nivel 2/Fuego/29.png").convert_alpha(), pygame.image.load("Nivel 2/Fuego/30.png").convert_alpha(),
                pygame.image.load("Nivel 2/Fuego/31.png").convert_alpha()]


    def fuego():
        global fase2
        global casax11
        global casax12
        global casax21
        global casax22
        global fondo1x
        global fondo2x
        for i in range(0, 15):
            if not fase2:
                if fuegoestado[i]:
                    if 0 <= fondo1x + 2560 <= 2560:
                        screen.blit(fuegoimg[int(spritefuego[i])], (casax11[i], 440))
                    if 0 <= fondo2x + 2560 <= 2560:
                        screen.blit(fuegoimg[int(spritefuego[i])], (casax21[i], 440))
                    if casax21[i] <= -25 or casax11[i] <= -25:
                        fuegoestado[i] = False
                    if spritefuego[i] >= 30:
                        spritefuego[i] = 11
                    else:
                        spritefuego[i] += 0.5
            else:
                screen.blit(fuegoimg[int(spritefuego[i])], (casax11[i], 440))
                screen.blit(fuegoimg[int(spritefuego[i])], (casax21[i], 440))
                screen.blit(fuegoimg[int(spritefuego[i])], (casax11[i] - 2560, 440))
                screen.blit(fuegoimg[int(spritefuego[i])], (casax21[i] - 2560, 440))
                if spritefuego[i] >= 30:
                    spritefuego[i] = 11
                else:
                    spritefuego[i] += 0.5


    # jefe

    jefeimg = [pygame.image.load("Nivel 2/Jefe/1.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/2.png").convert_alpha(),
            pygame.image.load("Nivel 2/Jefe/3.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/4.png").convert_alpha(),
            pygame.image.load("Nivel 2/Jefe/5.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/6.png").convert_alpha(),
            pygame.image.load("Nivel 2/Jefe/7.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/8.png").convert_alpha(),
            pygame.image.load("Nivel 2/Jefe/9.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/10.png").convert_alpha(),
            pygame.image.load("Nivel 2/Jefe/11.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/12.png").convert_alpha()]
    jefedañoimg = [pygame.image.load("Nivel 2/Jefe/Daño/1.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Daño/2.png").convert_alpha(),
                pygame.image.load("Nivel 2/Jefe/Daño/3.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Daño/4.png").convert_alpha(),
                pygame.image.load("Nivel 2/Jefe/Daño/5.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Daño/6.png").convert_alpha(),
                pygame.image.load("Nivel 2/Jefe/Daño/7.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Daño/8.png").convert_alpha(),
                pygame.image.load("Nivel 2/Jefe/Daño/9.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Daño/10.png").convert_alpha(),
                pygame.image.load("Nivel 2/Jefe/Daño/11.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Daño/12.png").convert_alpha()]
    jefebombaimg = [pygame.image.load("Nivel 2/Jefe/Bomba/1.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Bomba/2.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Jefe/Bomba/3.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Bomba/4.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Jefe/Bomba/5.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Bomba/6.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Jefe/Bomba/7.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Bomba/8.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Jefe/Bomba/9.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Bomba/10.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Jefe/Bomba/11.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Bomba/12.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Jefe/Bomba/13.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Bomba/14.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Jefe/Bomba/15.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Bomba/16.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Jefe/Bomba/17.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Bomba/18.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Jefe/Bomba/19.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Bomba/20.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Jefe/Bomba/21.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Bomba/22.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Jefe/Bomba/23.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Bomba/24.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Jefe/Bomba/25.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Bomba/26.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Jefe/Bomba/27.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Bomba/28.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Jefe/Bomba/29.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Bomba/30.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Jefe/Bomba/31.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Bomba/32.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Jefe/Bomba/33.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Bomba/34.png").convert_alpha(),
                    pygame.image.load("Nivel 2/Jefe/Bomba/35.png").convert_alpha()]
    jefeexplosionimg = [pygame.image.load("Nivel 2/Jefe/Explosion/1.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Explosion/2.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Jefe/Explosion/3.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Explosion/4.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Jefe/Explosion/5.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Explosion/6.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Jefe/Explosion/7.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Explosion/8.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Jefe/Explosion/9.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Explosion/10.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Jefe/Explosion/11.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Explosion/12.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Jefe/Explosion/13.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Explosion/14.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Jefe/Explosion/15.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Explosion/16.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Jefe/Explosion/17.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Explosion/18.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Jefe/Explosion/19.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Explosion/20.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Jefe/Explosion/21.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Explosion/22.png").convert_alpha(),
                        pygame.image.load("Nivel 2/Jefe/Explosion/23.png").convert_alpha(), pygame.image.load("Nivel 2/Jefe/Explosion/24.png").convert_alpha()]


    def jefe():
        global jefeestado
        global jefex
        global jefey
        global spritejefe
        global misilx
        global misily
        global misiles
        global misilestado
        global jefevida
        global jefeataque
        global jefemovx
        global jefedaño
        global jefebombaestado
        global spritejefebomba
        global jefebombax
        global jefebombamovx
        global jefebombay
        global funcionjefebombaestado
        global spritevida
        global jugadorx
        global jugadory
        global nenemigos1
        global tanquex
        global tanqueestado
        global dialogo10estado

        if jefeestado:
            if jefevida >= 60:
                canal20.play(explosionjefesonido)
                dialogo10estado = True
                spritejefe = 0
                jefemovx = 0
                jefeestado = False
            if jefex > 600:
                jefex -= 4
            jefex += jefemovx
            if jefex + 75 <= jugadorx <= jefex + 100 and jugadory >= jefey:
                spritevida = 7
            if jefex <= 1280:
                for i in range(0, nenemigos1):
                    if tanquex[i] >= jefex:
                        tanqueestado[i] = False
                if jefebombaestado == "listo" and not jefedaño and not jefeataque and jefex <= 750:
                    jefebombaestado = "disparando"
                    spritejefebomba = 0
                    funcionjefebombaestado = False
                    jefebombamovx = random.randint(7, 12)
                    jefebombax = jefex + 150
                    jefebombay = jefey + 213
                if not jefedaño:
                    screen.blit(jefeimg[int(spritejefe)], (jefex, jefey))
                    if spritejefe >= 11:
                        spritejefe = 0
                        if jefeataque:
                            if jefex <= 600:
                                jefemovx = 10
                            else:
                                jefemovx = 0
                                jefex = 600
                                jefeataque = False
                    else:
                        if jefeataque:
                            spritejefe += 0.75
                        else:
                            spritejefe += 0.33
                else:
                    screen.blit(jefedañoimg[int(spritejefe)], (jefex, jefey))
                    if spritejefe >= 11:
                        spritejefe = 0
                        canal18.play(superataquesonido)
                        jefeataque = True
                        jefedaño = False
                        jefemovx = -30
                        jefevida += 1
                    else:
                        spritejefe += 0.33

                if jefevida % 5 == 0 and not jefedaño:
                    jefedaño = True
                    spritejefe = 0
                for i in range(0, misiles):
                    if misilx[i] >= jefex and misily[i] >= jefey:
                        misilx[i] = 0
                        misily[i] = 0
                        misilestado[i] = "nolisto"
                        if not jefedaño and not jefeataque:
                            jefevida += 1

        if jefevida >= 60:
            screen.blit(jefeexplosionimg[int(spritejefe)], (jefex, jefey))
            if spritejefe <= 23:
                spritejefe += 0.5


    def jefebomba():

        global jefebombaestado
        global jefebombax
        global jefebombay
        global jefebombamovx
        global spritejefebomba
        global funcionjefebomba
        global funcionjefebombaestado
        global jefey
        global funcionjefebombap
        global jugadorx
        global jugadory
        global spritevida
        global dañoabomba
        global jefebombacolision

        if jefebombaestado == "disparando" and not funcionjefebombaestado:
            funcionjefebombap = random.randint(30, 175)
            funcionjefebombaestado = True
            dañoabomba = 0
            jefebombacolision = False
        if funcionjefebombaestado:
            funcionjefebomba = (pow(jefebombax - 575, 2)) / (4 * funcionjefebombap) - 75
            jefebombax -= jefebombamovx
            jefebombay = funcionjefebomba
            if spritejefebomba <= 10:
                spritejefebomba += 0.20
            if colision(jugadorx, jugadory, jefebombax, jefebombay):
                jefebombacolision = True
            if jefebombay >= 500 or jefebombacolision:
                if jefebombacolision:
                    dañoabomba += 1
                    if dañoabomba == 1:
                        spritevida += dañoabomba
                if spritejefebomba < 11:
                    spritejefebomba = 11
                if int(spritejefebomba) == 12:
                    canal14.play(bombajefeexplosionsonido)
                screen.blit(jefebombaimg[int(spritejefebomba)], (jefebombax - 25, int(jefebombay - 60)))
                jefebombamovx = 0
                if spritejefebomba >= 34:
                    jefebombaestado = "listo"
                else:
                    spritejefebomba += 0.5
            elif jefebombay < 500 or not jefebombacolision:
                screen.blit(jefebombaimg[int(spritejefebomba)], (jefebombax, int(jefebombay)))
    Icono = pygame.image.load('Imagenes/Icono.png')
    pygame.display.set_icon(Icono)
    # juego
    Pausa = False
    jugando = True
    intro = True
    lvl2 = False
    # Ventana
    reloj = pygame.time.Clock()
    # reloj.tick(60)
    canalpausa.set_volume(0.3)
    canalpausa.play(Spausa,-1)
    canalpausa.pause()
    canal17.play(cinematicasonido, loops=-1)
    canal3.play(helicopterosonido, loops=-1)
    global cinematicadialogo1estado
    global cinematicadialogo2estado
    global cinematicadialogo3estado
    global cinematicadialogo4estado
    global cinematicadialogo5estado
    global cinematicadialogo6estado
    global cinematicadialogo7estado
    global cinematicadialogo7

    while jugando:
        pygame.mouse.set_visible(0)
        canal3.set_volume(0)
        if intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    jugando = False

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        if cinematicadialogo4estado:
                            cinematicadialogo4estado = False
                            contadordialogo = 0
                            linea1 = ''
                            linea2 = ''
                            fade()
                            intro = False
                            lvl2 = True
            cinematica()
            cinematicadialogo()
            if cinematicadialogo7estado and int(contadordialogo)==len(cinematicadialogo7)-1:
                mixer.music.stop()
                canal1.stop()
                canal2.stop()
                canal3.stop()
                canal4.stop()
                canal5.stop()
                canal6.stop()
                canal7.stop()
                canal8.stop()
                canal9.stop()
                canal10.stop()
                canal11.stop()
                canal12.stop()
                canal13.stop()
                canal14.stop()
                canal15.stop()
                canal16.stop()
                canal17.stop()
                canal18.stop()
                canal19.stop()
                canal20.stop()
                canal21.stop()
                jugadorestado = True
                fondo1x = 0
                fondo2x = 2560
                spritevida = 0
                spritemuerte = 0
                spritetorrecontrol = 0
                jugadorx = 25
                jugadory = 360
                jugadormovx = 0
                jugadormovy = 0
                spritejugador = 0
                spritemunicionbomba = 10
                bombas = spritemunicionbomba
                cbombas = 0
                cmisiles = 0
                recargandomisil = "no"
                recargandobomba = "no"
                spriterecargamisil = 0
                spritemunicionmisil = misiles
                spriterecargabomba = 0
                destruccion = 0
                muerte = False
                info = open("Guardado.txt", "r")
                text=info.readline().replace("\n","")
                info.close()
                info=open(text+".txt","r")
                nombre = str(info.readline()).replace("\n","")
                puntaje = int(info.readline().replace("\n",""))
                info.close()
                spritetorrecontrol = 0
                dialogo1estado = True
                dialogo2estado = False
                dialogo3estado = False
                dialogo4estado = False
                dialogo5estado = False
                dialogo6estado = False
                dialogo7estado = False
                dialogo8estado = False
                dialogo9estado = False
                dialogo10estado = False
                linea1 = ''
                linea2 = ''
                escribiendosonidoestado = "listo"
                fase2 = False
                fase3 = False
                for i in range(0, misiles):
                    misilx[i] = 0
                    misily[i] = 0
                    misilestado[i] = "listo"

                spritehelicoptero = 0
                vidahelicoptero = 3
                spriteexplosion = 0
                for i in range(0, 15):
                    fuegoestado[i] = False
                    spritefuego[i] = 0
                    casax11[i] = casax11a[i]
                    casax12[i] = casax12a[i]
                    casax21[i] = casax11a[i] + 2560
                    casax22[i] = casax12a[i] + 2560
                    casax21a[i] = casax11a[i] + 2560
                    casax22a[i] = casax12a[i] + 2560

                spritejefebomba = 0
                spritejefe = 0
                jefex = 1500
                jefey = 50
                jefemovx = 0
                jefeestado = False
                jefevida = 1
                jefeataque = False
                jefedaño = False
                funcionjefebomba = 0
                funcionjefebombap = 0
                funcionjefebombaestado = False
                jefebombax = jefex + 150
                jefebombay = jefey + 213
                jefebombamovx = random.randint(7, 12)
                jefebombaestado = "listo"
                dañoa = 0
                dañoabomba = 0
                jefebombacolision = False

                for i in range(0, nenemigos1):
                    tanqueestado[i] = True
                    tanquex[i] = random.randint(1280, 1599)
                    tanquemovx[i] = 0
                    tanquemisilestado[i] = "listo"
                    tanquemisilx[i] = 0
                    tanquemisily[i] = 720
                    cambioidestado[i] = False
                    cambiodiestado[i] = False
                    tanquedireccion[i] = ""
                    spritecambio[i] = 0
                    tanquemisilmovy[i] = 0
                    tanquemisilmovx[i] = 0
                    spritetanque[i] = 0
                    tanquemisila[i] = False

                for i in range(0, nenemigos2):
                    helicopterox[i] = random.randint(1280, 1599)
                    helicopteroy[i] = random.randint(0, 550)
                    helicopteromovy[i] = 0  # random.randint(2, 5)
                    helicopteromovx[i] = 0  # -random.randint(2, 5)
                    helicopteroestado[i] = True
                    cdaño[i] = 0
                    misilhelicopterox[i] = 0
                    misilhelicopteroy[i] = 0
                    misilhelicopteroestado[i] = "listo"

                for i in range(0, corazones):
                    corazonx[i] = random.randint(1280, 3500)
                    corazony[i] = random.randint(0, 400)
                    corazonestado[i] = False

                spritelanzamisiles = 0
                lanzamisilesx = -80
                lanzamisilesy = 525
                lanzamisilesestado = "listo"
                misileslanzamisiles = 10
                for i in range(0, misileslanzamisiles):
                    misillanzamisilesestado[i] = "listo"
                    misillanzamisilesx[i] = random.randint(-45, 30)
                    misillanzamisilesmovx[i] = random.randint(10, 30)
                    misillanzamisilesy[i] = 0
                    spritemisillanzamisiles[i] = 0
                    misillanzamisilesfuncion[i] = 0
                    misillanzamisilesp[i] = 0

                misillanzamisilesestado[0] = "listo"

                for i in range(0, bombas):
                    bombax[i] = 0
                    bombay[i] = 0
                    bombaestado[i] = "listo"
                    spritebomba[i] = 0

                spritegameover = 0
                contadordialogo = 0
                contadorcinematica = 0
                cinematicadialogo1estado = True
                cinematicadialogo2estado = False
                cinematicadialogo3estado = False
                cinematicadialogo4estado = False
                cinematicadialogo5estado = False
                cinematicadialogo6estado = False
                cinematicadialogo7estado = False
                intro = True
                lvl2 = False
                jugando = True
                ganaste = False
                spriteganaste = 0

                return True,True


        if lvl2:
            
            canal17.set_volume(0)
            canal3.set_volume(1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jugando = False
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        jugadormovy1 = -10
                    if event.key == pygame.K_s:
                        jugadormovy = 10
                    if event.key == pygame.K_a:
                        jugadormovx1 = -10
                    if event.key == pygame.K_d:
                        jugadormovx = 10
                    if event.key == pygame.K_SPACE:
                        if recargandomisil == "no" and jugadorestado:
                            if misilestado[cmisiles] == "listo":
                                misilx[cmisiles] = jugadorx
                                misily[cmisiles] = jugadory
                                misilestado[cmisiles] = "disparando"
                                cmisiles += 1
                                canal4.play(balasonido)

                    if event.key == pygame.K_e:
                        if recargandobomba == "no" and jugadorestado:
                            if not jefeestado:
                                if bombaestado[cbombas] == "listo":
                                    canal1.play(bombasonido)
                                    bombaestado[cbombas] = "disparando"
                                    bombax[cbombas] = jugadorx
                                    bombay[cbombas] = jugadory
                                    cbombas += 1
                            else:
                                if lanzamisilesestado == "listo":
                                    lanzamisilesestado = "disparando"
                    if event.key == pygame.K_ESCAPE:
                        if not Pausa:
                            Pausa = True
                            canalpausa.unpause()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        jugadormovy = 0
                    if event.key == pygame.K_w :
                        jugadormovy1 = 0
                    if event.key == pygame.K_a:
                        jugadormovx1 = 0
                    if event.key == pygame.K_d:
                        jugadormovx = 0
                    if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                        if dialogo1estado:
                            contadordialogo = len(dialogo1) - 1
                        if dialogo2estado:
                            contadordialogo = len(dialogo2) - 1
                        if ganaste:
                            Save = open(text+".txt", "w")
                            Save.close()
                            Save = open(text+".txt", "a")
                            Save.write(nombre + "\n")
                            Save.write(str(int(puntaje + (8 - spritevida) * 600 / 8)) + "\n")
                            Save.write("2"+"\n")
                            Save.write(str(scorei))
                            Save.close()
                            canal17.set_volume(1)
                            canal0.set_volume(0)
                            canal21.set_volume(0)
                            lvl2 = False
                            fade()
                            intro = True
                            cinematicadialogo5estado = True
                            contadordialogo = 0
                            linea1 = ''
                            linea2 = ''

                        if not jugadorestado and not ganaste:
                            jugadorestado=True
                            fondo1x = 0
                            fondo2x = 2560
                            spritevida = 0
                            spritemuerte = 0
                            spritetorrecontrol = 0
                            jugadorx = 25
                            jugadory = 360
                            jugadormovx = 0
                            jugadormovy = 0
                            spritejugador = 0
                            spritemunicionbomba = 10
                            bombas = spritemunicionbomba
                            cbombas = 0
                            cmisiles = 0
                            recargandomisil = "no"
                            recargandobomba = "no"
                            spriterecargamisil = 0
                            spritemunicionmisil = misiles
                            spriterecargabomba = 0
                            destruccion = 0
                            muerte = False
                            info = open("Guardado.txt", "r")
                            text=info.readline().replace("\n","")
                            info.close()
                            info=open(text+".txt","r")
                            nombre = str(info.readline()).replace("\n","")
                            puntaje = int(info.readline().replace("\n",""))
                            info.close()
                            spritetorrecontrol = 0
                            dialogo1estado = True
                            dialogo2estado = False
                            dialogo3estado = False
                            dialogo4estado = False
                            dialogo5estado = False
                            dialogo6estado = False
                            dialogo7estado = False
                            dialogo8estado = False
                            dialogo9estado = False
                            dialogo10estado = False
                            linea1 = ''
                            linea2 = ''
                            contadordialogo = 0
                            escribiendosonidoestado = "listo"
                            fase2 = False
                            fase3 = False
                            for i in range(0, misiles):
                                misilx[i] = 0
                                misily[i] = 0
                                misilestado[i] = "listo"

                            spritehelicoptero = 0
                            vidahelicoptero = 3
                            spriteexplosion = 0
                            for i in range(0, 15):
                                fuegoestado[i] = False
                                spritefuego[i] = 0
                                casax11[i] = casax11a[i]
                                casax12[i] = casax12a[i]
                                casax21[i] = casax11a[i] + 2560
                                casax22[i] = casax12a[i] + 2560
                                casax21a[i] = casax11a[i] + 2560
                                casax22a[i] = casax12a[i] + 2560

                            spritejefebomba = 0
                            spritejefe = 0
                            jefex = 1500
                            jefey = 50
                            jefemovx = 0
                            jefeestado = False
                            jefevida = 1
                            jefeataque = False
                            jefedaño = False
                            funcionjefebomba = 0
                            funcionjefebombap = 0
                            funcionjefebombaestado = False
                            jefebombax = jefex + 150
                            jefebombay = jefey + 213
                            jefebombamovx = random.randint(7, 12)
                            jefebombaestado = "listo"
                            dañoa = 0
                            dañoabomba = 0
                            jefebombacolision = False

                            for i in range(0, nenemigos1):
                                tanqueestado[i] = True
                                tanquex[i] = random.randint(1280, 1599)
                                tanquemovx[i] = 0
                                tanquemisilestado[i] = "listo"
                                tanquemisilx[i] = 0
                                tanquemisily[i] = 720
                                cambioidestado[i] = False
                                cambiodiestado[i] = False
                                tanquedireccion[i] = ""
                                spritecambio[i] = 0
                                tanquemisilmovy[i] = 0
                                tanquemisilmovx[i] = 0
                                spritetanque[i] = 0
                                tanquemisila[i] = False

                            for i in range(0, nenemigos2):
                                helicopterox[i] = random.randint(1280, 1599)
                                helicopteroy[i] = random.randint(0, 550)
                                helicopteromovy[i] = 0 # random.randint(2, 5)
                                helicopteromovx[i] = 0  # -random.randint(2, 5)
                                helicopteroestado[i] = True
                                cdaño[i] = 0
                                misilhelicopterox[i] = 0
                                misilhelicopteroy[i] = 0
                                misilhelicopteroestado[i] = "listo"

                            for i in range(0, corazones):
                                corazonx[i] = random.randint(1280, 3500)
                                corazony[i] = random.randint(0, 400)
                                corazonestado[i] = False

                            spritelanzamisiles = 0
                            lanzamisilesx = -80
                            lanzamisilesy = 525
                            lanzamisilesestado = "listo"
                            misileslanzamisiles = 10
                            for i in range(0, misileslanzamisiles):
                                misillanzamisilesestado[i] = "listo"
                                misillanzamisilesx[i] = random.randint(-45, 30)
                                misillanzamisilesmovx[i] = random.randint(10, 30)
                                misillanzamisilesy[i] = 0
                                spritemisillanzamisiles[i] = 0
                                misillanzamisilesfuncion[i] = 0
                                misillanzamisilesp[i] = 0

                            misillanzamisilesestado[0] = "listo"

                            for i in range(0, bombas):
                                bombax[i] = 0
                                bombay[i] = 0
                                bombaestado[i] = "listo"
                                spritebomba[i] = 0

                            spritegameover = 0


            #Pausa
            while Pausa:
                canal3.pause()
                menu = Cinematica_1_1.pause()
                Pausa=False
                canal3.unpause()
                canalpausa.pause()
                if menu:
                    jugando=False
                    mixer.music.stop()
                    canal1.stop()
                    canal2.stop()
                    canal3.stop()
                    canal4.stop()
                    canal5.stop()
                    canal6.stop()
                    canal7.stop()
                    canal8.stop()
                    canal9.stop()
                    canal10.stop()
                    canal11.stop()
                    canal12.stop()
                    canal13.stop()
                    canal14.stop()
                    canal15.stop()
                    canal16.stop()
                    canal17.stop()
                    canal18.stop()
                    canal19.stop()
                    canal20.stop()
                    canal21.stop()
                    return True,False
                pygame.display.update()

            # Helicoptero

            # Actualizar movimiento/Sprites
            if destruccion >= 100 and not fase2:
                destruccion = 100
                dialogo3estado = False
                dialogo4estado = True
                fase2 = True
                contadordialogo = 0
                linea1 = ''
                linea2 = ''
                escribiendosonidoestado = "listo"
            fondo()
            if jugadorestado:
                fuego()
                tanque()
                misiltanque()
                misil()
                recargamisil()
                recargabomba()
                corazon()
                helicoptero()
                misilhelicoptero()
                jefe()
                bomba()
                jefebomba()
                jugador()
                amuerte()
                dialogo()

            if cmisiles >= misiles:
                spriterecargamisil = 0
                spritemunicionmisil = misiles
                recargandomisil = "si"
                cmisiles = 0
            if cbombas >= bombas:
                recargandobomba = "si"
                spriterecargabomba = 0
                spritemunicionbomba = bombas
                cbombas = 0
        pygame.display.update()