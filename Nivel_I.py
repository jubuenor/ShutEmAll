import pygame
from io import open
from pygame import mixer
import random
import math
import time
import sys
import Cinematica_1_1
pygame.init()
spritemuerte = 0
corazones = 6
corazonx = []
corazony = []
corazonestado = []
spritecorazon = 0
spritegameover = 0
for i in range(0, corazones):
    corazonx.append(random.randint(1280, 3500))
    corazony.append(random.randint(0, 400))
    corazonestado.append(False)
spritetorrecontrol = 0
jugadorx = 25
jugadory = 360
jugadormovx = 0
jugadormovy = 0
jugadormovx1 = 0
jugadormovy1 = 0
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
fondo1x = 0
fondo2x = 2560
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
texto = pygame.font.Font('freesansbold.ttf', 32)
omitir = "Pulsa ENTER para omitir o continuar"
omitirimg = texto.render(omitir, True, (255, 255, 255))
jugadorestado = True
peligro = True
muerte = False

# txt
info = open("Guardado.txt", "r")
text=info.readline().replace("\n","")
info.close()
info = open(text+".txt", "r")
nombre = str(info.readline()).replace("\n","")
punt=str(info.readline()).replace("\n","")
niv=str(info.readline()).replace("\n","")
score=str(info.readline()).replace("\n","")
info.close()
puntaje = 0
eliminaciones = 0
nombreimg = texto.render(nombre, True, (255, 255, 255))

