import pygame
from io import open
from pygame import mixer
import random
import math
import time
import sys
import Cinematica_1_1
pygame.init()
texto = pygame.font.Font('freesansbold.ttf', 32)
# txt
info = open("Guardado.txt", "r")
text=info.readline().replace("\n","")
info.close()
info=open(text+".txt","r")
nombre = str(info.readline()).replace("\n","")
puntaje = int(info.readline().replace("\n",""))
info.close()
nombreimg = texto.render(nombre, True, (255, 255, 255))
contadorcinematica = 0
cinematicadialogo1estado = True
cinematicadialogo2estado = False
cinematicadialogo3estado = False
cinematicadialogo4estado = False
cinematicadialogo5estado = False
cinematicadialogo6estado = False
cinematicadialogo7estado = False
cinematicadialogo8estado = False
cinematicadialogo1 = ['H', 'e', 'm', 'o', 's', ' ', 'i', 'n', 'v', 'e', 's', 't', 'i', 'g', 'a', 'd', 'o', ' ', 'e', 'n', ' ', 'l', 'a', 's',
                    ' ', 'r', 'u', 'i', 'n', 'a', 's', ' ', 'd', 'e', ' ', 'l', 'a', ' ', 'b', 'a', 's', 'e', ' ', 'c', 'i',
                    'e', 'n', 't', 'i', 'f', 'i', 'c', 'a', ' ', 'd', 'e', ' ', 'l', 'a', ' ', 'F', '.', 'A', '.', 'R', '.', ' ', 'y', ' ', 'e', 'n', 'c', 'o', 'n', 't', 'r', 'a', 'm', 'o','s',
                    ' ', 'p', 'i', 's', 't', 'a', 's', ' ', 'c', 'l', 'a', 'v', 'e', ' ', 'p', 'a', 'r', 'a', ' ', 'l', 'o',
                    'c', 'a', 'l', 'i', 'z', 'a', 'r', ' ', 'a', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'n', 'u', 'e', 's', 't', 'r', 'o', 's',
                    ' ', 'e', 'n', 'e', 'm', 'i', 'g', 'o', 's', '.',' ','A', ' ', 'p', 'e', 's', 'a', 'r', ' ', 'd', 'e', ' ', 'n', 'u', 'e', 's', 't', 'r', 'a', ' ', 'g', 'r', 'a', 'n',
                    ' ', 'v', 'i', 'c', 't', 'o', 'r', 'i', 'a', ' ', 'l', 'a', ' ', 'F', '.', 'A', '.', 'R', '.', ' ', 's',
                    'i', 'g', 'u', 'e', ' ', 'e', 'n', ' ', 'p', 'i', 'e', '.', '.', '.', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
cinematicadialogo2 = ['M', 'e', 's', 'e', 's', ' ', 'd', 'e', ' ', 'a', 'n', 'a', 'l', 'i', 's', 'i', 's', ' ', 'e', ' ', 'i', 'n', 'v', 'e', 's', 't',
                    'i', 'g', 'a', 'c', 'i', 'o', 'n', ' ', 'n', 'o', 's', ' ', 'l', 'l', 'e', 'v', 'ó', ' ', 'a', ' ', 'l', 'a',
                    ' ', 'p', 'o', 's', 'i', 'b', 'l', 'e', ' ', 'l', 'o', 'c', 'a', 'l', 'i', 'z', 'a', 'c', 'i', 'ó', 'n', ' ', 'd', 'e', ' ', 'l', 'o', 's', ' ',
                    'l', 'i', 'd', 'e', 'r', 'e', 's', ' ', 'p', 'r', 'i', 'n', 'c', 'i', 'p', 'a', 'l', 'e', 's', ' ', 'd', 'e', ' ', 'l',
                    'a', ' ', 'F', '.', 'A', '.', 'R', '.', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
cinematicadialogo3 = ['A', 'l', ' ', 'p', 'a', 'r', 'e', 'c', 'e', 'r', ' ', 's', 'e', ' ', 'i', 'n', 't', 'e', 'n', 't', 'a', 'r', 'á', 'n', ' ', 'r', 'e', 'u', 'n', 'i', 'r', ' ', 'e', 'n', ' ',
                    'u', 'n', 'a', ' ', 'i', 's', 'l', 'a', ' ', 'f', 'u', 'e', 'r', 'a', ' ', 'd', 'e', ' ', 'n', 'u', 'e', 's', 't', 'r', 'o', 's',
                    ' ' , 'r', 'a', 'd', 'a', 'r', 'e', 's', '.', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ]
cinematicadialogo4 = ['E', 's', ' ', 'p', 'r', 'o', 'b', 'a', 'b', 'l', 'e', ' ', 'q', 'u', 'e', ' ', 'i', 'n', 't', 'e', 'n', 't', 'e', 'n', ' ', 'e', 's', 'c', 'a', 'p',
                    'a', 'r', ' ', 'u', 'n', 'a', ' ', 'v', 'e', 'z', ' ', 'e', 's', 't', 'e', 's', ' ', 'a', 'l', 'l', 'í',
                    '.', ' ', 'p', 'o', 'r', ' ', 'e', 'l', 'l', 'o',',',' ','d', 'e', 'b', 'e', 's', ' ', 'i', 'n', 't', 'e', 'n', 't', 'a', 'r', ' ', 'c', 'a', 'p', 't', 'u', 'r','a'
                    'r', 'l', 'o', 's', ' ', 'e', 'n',' ', 's', 'u', 's', ' ', 'n', 'a', 'v', 'e', 's', ' ', 'd', 'e', ' ', 't', 'r', 'a', 'n', 's', 'p', 'o', 'r', 't', 'e', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                    ' ', '!', 'N', 'o', ' ', 'l', 'o', 's', ' ', 'd', 'e', 's', 't', 'r', 'u', 'y','a', 's', '!', ' ', 'L', 'o', 's', ' ', 'n', 'e', 'c', 'e', 's', 'i', 't', 'a'
                    'm', 'o', 's', ' ', 'v', 'i', 'v', 'o', 's', '.', '.', '.', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
cinematicadialogo5 = ['T', 'o', 'r', 'p', 'e', 'd', 'o', ':', ' ', 'I', 'n', 'h', 'a', 'b', 'i', 'l', 'i', 't', 'a', ' ', 'n', 'a', 'v', 'e', 's', ' ', 'd', 'e', ' ', 't', 'r', 'a', 'n', 's', 'p', 'o', 'r', 't', 'e',
                    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '','', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                    'L', 'a', 's', 'e', 'r', ' ', 's', 'a', 't', 'e', 'l', 'i', 't', 'a', 'l', ':', ' ', 'A', 'u', 'n', 'q', 'u', 'e', ' ', 'n', 'o',
                    ' ', 'e', 's', ' ', 'm', 'u', 'y', ' ', 'p', 'r', 'e', 'c', 'i', 's', 'a', ',', ' ', 'l', 'o', 'g', 'r', 'a', ' ', 'h', 'a', 'c', 'e', 'r', ' ', 'u', 'n', ' ', 'g', 'r', 'a', 'n',
                    ' ', 'd', 'a', 'ñ','o', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
cinematicadialogo6 = ['E', 'l', ' ', 'a', 't', 'a', 'q', 'u', 'e', ' ', 'f', 'u', 'e', ' ', 't', 'o', 'd', 'o',' ', 'u', 'n', ' ', 'é', 'x', 'i', 't', 'o',
                    '.', ' ', ' ', 'C', 'o', 'm', 'o', ' ', 'l', 'o', ' ', 's', 'u', 'p', 'o', 'n', 'í', 'a', 'm', 'o', 's',',', ' ', 'i', 'n', 't', 'e', 'n', 't', 'a', 'r', 'o', 'n',
                    ' ', 'e', 's', 'c', 'a', 'p', 'a', 'r', ' ', 'p', 'e', 'r', 'o', ' ', 'l', 'o', 's', ' ', 'c', 'a', 'p', 't', 'u', 'r', 'a', 'm', 'o', 's', ' ', 'a', ' ', 't', 'i', 'e', 'm', 'p', 'o', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
cinematicadialogo7 = ['I', 'n', 't', 'e', 'r', 'c', 'e', 'p', 't', 'a', 'm', 'o', 's', ' ', 'l', 'a', 's', ' ', 'n', 'a', 'v', 'e', 's', ' ', 'e', ' ', 'i', 'n', 't', 'e', 'r', 'r',
                    'o', 'g', 'a', 'm', 'o', 's', ' ', 'a', ' ', 's', 'u', 's', ' ', 't', 'r', 'i', 'p', 'u', 'l', 'a', 'n', 't', 'e', 's', '.',' ','A', 'u', 'n', 'q', 'u', 'e', ' ', 'a', 'l', 'g', 'u', 'n', 'o', 's', ' ', 'n', 'o', ' ', 'a', 'd', 'm', 'i', 't', 'i', 'a', 'n',
                    ' ', 's', 'e', 'r', ' ', 'm', 'i', 'e', 'm', 'b', 'r', 'o', 's', ' ', 'd', 'e',' ', 'l', 'a', ' ', 'F', '.', 'A', '.', 'R', '.',' ', 'l', 'o', 'g', 'r', 'a', 'm', 'o',
                    's', '', '', '', '', '', '', '', '', '', '', '', '', '', '',' ', 'o', 'b', 't', 'e', 'n', 'e', 'r', ' ', 'l', 'a', ' ', 'i', 'n', 'f', 'o', 'r', 'm', 'a', 'c',
                    'i', 'ó', ' ', 'q', 'u', 'e', ' ', 'n', 'o', 's', ' ', 'p', 'e', 'r', 'm', 'i', 't', 'i', 'r', 'a', ' ', 'e', 'n', 'c', 'o',
                    'n', 't', 'r', 'a', 'r', ' ', 'a', ' ','s','u', ' ', 'm', 'á', 'x', 'i', 'm', 'o', ' ', 'c', 'o', 'm', 'a', 'n', 'd', 'a', 'n', 't', 'e','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
cinematicadialogo8 = ['H','o', 'y', ' ', 'l', 'e', ' ', 'p', 'r', 'e', 's', 'e', 'n', 't', 'a', 'm', 'o','s', ' ', 'a', 'l', ' ', 's', 'i',
                    's', 't', 'e', 'm', 'a', ' ', 's', 'o', 'l','a', 'r', ' ', 'e', 's', 't', 'e', ' ', 's', 'i', 'm', 'b', 'o', 'l', 'o', ' ','d', 'e',
                    'n', 'u', 'e', 's', 't', 'r', 'a', ' ', 'v', 'i', 'c', 't', 'o', 'r','i', 'a', '.',' ','!', 'l', 'o', 's', ' ', 'b', 'u', 'e', 'n', 'o', 's',
                    ' ', 'v','e', 'n', 'c', 'e', 'r', 'e', 'm', 'o', 's', '!', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
st = 0
tx = 250
sn = 0
sh = 0
nx = 550
ny = 200
ss = 0

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
dialogo11estado = False
dialogo12estado = False
dialogo1 = ['', '', '', '', '', '', '', '', '!', 'J', 'e', 'f', 'e', '!', ' ', 'N', 'u', 'e', 's', 't', 'r', 'a', ' ',
            'm', 'i', 's', 'i', 'ó', 'n',
            ' ', 'e', 's', ' ', 'c', 'a', 'p', 't', 'u', 'r', 'a', 'r', ' ', 'a', 'l', 'g', 'u', 'n', 'a', 's', ' ',
            'n', 'a', 'v', 'e',
            's', ' ', 'e', ' ', 'i', 'n', 't', 'e', 'r', 'r', 'o', 'g', 'a', 'r', ' ', 'a', ' ', 's', 'u', 's', ' ',
            't', 'r', 'i',
            'p', 'u', 'l', 'a', 'n', 't', 'e', 's', '!', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dialogo2 = ['!', 'E', 's', 't', 'o', ' ', 'n', 'o', 's', ' ', 'p', 'o', 'd',
            'r', 'í', 'a', ' ', 'd', 'a', 'r', ' ', 'v', 'a', 'l', 'i', 'o', 's', 'a', ' ', 'i', 'n', 'f', 'o', 'r',
            'm', 'a', 'c', 'i', 'ó', 'n', '!', '', '', '', '', '', '', '', '', '', '', '', '', '', 'C', 'a', 'p', 't',
            'u', 'r', 'a', ' ', '5', '!', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dialogo3 = ['H', 'e', 'm', 'o', 's', ' ', 'i', 'n', 's', 't', 'a', 'l', 'a', 'd', 'o', ' ', 'u', 'n', ' ',
            't', 'o', 'r', 'p', 'e', 'd', 'o', ' ', 'q', 'u', 'e', ' ', 'i', 'n', 'h', 'a', 'b', 'i', 'l', 'i', 't',
            'a', ' ', 'n', 'a', 'v', 'e', 's', ' ', 'd', 'e', '', 't', 'r', 'a', 'n', 's', 'p', 'o', 'r', 't', 'e', '.'
    , ' ', ' ', ' ', '(', 'e', ')', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dialogo4 = ['L', 'o', 's', ' ', 'd', 'e', 'b', 'e', 's', ' ', 'c', 'a', 'p', 't', 'u', 'r', 'a', 'r', ',', ' ', 'n',
            'o', ' ', 'd', 'e', 's', 't',
            'r', 'u', 'i', 'r', '!', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dialogo5 = ['!', 'G', 'r', 'a', 'n', ' ', 't', 'r', 'a', 'b', 'a', 'j', 'o', ' ', 'j', 'e', 'f', 'e', '!', '', '', '',
            '', '', '', '', '', '', '', '', '']
dialogo6 = ['A', 'c', 'a', 'b', 'a', ' ', 'c', 'o', 'n', ' ', 'l', 'a', 's', ' ', 'n', 'a', 'v', 'e', 's', ' ', 'e',
            'n', 'e', 'm', 'i', 'g', 'a', 's', ' ', 'r', 'e', 's', 't',
            'a', 'n', 't', 'e', 's', '.', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dialogo7 = ['B', 'i', 'e', 'n', ' ', 'h', 'e', 'c', 'h', 'o', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
            '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '','', '', '', '', '', '', '', '', '', '!', 'E', 's', ' ', 'h', 'o', 'r', 'a',
            ' ', 'd', 'e', ' ', 'v', 'o', 'l', 'v', 'e', 'r',
            ' ', 'a', ' ', 'l', 'a', ' ', 'b', 'a', 's', 'e', '!', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dialogo8 = ['', '', '', '', '', '', '', '', '', '', '', '', '!', 'Q', 'U', '', 'E', ' ', 'F', 'U', 'E', ' ', 'E', 'S',
            'O', '!', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dialogo9 = ['!', 'E', 'l', ' ', 'e', 'n', 'e', 'm', 'i', 'g', 'o', ' ', 'i', 'n', 't', 'e', 'n', 't', 'a', ' ', 'r',
            'e', 'c', 'u', 'p', 'e',
            'r', 'a', 'r', ' ', 'l', 'a', 's', ' ', 'n', 'a', 'v', 'e', 's', ' ', 'c', 'a', 'p', 't', 'u', 'r', 'a',
            'd', 'a', 's', '!', '', '', '', '', '', '', '', '', '', '', '', '','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ]
dialogo10 = ['E', 'l', ' ', 's', 'a', 't', 'e', 'l', 'i', 't', 'e', ' ', 'e', 's', 't', 'á', ' ', 'l', 'i', 's', 't',
            'o', ' ', 'p', 'a', 'r', 'a', ' ',
            'd', 'i', 's', 'p', 'a', 'r', 'a', 'r', '!', ' ', ' ', ' ', '(', 'e', ')', '', '', '', '', '', '', '', '',
            '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dialogo11 = ['D', 'e', 's', 't', 'r', 'u', 'y', 'e', 'l', 'o', ' ', 'e', ' ', 'i', 'n', 't', 'e', 'n', 't', 'a', ' ',
            'h','u', 'í', 'r', '.', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dialogo12 = ['!', 'A', 's', 'í', ' ', 's', 'e', ' ', 'h', 'a', 'c', 'e', '!', ' ', 'H', 'o', 'r', 'a', ' ', 'd', 'e',
            ' ', 'v', 'o', 'l', 'v', 'e', 'r', '!', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
fuentedialogo = pygame.font.Font('Nivel 3/Open 24 Display St.ttf', 24)
linea1 = ''
linea2 = ''
contadordialogo = 0
linea1img = fuentedialogo.render(linea1, True, (0, 255, 0))
linea2img = fuentedialogo.render(linea2, True, (0, 255, 0))
escribiendosonidoestado = "listo"
fase2 = False
fase3 = False
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
    corazony.append(random.randint(0, 550))
    corazonestado.append(False)
spritetorrecontrol = 0
jugadorx = 25
jugadory = 360
jugadormovx = 0
jugadormovy = 0
jugadormovx1 = 0
jugadormovy1 = 0
spritejugador = 0
torpedox = 0
torpedoy = 0
torpedoestado = "listo"
spritetorpedo = 0
misilx = []
misily = []
misilsprite = 0
misilestado = []
misiles = 20
cmisiles = 0
recargandomisil = "no"
recargandotorpedo = "no"
spriterecargamisil = 0
spritemunicionmisil = misiles
spriterecargatorpedo = 0
spritemuniciontorpedo = 10

capturados = 0
capturadostotales = 5
fondo1x = 0
fondo2x = 2560
omitir = "Pulsa ENTER para omitir o continuar"
omitirimg = texto.render(omitir, True, (255, 255, 255))
jugadorestado = True
peligro = True
muerte = False
ganaste = False
fondo1x = 0
fondo2x = 2560

############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
def niv_3():
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
    global spritelaser
    global jefex
    global jefey
    global jefemovx
    global jefemovy
    global laserestado
    global jefeestado
    global jugadorx
    global jugadory
    global spritevida
    global laserxa
    global spriteplasma
    global jefex
    global jefey
    global plasmaestado
    global pendienteplasma
    global plasmamovx
    global plasmay
    global plasmax
    global plasmaxi
    global plasmayi
    global plasmas
    global misilx
    global misily
    global misiles
    global misilestado
    global spriteplasmaexplosion
    global jefeestado
    global plasmaxa
    global plasmaya
    global spritevida
    global jefevida
    global spritejefeexplosion
    global spritejefe
    global spritejefedaño
    global jefedaño
    global jefeestado
    global jefex
    global jefey
    global jefemovx
    global jefemovy
    global misilx
    global misily
    global misiles
    global misilestado
    global jefevida
    global laserestado
    global laserxa
    global spritejefeexplosion
    global jefevidatotal
    global dialogo12estado
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
    global nenemigos1
    global enemigoestado
    global spriteenemigo
    global spritehumo
    global enemigox
    global enemigoy
    global enemigoexplosion
    global spriteexplosion
    global enemigomovx
    global enemigomovy
    global capturados
    global nenemigos2
    global capturadostotales
    global vivosenemigos1
    global dialogo4estado
    global torpedox
    global torpedoy
    global torpedoestado
    global fase2
    global nenemigos2
    global helicopteroestado
    global spritehelicoptero
    global helicopterox
    global helicopteroy
    global cdaño
    global spriteexplosion
    global vivosenemigos2
    global contadorcinematica
    global spritejugador
    global contadorcinematica
    global jugadorx
    global st
    global sn
    global sh
    global tx
    global nx
    global ny
    global ss
    global cinematicadialogo5estado
    global cinematicadialogo1
    global cinematicadialogo2
    global cinematicadialogo3
    global cinematicadialogo4
    global cinematicadialogo5
    global cinematicadialogo6
    global cinematicadialogo7
    global cinematicadialogo8
    global cinematicadialogo1estado
    global cinematicadialogo2estado
    global cinematicadialogo3estado
    global cinematicadialogo4estado
    global cinematicadialogo5estado
    global cinematicadialogo6estado
    global cinematicadialogo7estado
    global cinematicadialogo8estado
    global contadordialogo
    global linea1
    global linea2
    global linea1img
    global linea2img
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
    global dialogo11estado
    global dialogo12estado
    global linea1img
    global linea2img
    global contadordialogo
    global helicopteromovx
    global helicopteromovy
    global enemigomovx
    global enemigomovy
    global nenemigos2
    global nenemigos1
    global spritetorrecontrol
    global escribiendosonidoestado
    global jefeestado
    global ganaste
    global fase3
    global corazonx
    global corazony
    global spritecorazon
    global corazonestado
    global spritevida
    global jugadorx
    global jugadory
    global corazones
    global spritejugador
    global spritevida
    global muerte
    global jugadorx
    global jugadory
    global jugadormovx
    global jugadormovy
    global jugadormovx1
    global jugadormovy1
    global jugadorx
    global jugadory
    global spritemuerte
    global spritetorpedo
    global torpedox
    global torpedoy
    global jefeestado
    global jefevida
    global spritesatelite
    global recargandotorpedo
    global satelitex
    global satelitey
    global jefex
    global jefey
    global jefedaño
    global dañoa
    global spritesatelitedaño
    global laserestado
    global laserxa
    global jefemovx
    global jefemovy
    global torpedoestado
    global misilsprite
    global misilx
    global misily
    global cmisiles
    global misilestados
    global spriterecargatorpedo
    global spritemuniciontorpedo
    global torpedoestado
    global recargandotorpedo
    global spriterecargamisil
    global spritemunicionmisil
    global misilestado
    global recargandomisil
    global laserx
    global lasery
    global bombas
    global cbombas
    global recargandobomba
    global spriterecargabomba
    global destruccion
    global vidahelicoptero
    global jugando
    global contadorcinematica
    global ganaste
    global spriteganaste
    global intro
    global lvl3

    mixer.init()
    # Ventana
    reloj = pygame.time.Clock()
    # reloj.tick(60)
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
    fondosonido = mixer.Sound("Nivel 3/Sonidos/Fondo.wav")
    helicopterosonido = mixer.Sound("Nivel 3/Sonidos/Helicoptero.wav")
    especialsonido = mixer.Sound("Nivel 3/Sonidos/Torpedo.wav")
    atrapadosonido = mixer.Sound("Nivel 3/Sonidos/NaveAtrapada.wav")
    balasonido = mixer.Sound("Nivel 3/Sonidos/Bala.wav")
    recargasonido = mixer.Sound("Nivel 3/Sonidos/Recarga.wav")
    explosionsonido = mixer.Sound("Nivel 3/Sonidos/Explosion.wav")
    hitsonido = mixer.Sound("Nivel 3/Sonidos/Hit.wav")
    recarga2sonido = mixer.Sound("Nivel 3/Sonidos/Recarga2.wav")
    repararsonido = mixer.Sound("Nivel 3/Sonidos/Reparar.wav")
    dañosonido = mixer.Sound("Nivel 3/Sonidos/Daño.wav")
    plasmasonido = mixer.Sound("Nivel 3/Sonidos/Plasma.wav")
    plasmasonido.set_volume(0.25)
    lasersonido = mixer.Sound("Nivel 3/Sonidos/Laser.wav")
    muertesonido = mixer.Sound("Nivel 3/Sonidos/Muerte.wav")
    plasmaexplosionsonido = mixer.Sound("Nivel 3/Sonidos/PlasmaE.wav")
    prejefesonido = mixer.Sound("Nivel 3/Sonidos/PreJefe.wav")
    satelitesonido = mixer.Sound("Nivel 3/Sonidos/Satelite.wav")
    escribiendosonido = mixer.Sound("Nivel 3/Sonidos/Escribiendo.wav")
    explosionjefesonido = mixer.Sound("Nivel 3/Sonidos/ExplosionJefe.wav")
    fondo2sonido = mixer.Sound("Nivel 3/Sonidos/Fondo2.wav")
    Spausa=mixer.Sound("Sonidos\\SpacyLoop.ogg")
    canalpausa.set_volume(0.3)
    canalpausa.play(Spausa,-1)
    canalpausa.pause()

    screen = pygame.display.set_mode((1280,720))
    fondo1 = pygame.image.load("Nivel 3/fondo.png").convert()
    barraestado = pygame.image.load("Nivel 3/barraestado.png").convert()

    pygame.display.set_caption("Shut 'em all")
    Icono = pygame.image.load('Imagenes/Icono.png')
    pygame.display.set_icon(Icono)


    # Introduccion

    cinematicaimg = [pygame.image.load("Nivel 3/Introduccion/1.png"), pygame.image.load("Nivel 3/Introduccion/2.png"),
                    pygame.image.load("Nivel 3/Introduccion/3.png"), pygame.image.load("Nivel 3/Introduccion/4.png"),
                    pygame.image.load("Nivel 3/Introduccion/5.png"), pygame.image.load("Nivel 3/Introduccion/6.png"),
                    pygame.image.load("Nivel 3/Introduccion/7.png"), pygame.image.load("Nivel 3/Introduccion/8.png"),
                    pygame.image.load("Nivel 3/Introduccion/9.png"), pygame.image.load("Nivel 3/Introduccion/10.png"),
                    pygame.image.load("Nivel 3/Introduccion/11.png"), pygame.image.load("Nivel 3/Introduccion/12.png")]



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
        global st
        global sn
        global sh
        global tx
        global nx
        global ny
        global ss
        global cinematicadialogo5estado

        screen.blit(cinematicaimg[contadorcinematica], (0, 0))
        if contadorcinematica == 4:
            jugadorx += 3
            screen.blit(jugadorimg[spritejugador], (jugadorx, 250))
            if jugadorx >= 800:
                jugadorx = 25
                fade()
                cinematicadialogo5estado = True
                spritejugador = 0
            if spritejugador >= 59:
                spritejugador = 0
            else:
                spritejugador += 1
        if contadorcinematica == 5:
            screen.blit(jugadorimg[spritejugador], (250, 200))
            screen.blit(jugadorimg[spritejugador], (650, 200))
            if tx <= 550:
                tx += 10
                screen.blit(enemigoimg[sn], (nx, ny))
                screen.blit(especialimg[int(st)], (tx, 200 + 40))
            else:
                nx -= 3
                ny += 3

                screen.blit(enemigoimg[sn], (nx, ny))
                screen.blit(humoimg[sh], (nx, ny-40))
                if ny >= 400:
                    tx = 250
                    nx = 550
                    ny = 200

            if sh >= 13:
                sh = 0
            else:
                sh += 1

            if sn >= 15:
                sn = 0
            else:
                sn += 1
            if st >= 15:
                st = 0
            else:
                st += 0.5

            screen.blit(sateliteimg[int(ss)], (600, 200))
            if ss >= 22:
                ss = 0
            else:
                ss += 0.25
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
        global cinematicadialogo8
        global cinematicadialogo1estado
        global cinematicadialogo2estado
        global cinematicadialogo3estado
        global cinematicadialogo4estado
        global cinematicadialogo5estado
        global cinematicadialogo6estado
        global cinematicadialogo7estado
        global cinematicadialogo8estado
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
                cinematicadialogo3estado = False
                cinematicadialogo4estado = True
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
                fade()
                cinematicadialogo4estado = False
                contadordialogo = 0
                linea1 = ''
                linea2 = ''

        if cinematicadialogo5estado:
            if contadordialogo < len(cinematicadialogo5):
                linea1img = fuentedialogo.render(linea1, True, (255, 255, 255))
                screen.blit(linea1img, (25, 625))
                linea2img = fuentedialogo.render(linea2, True, (255, 255, 255))
                screen.blit(linea2img, (25, 675))
                if contadordialogo <= 80:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea1 += cinematicadialogo5[int(contadordialogo)]

                if contadordialogo > 80:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea2 += cinematicadialogo5[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                screen.blit(linea1img, (25, 625))
                screen.blit(linea2img, (25, 675))
                screen.blit(omitirimg, (350, 350))

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
                cambioescena()
                pygame.time.delay(1600)
                fade()
                pygame.time.delay(1600)
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
                cinematicadialogo7estado = False
                cambioescena()
                cinematicadialogo8estado = True
                contadordialogo = 0
                linea1 = ''
                linea2 = ''

        if cinematicadialogo8estado:
            if contadordialogo < len(cinematicadialogo8):
                linea1img = fuentedialogo.render(linea1, True, (255, 255, 255))
                screen.blit(linea1img, (25, 625))
                linea2img = fuentedialogo.render(linea2, True, (255, 255, 255))
                screen.blit(linea2img, (25, 675))
                if contadordialogo <= 130:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea1 += cinematicadialogo8[int(contadordialogo)]

                if contadordialogo > 130:
                    if (contadordialogo / 4) % 0.25 == 0:
                        linea2 += cinematicadialogo8[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                screen.blit(linea1img, (25, 625))
                screen.blit(linea2img, (25, 675))


    municionmisilimg = [pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/1.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/2.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/3.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/4.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/5.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/6.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/7.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/8.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/9.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/10.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/11.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/12.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/13.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/14.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/15.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/16.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/17.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/18.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/19.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/20.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Municion/21.png").convert_alpha()
                        ]
    municiontorpedo = [pygame.image.load("Nivel 3/NaveSprite/Torpedo/Municion/1.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Torpedo/Municion/2.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Torpedo/Municion/3.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Torpedo/Municion/4.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Torpedo/Municion/5.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Torpedo/Municion/6.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Torpedo/Municion/7.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Torpedo/Municion/8.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Torpedo/Municion/9.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Torpedo/Municion/10.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Torpedo/Municion/11.png").convert_alpha()]
    recargamisilimg = [pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/1.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/2.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/3.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/4.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/5.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/6.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/7.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/8.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/9.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/10.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/11.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/12.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/13.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/14.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/15.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/16.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/17.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/18.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/19.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/20.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/21.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/22.png").convert_alpha(),
                    pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/23.png").convert_alpha()]
    recargatorpedoimg = [pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/1.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Misil/Recarga/2.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/3.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/4.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/5.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/6.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/7.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/8.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/9.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/10.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/11.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/12.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/13.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/14.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/15.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/16.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/17.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/18.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/19.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/20.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/21.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/22.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/23.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/24.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/25.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/26.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/27.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/28.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/29.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/30.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/31.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/32.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/33.png").convert_alpha(),
                        pygame.image.load("Nivel 3/NaveSprite/Torpedo/Recarga/34.png").convert_alpha()]
    corazonimg = [pygame.image.load("Nivel 3/Corazon/1.png").convert_alpha(), pygame.image.load("Nivel 3/Corazon/2.png").convert_alpha(),
                pygame.image.load("Nivel 3/Corazon/3.png").convert_alpha(), pygame.image.load("Nivel 3/Corazon/4.png").convert_alpha(),
                pygame.image.load("Nivel 3/Corazon/5.png").convert_alpha(), pygame.image.load("Nivel 3/Corazon/6.png").convert_alpha(),
                pygame.image.load("Nivel 3/Corazon/7.png").convert_alpha(), pygame.image.load("Nivel 3/Corazon/8.png").convert_alpha()]
    gameoverimg = [pygame.image.load("Nivel 3/Muerte/1.png").convert_alpha(), pygame.image.load("Nivel 3/Muerte/2.png").convert_alpha(),
                pygame.image.load("Nivel 3/Muerte/3.png").convert_alpha(), pygame.image.load("Nivel 3/Muerte/4.png").convert_alpha(),
                pygame.image.load("Nivel 3/Muerte/5.png").convert_alpha(), pygame.image.load("Nivel 3/Muerte/6.png").convert_alpha(),
                pygame.image.load("Nivel 3/Muerte/7.png").convert_alpha(), pygame.image.load("Nivel 3/Muerte/8.png").convert_alpha(),
                pygame.image.load("Nivel 3/Muerte/9.png").convert_alpha(), pygame.image.load("Nivel 3/Muerte/10.png").convert_alpha(),
                pygame.image.load("Nivel 3/Muerte/11.png").convert_alpha()]
    ganasteimg = [pygame.image.load("Nivel 3/Ganaste/1.png").convert_alpha(), pygame.image.load("Nivel 3/Ganaste/2.png").convert_alpha(),
                pygame.image.load("Nivel 3/Ganaste/3.png").convert_alpha(), pygame.image.load("Nivel 3/Ganaste/4.png").convert_alpha(),
                pygame.image.load("Nivel 3/Ganaste/5.png").convert_alpha(), pygame.image.load("Nivel 3/Ganaste/6.png").convert_alpha(),
                pygame.image.load("Nivel 3/Ganaste/7.png").convert_alpha(), pygame.image.load("Nivel 3/Ganaste/8.png").convert_alpha(),
                pygame.image.load("Nivel 3/Ganaste/9.png").convert_alpha(), pygame.image.load("Nivel 3/Ganaste/10.png").convert_alpha(),
                pygame.image.load("Nivel 3/Ganaste/11.png").convert_alpha()]
    muerteimg = [pygame.image.load("Nivel 3/NaveSprite/Muerte/1.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Muerte/2.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Muerte/3.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Muerte/4.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Muerte/5.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Muerte/6.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Muerte/7.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Muerte/8.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Muerte/9.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Muerte/10.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Muerte/11.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Muerte/12.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Muerte/13.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Muerte/14.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Muerte/15.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Muerte/16.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Muerte/17.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Muerte/18.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Muerte/19.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Muerte/20.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Muerte/21.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Muerte/22.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Muerte/23.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Muerte/24.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Muerte/25.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Muerte/26.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Muerte/27.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Muerte/28.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Muerte/29.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Muerte/30.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Muerte/31.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Muerte/32.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Muerte/33.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Muerte/34.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Muerte/35.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Muerte/36.png").convert_alpha()]
    # jugador
    jugadorimg = [pygame.image.load("Nivel 3/NaveSprite/1.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/2.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/3.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/4.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/5.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/6.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/7.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/8.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/9.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/10.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/11.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/12.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/13.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/14.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/15.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/16.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/17.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/18.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/19.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/20.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/21.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/22.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/23.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/24.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/25.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/26.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/27.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/28.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/29.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/30.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/31.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/32.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/33.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/34.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/35.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/36.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/37.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/38.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/39.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/40.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/41.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/42.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/43.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/44.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/45.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/46.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/47.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/48.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/49.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/50.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/51.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/52.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/53.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/54.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/55.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/56.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/57.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/58.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/59.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/60.png").convert_alpha(),
                ]
    especialimg = [pygame.image.load("Nivel 3/NaveSprite/Torpedo/1.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Torpedo/2.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Torpedo/3.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Torpedo/4.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Torpedo/5.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Torpedo/6.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Torpedo/7.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Torpedo/8.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Torpedo/9.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Torpedo/10.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Torpedo/11.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Torpedo/12.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Torpedo/13.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Torpedo/14.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Torpedo/15.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Torpedo/16.png").convert_alpha()]
    misilimg = [pygame.image.load("Nivel 3/NaveSprite/Misil/1.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Misil/2.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Misil/3.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Misil/4.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Misil/5.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Misil/6.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Misil/7.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Misil/8.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Misil/9.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Misil/10.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Misil/11.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Misil/12.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Misil/13.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Misil/14.png").convert_alpha()]
    sateliteimg = [pygame.image.load("Nivel 3/NaveSprite/Satelite/1.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Satelite/2.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Satelite/3.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Satelite/4.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Satelite/5.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Satelite/6.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Satelite/7.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Satelite/8.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Satelite/9.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Satelite/10.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Satelite/11.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Satelite/12.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Satelite/13.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Satelite/14.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Satelite/15.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Satelite/16.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Satelite/17.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Satelite/18.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Satelite/19.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Satelite/20.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Satelite/21.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Satelite/22.png").convert_alpha(),
                pygame.image.load("Nivel 3/NaveSprite/Satelite/23.png").convert_alpha()]
    spritesatelite = 0
    spritesatelitedaño = 0
    satelitex = random.randint(500, 900)
    satelitey = random.randint(-50, 365)
    spritevida = 0
    vidaimg = [pygame.image.load("Nivel 3/NaveSprite/Vida/1.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Vida/2.png").convert_alpha(),
            pygame.image.load("Nivel 3/NaveSprite/Vida/3.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Vida/4.png").convert_alpha(),
            pygame.image.load("Nivel 3/NaveSprite/Vida/5.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Vida/6.png").convert_alpha(),
            pygame.image.load("Nivel 3/NaveSprite/Vida/7.png").convert_alpha(), pygame.image.load("Nivel 3/NaveSprite/Vida/8.png").convert_alpha()]
    torrecontrolimg = [pygame.image.load("Nivel 3/TorreControl/1.png").convert_alpha(), pygame.image.load("Nivel 3/TorreControl/2.png").convert_alpha(),
                    pygame.image.load("Nivel 3/TorreControl/3.png").convert_alpha(), pygame.image.load("Nivel 3/TorreControl/4.png").convert_alpha(),
                    pygame.image.load("Nivel 3/TorreControl/5.png").convert_alpha(), pygame.image.load("Nivel 3/TorreControl/6.png").convert_alpha(),
                    pygame.image.load("Nivel 3/TorreControl/7.png").convert_alpha(), pygame.image.load("Nivel 3/TorreControl/8.png").convert_alpha(),
                    pygame.image.load("Nivel 3/TorreControl/9.png").convert_alpha(), pygame.image.load("Nivel 3/TorreControl/10.png").convert_alpha()]



    def fondo():
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

        if not fase3:
            fondo1x -= 2
            fondo2x -= 2
            if fondo1x <= -2560:
                fondo1x = 2560
            if fondo2x <= -2560:
                fondo2x = 2560
        else:
            fondo1x += 2
            fondo2x += 2
            if fondo1x >= 2560:
                fondo1x = -2560
            if fondo2x >= 2560:
                fondo2x = -2560

        screen.blit(fondo1, (fondo1x, 0))
        screen.blit(fondo1, (fondo2x, 0))
        # Barra estado
        screen.blit(barraestado, (0, 648))
        if recargandomisil == "no":
            screen.blit(municionmisilimg[cmisiles], (25, 685))
        if recargandotorpedo == "no":
            screen.blit(municiontorpedo[0], (250, 685))
        puntajeimg = texto.render("Puntaje: " + str(puntaje), True, (255, 255, 255))
        capturadosimg = texto.render("Capturados: " + str(capturados), True, (255, 255, 255))
        screen.blit(puntajeimg, (380, 657))
        screen.blit(capturadosimg, (380, 690))
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
        global dialogo11estado
        global dialogo12estado
        global linea1img
        global linea2img
        global contadordialogo
        global helicopteromovx
        global helicopteromovy
        global enemigomovx
        global enemigomovy
        global nenemigos2
        global nenemigos1
        global spritetorrecontrol
        global escribiendosonidoestado
        global jefeestado
        global ganaste
        global jugadorestado
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
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea1 += dialogo1[int(contadordialogo)]

                if contadordialogo > 49:
                    if (contadordialogo / 2) % 0.5 == 0:
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
                dialogo3estado = False
                contadordialogo = 0
                for i in range(0, nenemigos1):
                    enemigomovx[i] = random.randint(-4, 4)
                    enemigomovy[i] = random.randint(-4, 4)
                for i in range(0, nenemigos2):
                    helicopteromovy[i] = random.randint(-3, 3)
                    helicopteromovx[i] = random.randint(1, 2)
                linea1 = ''
                linea2 = ''
                escribiendosonidoestado = "listo"

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
                if dialogo7estado:
                    dialogo6estado = False
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
                if not jefeestado:
                    jefeestado = True
                    canal18.play(prejefesonido)
                    canal21.set_volume(1)
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
                dialogo10estado = True
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
                dialogo11estado = True
                contadordialogo = 0
                linea1 = ''
                linea2 = ''
                escribiendosonidoestado = "listo"

        if dialogo11estado:
            if escribiendosonidoestado == "listo":
                escribiendosonidoestado = "escribiendo"
            if contadordialogo < len(dialogo11):
                linea1img = fuentedialogo.render(linea1, True, (0, 255, 0))
                screen.blit(linea1img, (675, 650))
                linea2img = fuentedialogo.render(linea2, True, (0, 255, 0))
                screen.blit(linea2img, (675, 675))
                if contadordialogo <= 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea1 += dialogo11[int(contadordialogo)]

                if contadordialogo > 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea2 += dialogo11[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                screen.blit(linea1img, (675, 650))
                screen.blit(linea2img, (675, 675))
                if dialogo12estado:
                    dialogo11estado = False
                    contadordialogo = 0
                    linea1 = ''
                    linea2 = ''
                    escribiendosonidoestado = "listo"

        if dialogo12estado:
            if escribiendosonidoestado == "listo":
                escribiendosonidoestado = "escribiendo"
            if contadordialogo < len(dialogo12):
                linea1img = fuentedialogo.render(linea1, True, (0, 255, 0))
                screen.blit(linea1img, (675, 650))
                linea2img = fuentedialogo.render(linea2, True, (0, 255, 0))
                screen.blit(linea2img, (675, 675))
                if contadordialogo <= 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea1 += dialogo12[int(contadordialogo)]

                if contadordialogo > 49:
                    if (contadordialogo / 2) % 0.5 == 0:
                        linea2 += dialogo12[int(contadordialogo)]
                contadordialogo += 0.5
            else:
                dialogo12estado = False
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
                    corazony[i] = random.randint(0, 550)
                if colision(jugadorx, jugadory, corazonx[i], corazony[i]):
                    canal12.play(repararsonido)
                    if spritevida == 0:
                        spritevida = 0
                        puntaje += 500
                    else:
                        spritevida -= 1
                    corazonx[i] = random.randint(3000, 4000)
                    corazony[i] = random.randint(0, 550)
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
        global jugadormovx1
        global jugadormovy1
        
        # global peligro
        # Sprite jugador
        screen.blit(jugadorimg[spritejugador], (jugadorx, jugadory))
        jugadory += jugadormovy+jugadormovy1
        jugadorx += jugadormovx+jugadormovx1
        if jugadorx <= 0:
            jugadormovx1 = 0
            jugadorx = 0
        elif jugadorx >= 400:
            jugadormovx = 0
            jugadorx = 400
        if jugadory <= 0:
            jugadormovy1 = 0
            jugadory = 0
        elif jugadory >= 570:
            jugadormovy = 0
            jugadory = 570
        if spritejugador >= 59:
            spritejugador = 0
        else:
            spritejugador += 1
        if not muerte:
            if spritevida >= 7:
                canal16.play(muertesonido)
                muerte = True

        # if spritevida >= 3 and mixer.get_busy(11):
        #   canal11.mixer.play(peligrosonido, loops=1)
        #  peligro = False


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


    def torpedo():
        global spritetorpedo
        global torpedox
        global torpedoy
        global jefeestado
        global jefevida
        global spritesatelite
        global recargandotorpedo
        global satelitex
        global satelitey
        global jefex
        global jefey
        global jefedaño
        global dañoa
        global spritesatelitedaño
        global laserestado
        global laserxa
        global jefemovx
        global jefemovy
        global torpedoestado
        
        if torpedox >= 1280:
            torpedoestado = "listo"
            torpedox = 0
            torpedoy = 0

        if torpedoestado == "disparando" and not jefeestado:
            torpedox += 20
            screen.blit(especialimg[spritetorpedo], (torpedox, torpedoy + 20))
            if spritetorpedo >= 15:
                spritetorpedo = 0
            else:
                spritetorpedo += 1
        if torpedoestado == "disparando" and jefeestado:
            if spritesatelite >= 9 + spritesatelitedaño:
                recargandotorpedo = "si"
                torpedoestado == "nolisto"
                jefevida += dañoa
                dañoa = 0
                spritesatelitedaño = 0
                satelitex = random.randint(600, 900)
                satelitey = random.randint(-50, 250)
            else:
                screen.blit(sateliteimg[int(spritesatelite)], (satelitex, satelitey))
                spritesatelite += 0.25
                if 6 <= spritesatelite <= 9:
                    if (satelitex + 170 >= jefex + 150 and satelitey + 217 >= jefey and satelitey + 310 <= jefey + 145) or (
                            satelitex + 170 >= jefex and satelitey + 217 >= jefey + 145 and satelitey + 310 <= jefey + 330) or (
                            satelitex + 170 >= jefex + 150 and satelitey + 217 >= jefey + 330 and satelitey + 310 <= jefey + 430):
                        if dañoa <= 5:
                            dañoa += 1
                        spritesatelitedaño = 13
                        jefedaño = True
                        canal15.play(lasersonido)
                        if laserestado != "disparando":
                            laserestado = "disparando"
                            laserxa = jefex
                            jefevida += 1
                            jefemovx = 0
                            if jefey <= 250:
                                jefemovy = 2
                            if jefey > 250:
                                jefemovy = -2


    def misil():
        global misilsprite
        global misilx
        global misily
        global cmisiles
        global misilestados
        
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


    def recargatorpedo():
        global spriterecargatorpedo
        global spritemuniciontorpedo
        global torpedoestado
        global recargandotorpedo
        

        if recargandotorpedo == "si":
            screen.blit(municiontorpedo[spritemuniciontorpedo], (250, 685))
            screen.blit(recargatorpedoimg[spriterecargatorpedo], (340, 685))
            if spriterecargatorpedo >= 33:
                canal8.play(recarga2sonido)
                spritemuniciontorpedo -= 1
                spriterecargatorpedo = 0

            else:
                spriterecargatorpedo += 1
            if spritemuniciontorpedo <= 0:
                recargandotorpedo = "no"
                torpedoestado = "listo"


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
    nenemigos1 = 5
    nenemigos2 = 8
    vivosenemigos1 = nenemigos1
    vivosenemigos2 = nenemigos2
    misilhelicopteroimg = [pygame.image.load("Nivel 3/Enemigo2/Misil/1.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Misil/2.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Enemigo2/Misil/3.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Misil/4.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Enemigo2/Misil/5.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Misil/6.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Enemigo2/Misil/7.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Misil/8.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Enemigo2/Misil/9.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Misil/10.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Enemigo2/Misil/11.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Misil/12.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Enemigo2/Misil/13.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Misil/14.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Enemigo2/Misil/15.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Misil/16.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Enemigo2/Misil/14.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Misil/18.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Enemigo2/Misil/19.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Misil/20.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Enemigo2/Misil/21.png").convert_alpha()]
    helicopteroimg = [pygame.image.load("Nivel 3/Enemigo2/1.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/2.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/3.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/4.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/5.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/6.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/7.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/8.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/9.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/10.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/11.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/12.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/13.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/14.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/15.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/16.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/14.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/18.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/19.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/20.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/21.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/22.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/23.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/24.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/25.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/26.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/27.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/28.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/29.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/30.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/31.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/32.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/33.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/34.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/35.png").convert_alpha()]
    helicopteroimg1 = [pygame.image.load("Nivel 3/Enemigo2/Daño1/1.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño1/2.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño1/3.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño1/4.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño1/5.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño1/6.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño1/7.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño1/8.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño1/9.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño1/10.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño1/11.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño1/12.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño1/13.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño1/14.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño1/15.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño1/16.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño1/14.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño1/18.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño1/19.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño1/20.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño1/21.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño1/22.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño1/23.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño1/24.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño1/25.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño1/26.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño1/27.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño1/28.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño1/29.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño1/30.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño1/31.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño1/32.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño1/33.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño1/34.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño1/35.png").convert_alpha()]
    helicopteroimg2 = [pygame.image.load("Nivel 3/Enemigo2/Daño2/1.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño2/2.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño2/3.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño2/4.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño2/5.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño2/6.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño2/7.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño2/8.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño2/9.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño2/10.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño2/11.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño2/12.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño2/13.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño2/14.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño2/15.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño2/16.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño2/14.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño2/18.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño2/19.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño2/20.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño2/21.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño2/22.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño2/23.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño2/24.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño2/25.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño2/26.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño2/27.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño2/28.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño2/29.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño2/30.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño2/31.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño2/32.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño2/33.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño2/34.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño2/35.png").convert_alpha()]
    helicopteroimg3 = [pygame.image.load("Nivel 3/Enemigo2/Daño3/1.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño3/2.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño3/3.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño3/4.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño3/5.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño3/6.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño3/7.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño3/8.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño3/9.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño3/10.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño3/11.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño3/12.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño3/13.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño3/14.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño3/15.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño3/16.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño3/14.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño3/18.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño3/19.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño3/20.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño3/21.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño3/22.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño3/23.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño3/24.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño3/25.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo2/Daño3/26.png").convert_alpha(),
                    pygame.image.load("Nivel 3/Enemigo2/Daño3/27.png").convert_alpha()]
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
        helicopterox.append(random.randint(1500, 1800))
        helicopteroy.append(random.randint(0, 550))
        helicopteromovy.append(0)
        helicopteromovx.append(0)
        helicopteroestado.append(True)
        cdaño.append(0)
        misilhelicopterox.append(0)
        misilhelicopteroy.append(0)
        misilhelicopteroestado.append("listo")

    enemigoimg = [pygame.image.load("Nivel 3/Enemigo/1.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo/2.png").convert_alpha(),
                pygame.image.load("Nivel 3/Enemigo/3.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo/4.png").convert_alpha(),
                pygame.image.load("Nivel 3/Enemigo/5.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo/6.png").convert_alpha(),
                pygame.image.load("Nivel 3/Enemigo/7.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo/8.png").convert_alpha(),
                pygame.image.load("Nivel 3/Enemigo/9.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo/10.png").convert_alpha(),
                pygame.image.load("Nivel 3/Enemigo/11.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo/12.png").convert_alpha(),
                pygame.image.load("Nivel 3/Enemigo/13.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo/14.png").convert_alpha(),
                pygame.image.load("Nivel 3/Enemigo/15.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo/16.png").convert_alpha()]
    humoimg = [pygame.image.load("Nivel 3/Enemigo/Humo/1.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo/2.png").convert_alpha(),
            pygame.image.load("Nivel 3/Enemigo/Humo/3.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo/Humo/4.png").convert_alpha(),
            pygame.image.load("Nivel 3/Enemigo/Humo/5.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo/Humo/6.png").convert_alpha(),
            pygame.image.load("Nivel 3/Enemigo/Humo/7.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo/Humo/8.png").convert_alpha(),
            pygame.image.load("Nivel 3/Enemigo/Humo/9.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo/Humo/10.png").convert_alpha(),
            pygame.image.load("Nivel 3/Enemigo/Humo/11.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo/Humo/12.png").convert_alpha(),
            pygame.image.load("Nivel 3/Enemigo/Humo/13.png").convert_alpha(), pygame.image.load("Nivel 3/Enemigo/Humo/14.png").convert_alpha(), ]
    spritehumo = 0
    enemigoestado = []
    enemigox = []
    enemigoy = []
    enemigomovx = []
    enemigomovy = []
    spriteenemigo = 0
    enemigoexplosion = []

    for i in range(0, nenemigos1):
        enemigox.append(random.randint(1280, 2000))
        enemigoy.append(random.randint(0, 550))
        enemigomovx.append(0)
        enemigomovy.append(0)
        enemigoestado.append(True)
        enemigoexplosion.append("no")


    def helicoptero():
        global nenemigos2
        global helicopteroestado
        global spritehelicoptero
        global helicopterox
        global helicopteroy
        global cdaño
        global spriteexplosion
        global capturados
        global capturadostotales
        global puntaje
        global vivosenemigos2
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
                    if capturados < capturadostotales:
                        helicopteroestado[i] = True
                        helicopterox[i] = random.randint(1280, 2000)
                        helicopteroy[i] = random.randint(0, 550)
                        cdaño[i] = 0
                    else:
                        helicopteroestado[i] = True
                        helicopterox[i] = random.randint(1280, 2000)
                        helicopteroy[i] = random.randint(0, 550)
                        cdaño[i] = 0
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
                            if fase2:
                                vivosenemigos2 -= 1

                if helicopterox[i] >= 2000:
                    helicopteromovx[i] = -random.randint(2, 5)
                elif helicopterox[i] <= 600:
                    helicopteromovx[i] = random.randint(2, 5)
                if helicopteroy[i] >= 550:
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

        for i in range(0, nenemigos2):
            misilhelicopterox[i] += -misilhelicopteromovx
            if misilhelicopterox[i] <= random.randint(-1000, -500) and helicopterox[i] <= 1280:
                misilhelicopteroestado[i] = "listo"

            if misilhelicopteroestado[i] == "disparando":
                screen.blit(misilhelicopteroimg[spritemisilhelicoptero], (misilhelicopterox[i], misilhelicopteroy[i] + 30))
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


    def enemigo():
        global nenemigos1
        global enemigoestado
        global spriteenemigo
        global spritehumo
        global enemigox
        global enemigoy
        global enemigoexplosion
        global spriteexplosion
        global enemigomovx
        global enemigomovy
        global capturados
        global nenemigos2
        global capturadostotales
        global vivosenemigos1
        global dialogo4estado
        global torpedox
        global torpedoy
        global torpedoestado
        global fase2
        global puntaje

        for i in range(0, nenemigos1):
            if enemigoestado[i]:
                screen.blit(enemigoimg[spriteenemigo], (enemigox[i], enemigoy[i]))
            else:
                if enemigoexplosion[i] == "si":
                    screen.blit(helicopteroimg3[spriteexplosion], (enemigox[i], enemigoy[i]))
                    if spriteexplosion >= 26:
                        if capturados < capturadostotales:
                            enemigox[i] = random.randint(1280, 1600)
                            enemigoy[i] = random.randint(55, 550)
                            enemigomovx[i] = random.randint(4, 8)
                            enemigomovy[i] = random.randint(4, 8)
                            enemigoexplosion[i] = "no"
                            enemigoestado[i] = True
                        else:
                            enemigox[i] = -200
                            enemigoy[i] = 0
                            enemigomovx[i] = 0
                            enemigomovy[i] = 0
                            enemigoestado[i] = False
                    else:
                        spriteexplosion += 1
                if enemigoy[i] < 550 and enemigoexplosion[i] == "no":
                    screen.blit(humoimg[spritehumo], (enemigox[i], enemigoy[i] - 20))
                    screen.blit(enemigoimg[1], (enemigox[i], enemigoy[i]))
                if enemigoy[i] > 550:
                    if capturados < capturadostotales:
                        enemigox[i] = random.randint(1280, 1600)
                        enemigoy[i] = random.randint(55, 550)
                        enemigomovx[i] = random.randint(4, 8)
                        enemigomovy[i] = random.randint(4, 8)
                        enemigoexplosion[i] = "no"
                        enemigoestado[i] = True
                    else:
                        enemigox[i] = -200
                        enemigoy[i] = 0
                        enemigomovx[i] = 0
                        enemigomovy[i] = 0
                        enemigoestado[i] = False

            enemigox[i] += enemigomovx[i]
            enemigoy[i] += enemigomovy[i]
            if enemigoestado[i]:
                for j in range(0, misiles):
                    if colision(misilx[j], misily[j], enemigox[i], enemigoy[i]):
                        if fase2:
                            vivosenemigos1 -= 1
                        if random.randint(1, 4) == 1 and capturados < capturadostotales and not dialogo4estado:
                            dialogo4estado = True
                        spriteexplosion = 0
                        if capturados < capturadostotales:
                            puntaje -= 2000
                        enemigoestado[i] = False
                        canal6.play(explosionsonido)
                        misilestado[j] = "nolisto"
                        enemigoexplosion[i] = "si"
                        misilx[j] = 0
                        misily[j] = 0
                        enemigomovx[i] = 0
                        enemigomovy[i] = 0
                if colision(torpedox, torpedoy, enemigox[i], enemigoy[i]):
                    if fase2:
                        vivosenemigos1 -= 1
                    enemigoexplosion[i] == "no"
                    puntaje += 2500
                    capturados += 1
                    enemigoestado[i] = False
                    canal2.play(atrapadosonido)
                    torpedox = 0
                    torpedoy = 0
                    torpedoestado = "listo"
                    enemigomovx[i] = -3
                    enemigomovy[i] = 3

                if enemigox[i] >= 2000:
                    enemigomovx[i] = -random.randint(4, 8)
                elif enemigox[i] <= 500:
                    enemigomovx[i] = random.randint(4, 8)
                if enemigoy[i] >= 550:
                    enemigomovy[i] = -random.randint(4, 8)
                elif enemigoy[i] <= 0:
                    enemigomovy[i] = random.randint(4, 8)

        if spritehumo >= 13:
            spritehumo = 6
        else:
            spritehumo += 1

        if spriteenemigo >= 15:
            spriteenemigo = 0
        else:
            spriteenemigo += 1


    jefeimg = [pygame.image.load("Nivel 3/Jefe/1.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/2.png").convert_alpha(),
            pygame.image.load("Nivel 3/Jefe/3.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/4.png").convert_alpha(),
            pygame.image.load("Nivel 3/Jefe/5.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/6.png").convert_alpha(),
            pygame.image.load("Nivel 3/Jefe/7.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/8.png").convert_alpha()]
    jefedañoimg = [pygame.image.load("Nivel 3/Jefe/Daño/1.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Daño/2.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Daño/3.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Daño/4.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Daño/5.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Daño/6.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Daño/7.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Daño/8.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Daño/9.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Daño/10.png").convert_alpha()]
    jefeexplosionimg = [pygame.image.load("Nivel 3/Jefe/Explosion/1.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/2.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/3.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/4.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/5.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/6.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/7.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/8.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/9.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/10.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/11.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/12.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/13.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/14.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/15.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/16.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/17.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/18.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/19.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/20.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/21.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/22.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/23.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/24.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/25.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/26.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/27.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/28.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/29.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/30.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/31.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/32.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/33.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/34.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/35.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/36.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/37.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/38.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/39.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/40.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/41.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/42.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/43.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/44.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/45.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/46.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/47.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/48.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/49.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/50.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/51.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Explosion/52.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Explosion/53.png").convert_alpha()]
    plasmaimg = [pygame.image.load("Nivel 3/Jefe/Plasma/1.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Plasma/2.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Plasma/3.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Plasma/4.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Plasma/5.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Plasma/6.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Plasma/7.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Plasma/8.png").convert_alpha()]
    plasmaexplosionimg = [pygame.image.load("Nivel 3/Jefe/Plasma/Explosion/1.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Plasma/Explosion/2.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Plasma/Explosion/3.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Plasma/Explosion/4.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Plasma/Explosion/5.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Plasma/Explosion/6.png").convert_alpha(),
                        pygame.image.load("Nivel 3/Jefe/Plasma/Explosion/7.png").convert_alpha()]
    laserimg = [pygame.image.load("Nivel 3/Jefe/Laser/1.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Laser/2.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Laser/3.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Laser/4.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Laser/5.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Laser/6.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Laser/7.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Laser/8.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Laser/9.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Laser/10.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Laser/11.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Laser/12.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Laser/13.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Laser/14.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Laser/15.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Laser/16.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Laser/17.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Laser/18.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Laser/19.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Laser/20.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Laser/21.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Laser/22.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Laser/23.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Laser/24.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Laser/25.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Laser/26.png").convert_alpha(),
                pygame.image.load("Nivel 3/Jefe/Laser/27.png").convert_alpha(), pygame.image.load("Nivel 3/Jefe/Laser/28.png").convert_alpha()]
    plasmax = []
    plasmaxi = []
    plasmayi = []
    plasmay = []
    plasmamovx = []
    plasmaxa = []
    plasmaya = []
    plasmaestado = []
    pendienteplasma = []
    spriteplasma = 0
    spritelaser = 0
    spriteplasmaexplosion = 0
    plasmas = 5
    jefex = 2500
    jefey = random.randint(50, 400)
    jefemovx = random.randint(2, 10)
    jefemovy = random.randint(2, 5)
    spritejefe = 0
    spritejefeexplosion = 0
    jefevida = 1
    jefevidatotal = 40
    spritejefedaño = 0
    jefeestado = False
    jefedaño = False

    laserestado = "listo"
    laserx = 0
    lasery = 0
    laserxa = 0
    dañoa = 0
    for i in range(0, plasmas):
        plasmax.append(1280)
        plasmaxi.append(1280)
        plasmayi.append(0)
        plasmay.append(0)
        plasmaestado.append("nolisto")
        pendienteplasma.append(0)
        plasmamovx.append(random.randint(8, 16))
        plasmaxa.append(1280)
        plasmaya.append(0)

    plasmaestado[0] = "listo"


    def jefe():
        global spritejefe
        global spritejefedaño
        global jefedaño
        global jefeestado
        global jefex
        global jefey
        global jefemovx
        global jefemovy
        global misilx
        global misily
        global misiles
        global misilestado
        global jefevida
        global laserestado
        global laserxa
        global spritejefeexplosion
        global jefevidatotal
        global dialogo12estado
        reloj.tick(30)

        if jefeestado:
            jefex += jefemovx
            jefey += jefemovy

            if jefevida >= jefevidatotal:
                if spritejefeexplosion == 0:
                    dialogo12estado = True
                    canal20.play(explosionjefesonido)
                jefemovx = 0
                jefemovy = 0
                screen.blit(jefeexplosionimg[int(spritejefeexplosion)], (jefex, jefey))
                if spritejefeexplosion >= 52:
                    jefeestado = False
                else:
                    spritejefeexplosion += 0.33
            else:
                if not jefedaño:
                    screen.blit(jefeimg[int(spritejefe)], (jefex, jefey))
                else:
                    screen.blit(jefedañoimg[int(spritejefedaño)], (jefex, jefey))
                for i in range(0, misiles):
                    if (misilx[i] >= jefex + 175 and jefey <= misily[i] <= jefey + 145) or (
                            misilx[i] >= jefex + 25 and jefey + 145 <= misily[i] <= jefey + 330) or (
                            misilx[i] >= jefex + 175 and jefey + 330 <= misily[i] <= jefey + 430):
                        misilx[i] = 0
                        misily[i] = 0
                        misilestado[i] = "nolisto"
                        canal7.play(hitsonido)
                        if jefevida % 4 == 0:
                            jefedaño = True
                        if jefevida % 7 != 0 and laserestado != "disparando":
                            jefevida += 1
                        if jefevida % 7 == 0 and laserestado != "disparando":
                            canal15.play(lasersonido)
                            laserestado = "disparando"
                            laserxa = jefex
                            jefevida += 1
                            jefemovx = 0
                            if jefey <= 250:
                                jefemovy = 2
                            if jefey > 250:
                                jefemovy = -2
                if laserestado != "disparando":
                    if jefex <= 650:
                        jefemovx = random.randint(2, 8)
                    elif jefex >= 900:
                        jefemovx = random.randint(-8, -2)
                    if jefey <= 0:
                        jefemovy = random.randint(2, 5)
                    elif jefey >= 150:
                        jefemovy = random.randint(-5, -2)
                elif laserestado == "disparando":
                    if jefey <= 0:
                        jefemovy = 2
                    elif jefey >= 150:
                        jefemovy = -2

        if spritejefedaño >= 9:
            spritejefedaño = 0
            jefedaño = False
        else:
            spritejefedaño += 0.5
        if spritejefe >= 7:
            spritejefe = 0
        else:
            spritejefe += 0.25


    def plasma():
        global spriteplasma
        global jefex
        global jefey
        global plasmaestado
        global jugadorx
        global jugadory
        global pendienteplasma
        global plasmamovx
        global plasmay
        global plasmax
        global plasmaxi
        global plasmayi
        global plasmas
        global misilx
        global misily
        global misiles
        global misilestado
        global spriteplasmaexplosion
        global jefeestado
        global plasmaxa
        global plasmaya
        global spritevida
        global jefevida
        global spritejefeexplosion

        if jefeestado:
            for i in range(0, plasmas):
                if int(spritejefeexplosion) >= 19:
                    plasmaestado[i] == "explosion"
                if plasmaestado[i] == "listo":
                    plasmaxi[i] = jefex + 100
                    plasmayi[i] = jefey
                    plasmax[i] = plasmaxi[i]
                    pendienteplasma[i] = (plasmayi[i] - jugadory) / (plasmaxi[i] - jugadorx)
                    plasmaestado[i] = "disparando"
                    canal14.play(plasmasonido)

                if plasmaestado[i] == "disparando":
                    plasmax[i] -= plasmamovx[i]
                    plasmay[i] = pendienteplasma[i] * (plasmax[i] - plasmaxi[i]) + plasmayi[i]
                    screen.blit(plasmaimg[int(spriteplasma)], (int(plasmax[i]), int(plasmay[i])))

                for j in range(0, misiles):

                    if colision(misilx[j], misily[j], plasmax[i], plasmay[i] + 40):
                        plasmamovx[i]= random.randint(8, 16)
                        misilestado[j] = "nolisto"
                        misilx[j] = 0
                        misily[j] = 0
                        plasmaxa[i] = plasmax[i]
                        plasmaya[i] = plasmay[i]
                        plasmax[i] = -40
                        plasmay[i] = 1
                        canal17.play(plasmaexplosionsonido)
                        plasmaestado[i] = "explosion"
                        spriteplasmaexplosion = 0

                if colision(jugadorx, jugadory, plasmax[i], plasmay[i]):
                    plasmamovx[i] = random.randint(8, 16)
                    plasmaxa[i] = plasmax[i]
                    plasmaya[i] = plasmay[i]
                    plasmax[i] = -40
                    plasmay[i] = 40
                    canal17.play(plasmaexplosionsonido)
                    canal7.play(hitsonido)
                    if spritevida < 7:
                        spritevida += 1
                    plasmaestado[i] = "explosion"
                    spriteplasmaexplosion = 0

                if plasmaestado[i] == "explosion":
                    if spriteplasmaexplosion >= 7:
                        if spritejefeexplosion >= 19:
                            plasmaestado[i] = "nolisto"
                            plasmamovx[i] = random.randint(8, 16)
                        else:
                            plasmaestado[i] = "listo"
                    else:
                        screen.blit(plasmaexplosionimg[int(spriteplasmaexplosion)], (int(plasmaxa[i]), int(plasmaya[i])))
                        spriteplasmaexplosion += 0.25

                if plasmax[i] <= -200 or (plasmay[i] < 0 or plasmay[i] >= 550):
                    plasmamovx[i] = random.randint(8, 16)
                    plasmaestado[i] = "listo"
                    plasmax[i] = -40
                    plasmay[i] = 10

                if i < plasmas - 1 and 600 <= plasmax[i] <= 605 and plasmaestado[i + 1] == "nolisto":
                    plasmamovx[i] = random.randint(8, 16)
                    plasmaestado[i + 1] = "listo"

        if spriteplasma >= 7:
            spriteplasma = 0
        else:
            spriteplasma += 0.5


    def laser():
        global spritelaser
        global jefex
        global jefey
        global jefemovx
        global jefemovy
        global laserestado
        global jefeestado
        global jugadorx
        global jugadory
        global spritevida
        global laserxa

        if laserestado == "disparando" and jefeestado:
            screen.blit(laserimg[int(spritelaser)], (jefex - 1075, jefey + 375))
            if spritelaser >= 27:
                spritelaser = 0
                laserestado = "nolisto"
            else:
                if spritelaser <= 3:
                    spritelaser += 0.028
                else:
                    laserxa -= 16
                    spritelaser += 0.3
                    if jefey + 392 <= jugadory + 40 <= jefey + 458 and jugadorx >= laserxa:
                        if spritevida < 7:
                            spritevida += 7 - spritevida

    canal0.play(fondosonido,-1)
    Icono = pygame.image.load('Nivel 3/Icono.png')
    pygame.display.set_icon(Icono)
    canal3.play(helicopterosonido, loops=-1)
    canal0.play(helicopterosonido, loops=-1)
    # juego
    Pausa=False
    jugando = True
    intro = True
    lvl3 = False

    while jugando:
        pygame.mouse.set_visible(0)
        if intro:
            canal3.set_volume(0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jugando = False
                    sys.exit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                        if cinematicadialogo5estado:
                            cinematicadialogo5estado = False
                            contadordialogo = 0
                            linea1 = ''
                            linea2 = ''
                            fade()
                            intro = False
                            canal0.pause()
                            lvl3 = True
            cinematica()
            cinematicadialogo()
            if cinematicadialogo8estado and int(contadordialogo)==len(cinematicadialogo8)-1:
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

                vivosenemigos1 = nenemigos1
                vivosenemigos2 = nenemigos2

                for i in range(0, nenemigos1):
                    enemigox[i] = random.randint(1280, 2000)
                    enemigoy[i] = random.randint(0, 550)
                    enemigomovx[i] = 0
                    enemigomovy[i] = 0
                    enemigoestado[i] = True
                    enemigoexplosion[i] = "no"

                spritegameover = 0
                jugadorestado = True
                spriteplasma = 0
                spritelaser = 0
                spriteplasmaexplosion = 0
                jefex = 2500
                jefey = random.randint(50, 400)
                jefemovx = random.randint(2, 10)
                jefemovy = random.randint(2, 5)
                spritejefe = 0
                spritejefeexplosion = 0
                jefevida = 1
                jefevidatotal = 40
                spritejefedaño = 0
                jefeestado = False
                jefedaño = False
                laserestado = "listo"
                laserx = 0
                lasery = 0
                laserxa = 0
                dañoa = 0
                for i in range(0, plasmas):
                    plasmax[i] = 1280
                    plasmaxi[i] = 1280
                    plasmayi[i] = 0
                    plasmay[i] = 0
                    plasmaestado[i] = "nolisto"
                    pendienteplasma[i] = 0
                    plasmamovx[i] = random.randint(8, 16)
                    plasmaxa[i] = 1280
                    plasmaya[i] = 0

                capturados = 0

                plasmaestado[0] = "listo"
                contadorcinematica = 0
                cinematicadialogo1estado = True
                cinematicadialogo2estado = False
                cinematicadialogo3estado = False
                cinematicadialogo4estado = False
                cinematicadialogo5estado = False
                cinematicadialogo6estado = False
                cinematicadialogo7estado = False
                cinematicadialogo8estado = False
                spriteganaste = 0

                intro = True
                lvl3 = False
                jugando = True
                ganaste = False
                return True,True

        if lvl3:
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
                        if recargandomisil == "no":
                            if misilestado[cmisiles] == "listo" and jugadorestado:
                                misilx[cmisiles] = jugadorx
                                misily[cmisiles] = jugadory
                                misilestado[cmisiles] = "disparando"
                                cmisiles += 1
                                canal4.play(balasonido)

                    if event.key == pygame.K_e:
                        if recargandotorpedo == "no" and jugadorestado:
                            if torpedoestado == "listo":
                                recargandotorpedo = "si"
                                spriterecargatorpedo = 0
                                spritesatelite = 0
                                spritemuniciontorpedo = 10
                                if jefeestado:
                                    canal1.play(satelitesonido)
                                else:
                                    canal1.play(especialsonido)
                                torpedoestado = "disparando"
                                torpedox = jugadorx
                                torpedoy = jugadory
                    if event.key == pygame.K_ESCAPE:
                        if not Pausa:
                            Pausa=True
                            canalpausa.unpause()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        jugadormovy1 = 0
                    if event.key == pygame.K_s:
                        jugadormovy = 0
                    if event.key == pygame.K_a:
                        jugadormovx1 = 0
                    if event.key == pygame.K_d:
                        jugadormovx = 0
                    if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                        if dialogo1estado:
                            contadordialogo = len(dialogo1)-1
                        if dialogo2estado:
                            contadordialogo = len(dialogo2) - 1
                        if dialogo3estado:
                            contadordialogo = len(dialogo3) - 1
                        if ganaste:
                            Save = open("Guardado.txt", "r")
                            text=Save.readline().replace("\n","")
                            Save.close()
                            Save = open(text+".txt", "w")
                            Save.close()
                            Save = open(text+".txt", "a")
                            Save.write(nombre + "\n")
                            Save.write(str(int(puntaje + (8 - spritevida) * 600 / 8)) + "\n")
                            Save.write("3"+"\n")
                            Save.write(str(scorei))
                            Save.close()
                            canal21.set_volume(0)
                            lvl3 = False
                            fade()
                            intro = True
                            cinematicadialogo6estado = True
                            contadordialogo = 0
                            linea1 = ''
                            linea2 = ''
                            canal0.unpause()


                        if not jugadorestado and not ganaste:
                            canal21.set_volume(0)
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
                            dialogo11estado = False
                            dialogo12estado = False
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


                            for i in range(0, nenemigos2):
                                helicopterox[i] = random.randint(1280, 1599)
                                helicopteroy[i] = random.randint(0, 550)
                                helicopteromovy[i] = 0
                                helicopteromovx[i] = 0
                                helicopteroestado[i] = True
                                cdaño[i] = 0
                                misilhelicopterox[i] = 0
                                misilhelicopteroy[i] = 0
                                misilhelicopteroestado[i] = "listo"

                            for i in range(0, corazones):
                                corazonx[i] = random.randint(1280, 3500)
                                corazony[i] = random.randint(0, 400)
                                corazonestado[i] = False

                            vivosenemigos1 = nenemigos1
                            vivosenemigos2 = nenemigos2

                            for i in range(0, nenemigos1):
                                enemigox[i] = random.randint(1280, 2000)
                                enemigoy[i] = random.randint(0, 550)
                                enemigomovx[i] = 0
                                enemigomovy[i] = 0
                                enemigoestado[i] = True
                                enemigoexplosion[i] = "no"

                            spritegameover = 0
                            jugadorestado = True
                            spriteplasma = 0
                            spritelaser = 0
                            spriteplasmaexplosion = 0
                            jefex = 2500
                            jefey = random.randint(50, 400)
                            jefemovx = random.randint(2, 10)
                            jefemovy = random.randint(2, 5)
                            spritejefe = 0
                            spritejefeexplosion = 0
                            jefevida = 1
                            jefevidatotal = 40
                            spritejefedaño = 0
                            jefeestado = False
                            jefedaño = False
                            laserestado = "listo"
                            laserx = 0
                            lasery = 0
                            laserxa = 0
                            dañoa = 0
                            for i in range(0, plasmas):
                                plasmax[i] = 1280
                                plasmaxi[i] = 1280
                                plasmayi[i] = 0
                                plasmay[i] = 0
                                plasmaestado[i] = "nolisto"
                                pendienteplasma[i] = 0
                                plasmamovx[i] = random.randint(8, 16)
                                plasmaxa[i] = 1280
                                plasmaya[i] = 0

                            plasmaestado[0] = "listo"

                            capturados = 0

            #Pausa
            while Pausa:
                canal3.pause()
                menu=Cinematica_1_1.pause()
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

            if capturados >= capturadostotales and not fase2:
                fase2 = True
                dialogo5estado = True

            if (vivosenemigos1 <= 0 or vivosenemigos2 <= 0) and not fase3:
                fase3 = True
                dialogo7estado = True
            fondo()
            if jugadorestado:
                jugador()
                misil()
                recargamisil()
                recargatorpedo()
                corazon()
                jefe()
                plasma()
                laser()
                enemigo()
                helicoptero()
                misilhelicoptero()
                amuerte()
                torpedo()
                dialogo()

            if cmisiles >= misiles:
                spriterecargamisil = 0
                spritemunicionmisil = misiles
                recargandomisil = "si"
                cmisiles = 0

        pygame.display.update()