def niv_I():
    global score
    global niv
    global punt
    global text
    info = open("Guardado.txt", "r")
    text=info.readline().replace("\n","")
    info.close()
    info = open(text+".txt", "r")
    nombre = str(info.readline()).replace("\n","")
    punt=str(info.readline()).replace("\n","")
    niv=str(info.readline()).replace("\n","")
    score=str(info.readline()).replace("\n","")
    info.close()
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
    global nenemigos2
    global helicopteroestado
    global spritehelicoptero
    global helicopterox
    global helicopteroy
    global cdaño
    global spriteexplosion
    global puntaje
    global eliminaciones
    global reaparicion
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
    global eliminaciones
    global corazonx
    global corazony
    global spritecorazon
    global corazonestado
    global spritevida
    global jugadorx
    global jugadory
    global corazones
    global puntaje
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
    global jugadorx
    global jugadory
    global jugadorestado
    global spritemuerte
    global bombas
    global spritebomba
    global bombax
    global bombay
    global recargandobomba
    global tanquex
    global tanquey
    global nenemigos1
    global bombaestado
    global tanqueestado
    global spritetanque
    global puntaje
    global recargandobomba
    global spriterecargabomba
    global spritemunicionbomba
    global eliminaciones
    global reaparicion
    global misilsprite
    global misilx
    global misily
    global cmisiles
    global misilestado
    global spriterecargabomba
    global spritemunicionbomba
    global bombaestado
    global recargandobomba
    global bombas
    global spritebomba
    global spriterecargamisil
    global spritemunicionmisil
    global misilestado
    global recargandomisil
    global fondo1x
    global fondo2x
    global cmisiles
    global spritegameover
    global nombreimg
    global jugadorx
    global jugadorestado
    global cbombas
    global eliminaciones
    global linea1
    global linea2
    global dialogo1estado
    global dialogo2estado
    global dialogo3estado
    global dialogo4estado
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
    global jugadorestado
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
    Spausa=mixer.Sound("Sonidos\\SpacyLoop.ogg")
    fuegosonido = mixer.Sound("Nivel I/Sonidos/Fuego.wav")
    helicopterosonido = mixer.Sound("Nivel I/Sonidos/Helicoptero.wav")
    bombasonido = mixer.Sound("Nivel I/Sonidos/Bomba.wav")
    atrapadosonido = mixer.Sound("Nivel I/Sonidos/NaveAtrapada.wav")
    balasonido = mixer.Sound("Nivel I/Sonidos/Bala.wav")
    recargasonido = mixer.Sound("Nivel I/Sonidos/Recarga.wav")
    explosionsonido = mixer.Sound("Nivel I/Sonidos/Explosion.wav")
    hitsonido = mixer.Sound("Nivel I/Sonidos/Hit.wav")
    recarga2sonido = mixer.Sound("Nivel I/Sonidos/Recarga2.wav")
    navesonido = mixer.Sound("Nivel I/Sonidos/Nave.wav")
    misiltanquesonido = mixer.Sound("Nivel I/Sonidos/MisilTanque.wav")
    repararsonido = mixer.Sound("Nivel I/Sonidos/Reparar.wav")
    dañosonido = mixer.Sound("Nivel I/Sonidos/Daño.wav")
    bombajefeexplosionsonido = mixer.Sound("Nivel I/Sonidos/BombaExplosionJefe.wav")
    bombaexplosionsonido = mixer.Sound("Nivel I/Sonidos/BombaExplosion.wav")
    muertesonido = mixer.Sound("Nivel I/Sonidos/Muerte.wav")
    plasmaexplosionsonido = mixer.Sound("Nivel I/Sonidos/PlasmaE.wav")
    satelitesonido = mixer.Sound("Nivel I/Sonidos/Satelite.wav")
    escribiendosonido = mixer.Sound("Nivel I/Sonidos/Escribiendo.wav")
    explosionjefesonido = mixer.Sound("Nivel I/Sonidos/ExplosionJefe.wav")
    fondo2sonido = mixer.Sound("Nivel I/Sonidos/Fondo2.wav")
    superataquesonido = mixer.Sound("Nivel I/Sonidos/SuperAtaque.wav")
    cinematicasonido = mixer.Sound("Nivel I/Sonidos/Cinematica.wav")
    screen = pygame.display.set_mode((1280, 720))
    screen.fill((0, 0, 0))
    pygame.display.set_caption("Shut 'em all")
    fuentedialogo = pygame.font.Font('Nivel I/Open 24 Display St.ttf', 24)
    Icono = pygame.image.load('Imagenes\\Icono.png')
    pygame.display.set_icon(Icono)
    fondo1 = pygame.image.load("Nivel I/fondo.png")
    barraestado = pygame.image.load("Nivel I/barraestado.png")
    municionmisilimg = [pygame.image.load("Nivel I/NaveSprite/Misil/Municion/1.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/2.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/3.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/4.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/5.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/6.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/7.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/8.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/9.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/10.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/11.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/12.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/13.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/14.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/15.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/16.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/17.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/18.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/19.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/20.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Misil/Municion/21.png").convert_alpha()
                        ]
    municionbombaimg = [pygame.image.load("Nivel I/NaveSprite/Bomba/Municion/1.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Bomba/Municion/2.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Bomba/Municion/3.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Bomba/Municion/4.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Bomba/Municion/5.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Bomba/Municion/6.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Bomba/Municion/7.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Bomba/Municion/8.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Bomba/Municion/9.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Bomba/Municion/10.png").convert_alpha(),
                        pygame.image.load("Nivel I/NaveSprite/Bomba/Municion/11.png").convert_alpha()]
    recargamisilimg = [pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/1.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/2.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/3.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/4.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/5.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/6.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/7.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/8.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/9.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/10.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/11.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/12.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/13.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/14.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/15.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/16.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/17.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/18.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/19.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/20.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/21.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/22.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Misil/Recarga/23.png").convert_alpha()]
    recargabombaimg = [pygame.image.load("Nivel I/NaveSprite/Bomba/Recarga/1.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Bomba/Recarga/2.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Bomba/Recarga/3.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Bomba/Recarga/4.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Bomba/Recarga/5.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Bomba/Recarga/6.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Bomba/Recarga/7.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Bomba/Recarga/8.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Bomba/Recarga/9.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Bomba/Recarga/10.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Bomba/Recarga/11.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Bomba/Recarga/12.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Bomba/Recarga/13.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Bomba/Recarga/14.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Bomba/Recarga/15.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Bomba/Recarga/16.png").convert_alpha(),
                    pygame.image.load("Nivel I/NaveSprite/Bomba/Recarga/17.png").convert_alpha()]
    corazonimg = [pygame.image.load("Nivel I/Corazon/1.png").convert_alpha(), pygame.image.load("Nivel I/Corazon/2.png").convert_alpha(),
                pygame.image.load("Nivel I/Corazon/3.png").convert_alpha(), pygame.image.load("Nivel I/Corazon/4.png").convert_alpha(),
                pygame.image.load("Nivel I/Corazon/5.png").convert_alpha(), pygame.image.load("Nivel I/Corazon/6.png").convert_alpha(),
                pygame.image.load("Nivel I/Corazon/7.png").convert_alpha(), pygame.image.load("Nivel I/Corazon/8.png").convert_alpha()]
    gameoverimg = [pygame.image.load("Nivel I/Muerte/1.png").convert_alpha(), pygame.image.load("Nivel I/Muerte/2.png").convert_alpha(),
                pygame.image.load("Nivel I/Muerte/3.png").convert_alpha(), pygame.image.load("Nivel I/Muerte/4.png").convert_alpha(),
                pygame.image.load("Nivel I/Muerte/5.png").convert_alpha(), pygame.image.load("Nivel I/Muerte/6.png").convert_alpha(),
                pygame.image.load("Nivel I/Muerte/7.png").convert_alpha(), pygame.image.load("Nivel I/Muerte/8.png").convert_alpha(),
                pygame.image.load("Nivel I/Muerte/9.png").convert_alpha(), pygame.image.load("Nivel I/Muerte/10.png").convert_alpha(),
                pygame.image.load("Nivel I/Muerte/11.png").convert_alpha()]
    muerteimg = [pygame.image.load("Nivel I/NaveSprite/Muerte/1.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Muerte/2.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Muerte/3.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Muerte/4.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Muerte/5.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Muerte/6.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Muerte/7.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Muerte/8.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Muerte/9.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Muerte/10.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Muerte/11.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Muerte/12.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Muerte/13.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Muerte/14.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Muerte/15.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Muerte/16.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Muerte/17.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Muerte/18.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Muerte/19.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Muerte/20.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Muerte/21.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Muerte/22.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Muerte/23.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Muerte/24.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Muerte/25.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Muerte/26.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Muerte/27.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Muerte/28.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Muerte/29.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Muerte/30.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Muerte/31.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Muerte/32.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Muerte/33.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Muerte/34.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Muerte/35.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Muerte/36.png").convert_alpha()]
    # jugador
    jugadorimg = [pygame.image.load("Nivel I/NaveSprite/1.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/2.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/3.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/4.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/5.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/6.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/7.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/8.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/9.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/10.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/11.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/12.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/13.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/14.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/15.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/16.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/17.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/18.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/19.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/20.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/21.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/22.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/23.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/24.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/25.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/26.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/27.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/28.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/29.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/30.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/31.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/32.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/33.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/34.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/35.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/36.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/37.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/38.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/39.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/40.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/41.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/42.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/43.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/44.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/45.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/46.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/47.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/48.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/49.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/50.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/51.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/52.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/53.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/54.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/55.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/56.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/57.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/58.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/59.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/60.png").convert_alpha(),
                ]
    especialimg = [pygame.image.load("Nivel I/NaveSprite/Bomba/1.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Bomba/2.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Bomba/3.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Bomba/4.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Bomba/5.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Bomba/6.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Bomba/7.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Bomba/8.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Bomba/9.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Bomba/10.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Bomba/11.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Bomba/12.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Bomba/13.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Bomba/14.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Bomba/15.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Bomba/16.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Bomba/17.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Bomba/18.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Bomba/19.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Bomba/20.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Bomba/21.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Bomba/22.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Bomba/23.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Bomba/24.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Bomba/25.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Bomba/26.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Bomba/27.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Bomba/28.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Bomba/29.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Bomba/30.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Bomba/31.png").convert_alpha()]
    misilimg = [pygame.image.load("Nivel I/NaveSprite/Misil/1.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Misil/2.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Misil/3.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Misil/4.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Misil/5.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Misil/6.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Misil/7.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Misil/8.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Misil/9.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Misil/10.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Misil/11.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Misil/12.png").convert_alpha(),
                pygame.image.load("Nivel I/NaveSprite/Misil/13.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Misil/14.png").convert_alpha()]

    spritevida = 0
    vidaimg = [pygame.image.load("Nivel I/NaveSprite/Vida/1.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Vida/2.png").convert_alpha(),
            pygame.image.load("Nivel I/NaveSprite/Vida/3.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Vida/4.png").convert_alpha(),
            pygame.image.load("Nivel I/NaveSprite/Vida/5.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Vida/6.png").convert_alpha(),
            pygame.image.load("Nivel I/NaveSprite/Vida/7.png").convert_alpha(), pygame.image.load("Nivel I/NaveSprite/Vida/8.png").convert_alpha()]
    torrecontrolimg = [pygame.image.load("Nivel I/TorreControl/1.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/2.png").convert_alpha(),
                    pygame.image.load("Nivel I/TorreControl/3.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/4.png").convert_alpha(),
                    pygame.image.load("Nivel I/TorreControl/5.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/6.png").convert_alpha(),
                    pygame.image.load("Nivel I/TorreControl/7.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/8.png").convert_alpha(),
                    pygame.image.load("Nivel I/TorreControl/9.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/10.png").convert_alpha()]

    # dialogo torre control
    dialogo1img = [pygame.image.load("Nivel I/TorreControl/1/1.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/1/2.png").convert_alpha(),
                pygame.image.load("Nivel I/TorreControl/1/3.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/1/4.png").convert_alpha(),
                pygame.image.load("Nivel I/TorreControl/1/5.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/1/6.png").convert_alpha(),
                pygame.image.load("Nivel I/TorreControl/1/7.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/1/8.png").convert_alpha(),
                pygame.image.load("Nivel I/TorreControl/1/9.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/1/10.png").convert_alpha(),
                pygame.image.load("Nivel I/TorreControl/1/11.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/1/12.png").convert_alpha(),
                pygame.image.load("Nivel I/TorreControl/1/13.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/1/14.png").convert_alpha(),
                pygame.image.load("Nivel I/TorreControl/1/15.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/1/16.png").convert_alpha(),
                pygame.image.load("Nivel I/TorreControl/1/17.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/1/18.png").convert_alpha(),
                pygame.image.load("Nivel I/TorreControl/1/19.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/1/20.png").convert_alpha(),
                pygame.image.load("Nivel I/TorreControl/1/21.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/1/22.png").convert_alpha(),
                pygame.image.load("Nivel I/TorreControl/1/22.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/1/24.png").convert_alpha(),
                pygame.image.load("Nivel I/TorreControl/1/25.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/1/26.png").convert_alpha(),
                pygame.image.load("Nivel I/TorreControl/1/27.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/1/28.png").convert_alpha(),
                pygame.image.load("Nivel I/TorreControl/1/29.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/1/30.png").convert_alpha(),
                pygame.image.load("Nivel I/TorreControl/1/31.png").convert_alpha(), pygame.image.load("Nivel I/TorreControl/1/32.png").convert_alpha(), ]
    spritetorrecontrol = 0
    dialogo1estado = True
    dialogo2estado = False
    dialogo3estado = False
    dialogo4estado = False

    dialogo1 = ['!','B', 'i', 'e', 'n', 'v', 'e', 'n', 'i', 'd', 'o', ' ', 'a', 'l', ' ', 'm', 'o', 'd', 'o', ' ', 'd', 'e', ' ', 'j', 'u', 'e', 'g', 'o',
                ' ', 'l', 'i', 'b', 'r', 'e', '!', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    dialogo2 = ['T', 'u', ' ', 'o', 'b','j', 'e', 't', 'i', 'v', 'o', ' ', 'e', 's', ' ', 'd', 'e', 's', 't', 'r', 'u', 'i', 'r', ' ', 'a', 'l', ' ', 'm', 'á', 'y', 'o', 'r',' ',
                'n', 'u', 'm', 'e', 'r', 'o', ' ', 'd', 'e', ' ' '', '', '', '', '', '' ,'', '', '', '', '', '','e', 'n', 'e', 'm', 'i','g', 'o', 's', ' ', 'y', ' ', 's', 'o', 'b', 'r', 'e', 'v', 'i', 'v', 'i', 'r',
                '.', '.', '.', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                '', '', '', '', '', '', '', '', '', '', '']
    dialogo3 = ['A', ' ', 'm', 'e', 'd', 'i', 'd', 'a', ' ', 'q', 'u', 'e', ' ', 'a', 'v', 'a', 'n', 'c', 'e', 's', ' ', 's', 'u', 'b', 'i', 'r', 'a', ' ', 'l', 'a', ' ', 'd', 'i', 'f', 'i', 'c',
                'u', 'l', 't', 'a', 'd', '', '', '', '', '', '', '', '', '', '', '', '',' ', '!', 'T', 'e', 'n', ' ', 'c', 'u', 'i', 'd', 'a','d', 'o', '!', '', '', '', '',
                '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                '', '', '', '', '', '','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    dialogo4 = ['A', 't', 'a', 'q', 'u', 'e', ' ', 'b', 'á', 's', 'i', 'c', 'o', ':', ' ', 'M', 'i', 's', 'i', 'l', ' ', '(', 'T', 'e', 'c', 'l', 'a', ' ', 'e', 's', 'p', 'a', 'c', 'i', 'o',')','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                'A', 't', 'a', 'q', 'u','e', ' ', 'e', 's', 'p', 'e', 'c', 'i', 'a', 'l', ':', ' ', 'B', 'o', 'm', 'b', 'a', ' ', '(', 'T', 'e', 'c', 'l', 'a', ' ', 'E', ')', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '','', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

    linea1 = ''
    linea2 = ''
    contadordialogo = 0
    linea1img = fuentedialogo.render(linea1, True, (0, 255, 0))
    linea2img = fuentedialogo.render(linea2, True, (0, 255, 0))
    escribiendosonidoestado = "listo"


    def fondo():
        global fondo1x
        global fondo2x
        global cmisiles
        global spritegameover
        global nombreimg
        global jugadorx
        global jugadorestado
        global cbombas
        global eliminaciones
        
        fondo1x -= 2
        fondo2x -= 2
        if fondo1x <= -2560:
            fondo1x = 2560
        if fondo2x <= -2560:
            fondo2x = 2560

        screen.blit(fondo1, (fondo1x, 0))
        screen.blit(fondo1, (fondo2x, 0))
        # Barra estado
        screen.blit(barraestado, (0, 648))
        if recargandomisil == "no":
            screen.blit(municionmisilimg[cmisiles], (25, 685))
        if recargandobomba == "no":
            screen.blit(municionbombaimg[cbombas], (250, 685))
        puntajeimg = texto.render("Puntaje: " + str(puntaje), True, (255, 255, 255))
        eliminacionesimg = texto.render("Eliminaciones: "+str(eliminaciones), True, (255, 255, 255))
        screen.blit(puntajeimg, (380, 657))
        screen.blit(vidaimg[spritevida], (25, 657))
        screen.blit(nombreimg, (25, 25))
        screen.blit(eliminacionesimg, (380, 690))

        if not jugadorestado:
            screen.blit(gameoverimg[int(spritegameover)], (0, 0))
            screen.blit(puntajeimg, (450, 500))
            screen.blit(eliminacionesimg, (450, 550))
            if spritegameover < 10:
                spritegameover += 0.5
            else:
                spritegameover += 0


    def dialogo():
        global linea1
        global linea2
        global dialogo1estado
        global dialogo2estado
        global dialogo3estado
        global dialogo4estado
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
        global jugadorestado

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
                dialogo4estado = True
                contadordialogo = 0
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
                for i in range(0, nenemigos2):
                    helicopteromovy[i] = random.randint(-3, 3)
                    helicopteromovx[i] = random.randint(1, 2)
                for i in range(0, nenemigos1):
                    tanquemovx[i] = random.randint(1, 5)


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
        elif jugadorx >= 1240:
            jugadormovx = 0
            jugadorx = 1240

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
        global recargandobomba
        global tanquex
        global tanquey
        global nenemigos1
        global bombaestado
        global tanqueestado
        global spritetanque
        global puntaje
        global recargandobomba
        global spriterecargabomba
        global spritemunicionbomba
        global eliminaciones
        global reaparicion
        
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
                            eliminaciones += 1
                            spritetanque[j] = 29
                            puntaje += 2000
                            reaparicion = True

            if bombaestado[i] == "explosion":
                if spritebomba[i] >= 30:
                    bombaestado[i] = "nolisto"
                else:
                    spritebomba[i] += 0.5
                    screen.blit(especialimg[int(spritebomba[i])], (bombax[i] - 40, bombay[i] - 60))

            if bombaestado[i] == "nolisto":
                bombax[i] = 0
                bombay[i] = 0


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
        global spritebomba
        
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
    nenemigos1 = 1
    nenemigos2 = 1
    misilhelicopteroimg = [pygame.image.load("Nivel I/Enemigo2/Misil/1.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Misil/2.png").convert_alpha(),
                        pygame.image.load("Nivel I/Enemigo2/Misil/3.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Misil/4.png").convert_alpha(),
                        pygame.image.load("Nivel I/Enemigo2/Misil/5.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Misil/6.png").convert_alpha(),
                        pygame.image.load("Nivel I/Enemigo2/Misil/7.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Misil/8.png").convert_alpha(),
                        pygame.image.load("Nivel I/Enemigo2/Misil/9.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Misil/10.png").convert_alpha(),
                        pygame.image.load("Nivel I/Enemigo2/Misil/11.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Misil/12.png").convert_alpha(),
                        pygame.image.load("Nivel I/Enemigo2/Misil/13.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Misil/14.png").convert_alpha(),
                        pygame.image.load("Nivel I/Enemigo2/Misil/15.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Misil/16.png").convert_alpha(),
                        pygame.image.load("Nivel I/Enemigo2/Misil/14.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Misil/18.png").convert_alpha(),
                        pygame.image.load("Nivel I/Enemigo2/Misil/19.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Misil/20.png").convert_alpha(),
                        pygame.image.load("Nivel I/Enemigo2/Misil/21.png").convert_alpha()]
    helicopteroimg = [pygame.image.load("Nivel I/Enemigo2/1.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/2.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/3.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/4.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/5.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/6.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/7.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/8.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/9.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/10.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/11.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/12.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/13.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/14.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/15.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/16.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/14.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/18.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/19.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/20.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/21.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/22.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/23.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/24.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/25.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/26.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/27.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/28.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/29.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/30.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/31.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/32.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/33.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/34.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/35.png").convert_alpha()]
    helicopteroimg1 = [pygame.image.load("Nivel I/Enemigo2/Daño1/1.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño1/2.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño1/3.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño1/4.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño1/5.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño1/6.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño1/7.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño1/8.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño1/9.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño1/10.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño1/11.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño1/12.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño1/13.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño1/14.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño1/15.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño1/16.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño1/14.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño1/18.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño1/19.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño1/20.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño1/21.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño1/22.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño1/23.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño1/24.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño1/25.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño1/26.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño1/27.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño1/28.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño1/29.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño1/30.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño1/31.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño1/32.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño1/33.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño1/34.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño1/35.png").convert_alpha()]
    helicopteroimg2 = [pygame.image.load("Nivel I/Enemigo2/Daño2/1.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño2/2.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño2/3.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño2/4.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño2/5.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño2/6.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño2/7.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño2/8.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño2/9.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño2/10.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño2/11.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño2/12.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño2/13.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño2/14.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño2/15.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño2/16.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño2/14.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño2/18.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño2/19.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño2/20.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño2/21.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño2/22.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño2/23.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño2/24.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño2/25.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño2/26.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño2/27.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño2/28.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño2/29.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño2/30.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño2/31.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño2/32.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño2/33.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño2/34.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño2/35.png").convert_alpha()]
    helicopteroimg3 = [pygame.image.load("Nivel I/Enemigo2/Daño3/1.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño3/2.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño3/3.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño3/4.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño3/5.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño3/6.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño3/7.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño3/8.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño3/9.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño3/10.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño3/11.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño3/12.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño3/13.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño3/14.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño3/15.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño3/16.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño3/14.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño3/18.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño3/19.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño3/20.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño3/21.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño3/22.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño3/23.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño3/24.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño3/25.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo2/Daño3/26.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo2/Daño3/27.png").convert_alpha()]
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
        helicopteromovy.append(0)
        helicopteromovx.append(0)
        helicopteroestado.append(True)
        cdaño.append(0)
        misilhelicopterox.append(0)
        misilhelicopteroy.append(0)
        misilhelicopteroestado.append("listo")

    humoimg = [pygame.image.load("Nivel I/Enemigo/Humo/1.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Humo/2.png").convert_alpha(),
            pygame.image.load("Nivel I/Enemigo/Humo/3.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Humo/4.png").convert_alpha(),
            pygame.image.load("Nivel I/Enemigo/Humo/5.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Humo/6.png").convert_alpha(),
            pygame.image.load("Nivel I/Enemigo/Humo/7.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Humo/8.png").convert_alpha(),
            pygame.image.load("Nivel I/Enemigo/Humo/9.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Humo/10.png").convert_alpha(),
            pygame.image.load("Nivel I/Enemigo/Humo/11.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Humo/12.png").convert_alpha(),
            pygame.image.load("Nivel I/Enemigo/Humo/13.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Humo/14.png").convert_alpha()]
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
        global eliminaciones
        global reaparicion
        
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
                    helicopteroestado[i] = True
                    helicopterox[i] = random.randint(1280, 2000)
                    helicopteroy[i] = random.randint(0, 550)
                    eliminaciones += 1
                    reaparicion = True
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


    tanqueiimg = [pygame.image.load("Nivel I/Enemigo/Izquierda/1.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/2.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/3.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/4.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/5.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/6.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/7.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/8.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/9.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/10.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/11.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/12.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/13.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/14.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/15.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/16.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/17.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/18.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/19.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/20.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/21.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/22.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/23.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/24.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/25.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/26.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/27.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/28.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/29.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/30.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/31.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/32.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/33.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/34.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/35.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/36.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/37.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/38.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/39.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/40.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/41.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/42.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/43.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/44.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/45.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/46.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/47.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/48.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/49.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/50.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/51.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Izquierda/52.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Izquierda/53.png").convert_alpha()]
    tanquedimg = [pygame.image.load("Nivel I/Enemigo/Derecha/1.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/2.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/3.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/4.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/5.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/6.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/7.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/8.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/9.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/10.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/11.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/12.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/13.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/14.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/15.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/16.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/17.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/18.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/19.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/20.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/21.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/22.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/23.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/24.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/25.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/26.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/27.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/28.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/29.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/30.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/31.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/32.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/33.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/34.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/35.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/36.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/37.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/38.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/39.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/40.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/41.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/42.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/43.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/44.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/45.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/46.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/47.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/48.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/49.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/50.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/51.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/Derecha/52.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/Derecha/53.png").convert_alpha()]
    cambiodiimg = [pygame.image.load("Nivel I/Enemigo/CambioDI/1.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/CambioDI/2.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/CambioDI/3.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/CambioDI/4.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/CambioDI/5.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/CambioDI/6.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/CambioDI/7.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/CambioDI/8.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/CambioDI/9.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/CambioDI/10.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/CambioDI/11.png").convert_alpha()]
    cambioidimg = [pygame.image.load("Nivel I/Enemigo/CambioID/1.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/CambioID/2.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/CambioID/3.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/CambioID/4.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/CambioID/5.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/CambioID/6.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/CambioID/7.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/CambioID/8.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/CambioID/9.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/CambioID/10.png").convert_alpha(),
                pygame.image.load("Nivel I/Enemigo/CambioID/11.png").convert_alpha()]
    tanquemisiliimg = [pygame.image.load("Nivel I/Enemigo/MisilI/1.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilI/2.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilI/3.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilI/4.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilI/5.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilI/6.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilI/7.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilI/8.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilI/9.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilI/10.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilI/11.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilI/12.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilI/13.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilI/14.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilI/15.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilI/16.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilI/14.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilI/18.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilI/19.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilI/20.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilI/21.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilI/22.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilI/23.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilI/24.png").convert_alpha()]
    tanquemisildimg = [pygame.image.load("Nivel I/Enemigo/MisilD/1.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilD/2.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilD/3.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilD/4.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilD/5.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilD/6.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilD/7.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilD/8.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilD/9.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilD/10.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilD/11.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilD/12.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilD/13.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilD/14.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilD/15.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilD/16.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilD/14.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilD/18.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilD/19.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilD/20.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilD/21.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilD/22.png").convert_alpha(),
                    pygame.image.load("Nivel I/Enemigo/MisilD/23.png").convert_alpha(), pygame.image.load("Nivel I/Enemigo/MisilD/24.png").convert_alpha()]
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
        global eliminaciones

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
    canalpausa.set_volume(0.3)
    canalpausa.play(Spausa,-1)
    canalpausa.pause()
    canal3.play(helicopterosonido,loops=-1)
    # juego
    Pausa = False
    reaparicion = True
    jugando = True
    lvl2 = True

    while jugando:

        if lvl2:
            canal17.set_volume(0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    jugando = False
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        jugadormovy1 = -8
                    if event.key == pygame.K_s:
                        jugadormovy = 8
                    if event.key == pygame.K_a:
                        jugadormovx1 = -8
                    if event.key == pygame.K_d:
                        jugadormovx = 8
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
                            if bombaestado[cbombas] == "listo":
                                canal1.play(bombasonido)
                                bombaestado[cbombas] = "disparando"
                                bombax[cbombas] = jugadorx
                                bombay[cbombas] = jugadory
                                cbombas += 1
                    if event.key == pygame.K_ESCAPE:
                        if not Pausa:
                            Pausa = True
                            canalpausa.unpause()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        jugadormovy1 = 0
                    if event.key == pygame.K_a:
                        jugadormovx1 = 0
                    if event.key == pygame.K_s:
                        jugadormovy = 0
                    if event.key == pygame.K_d:
                        jugadormovx = 0
                    if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                        if dialogo1estado:
                            contadordialogo = len(dialogo1) - 1
                        if dialogo2estado:
                            contadordialogo = len(dialogo2) - 1
                        if dialogo3estado:
                            contadordialogo = len(dialogo3) - 1
                        if dialogo4estado:
                            contadordialogo = len(dialogo4) - 1

                    if not jugadorestado:
                        if int(score)<puntaje:
                            info = open(text+".txt", "w")
                            info.close()
                            info = open(text+".txt", "a")
                            info.write(nombre+"\n")
                            info.write(punt+"\n")
                            info.write(niv+"\n")
                            info.write(str(puntaje))
                            info.close()
                        puntaje=0
                        eliminaciones=0
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

                        for i in range(0, bombas):
                            bombax[i] = 0
                            bombay[i] = 0
                            bombaestado[i] = "listo"
                            spritebomba[i] = 0

                        spritegameover = 0
                        jugadorestado = True

            if eliminaciones % 10 == 0 and eliminaciones != 0 and reaparicion:
                tanqueestado.append(True)
                tanquex.append(random.randint(1280, 1599))
                tanquemovx.append(random.randint(1, 5))
                tanquemisilestado.append("listo")
                tanquemisilx.append(0)
                tanquemisily.append(720)
                cambiodiestado.append(False)
                cambioidestado.append(False)
                tanquedireccion.append("izquierda")
                spritecambio.append(0)
                tanquemisilmovx.append(0)
                tanquemisilmovy.append(0)
                spritetanque.append(0)
                tanquemisila.append(False)
                nenemigos1 += 1
                reaparicion = False

            if eliminaciones % 5 == 0 and eliminaciones != 0 and reaparicion:
                helicopterox.append(random.randint(1280, 1599))
                helicopteroy.append(random.randint(0, 550))
                helicopteromovy.append(random.randint(2, 5))
                helicopteromovx.append(-random.randint(2, 5))
                helicopteroestado.append(True)
                cdaño.append(0)
                misilhelicopterox.append(0)
                misilhelicopteroy.append(0)
                misilhelicopteroestado.append("listo")
                nenemigos2 += 1
                reaparicion = False

            fondo()
            if jugadorestado:
                tanque()
                misiltanque()
                misil()
                recargamisil()
                recargabomba()
                corazon()
                helicoptero()
                misilhelicoptero()
                bomba()
                jugador()
                amuerte()
                dialogo()


            #Pausa
            while Pausa:
                menu = Cinematica_1_1.pause()
                Pausa=False
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
                    return True
                pygame.display.update()
            
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