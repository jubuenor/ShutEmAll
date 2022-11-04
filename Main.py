import pygame as p
import numpy as np
from pygame import mixer
import random as r
import Nivel_1
import Nivel_2
import Nivel_3
import Nivel_4
import Nivel_I
import Cinematica_1_1
Save=open("1.txt","r")
nombre1=Save.readline().replace('\n',"")
score1=Save.readline().replace('\n',"")
nivel1=Save.readline().replace('\n',"")
scorei1=Save.readline().replace('\n',"")
Save.close()
Save=open("2.txt","r")
nombre2=Save.readline().replace('\n',"")
score2=Save.readline().replace('\n',"")
nivel2=Save.readline().replace('\n',"")
scorei2=Save.readline().replace('\n',"")
Save.close()
Save=open("3.txt","r")
nombre3=Save.readline().replace('\n',"")
score3=Save.readline().replace('\n',"")
nivel3=Save.readline().replace('\n',"")
scorei3=Save.readline().replace('\n',"")
Save.close()
nombres=[nombre1,nombre2,nombre3]
scores=[score1,score2,score3]
nivelesg=[nivel1,nivel2,nivel3]
scoresi=[scorei1,scorei2,scorei3]
Load=open("Guardado.txt","r")
text=int(Load.readline())
Load.close()
p.init()
Icono = p.image.load('Imagenes\\Icono.png')
p.display.set_icon(Icono)
x=1280
y=720
#Fuentes
fonttext2=p.font.Font('Fuentes\\Timeless-Bold.ttf',15)
font=p.font.Font("Fuentes\\Coalition_v2.ttf",100)
font1=p.font.Font("Fuentes\\Open 24 Display St.ttf",30)
#Sonidos
mixer.music.load("Sonidos\\MyVeryOwnDeadShip.ogg")
Balas=mixer.Sound("Sonidos\\Bala.wav")
tap=mixer.Sound("Sonidos\\boton_tap.wav")
canalbala=mixer.Channel(0)
canaltap=mixer.Channel(1)
k1,k2,k3=0,0,0
countsonido=0
mixer.music.play(-1)
#Opciones
select=[False,False,False]
MH="Modo Historia "
Reset="Reiniciar"
ML="Modo Libre "
S="Salir "
Jugar=font1.render("Jugar",True,(255,255,255))
salir=font1.render("Salir",True,(255,255,255))
k1s,k2s,k3s=0,0,0
def opciones(k1,k2,k3,a=False):
    if not a:
        op1=font1.render(MH,True,(255,255,255))
        op1l=font1.render(MH[0:k1],True,(0,255,0))
        j=0
    else:
        j=1
        op1=font1.render(Reset,True,(255,255,255))
        op1l=font1.render(Reset[0:k1],True,(0,255,0))
    cop1=op1.get_rect(center=(int(x/2-93-45*j),int(y/2)))
    op2=font1.render(ML,True,(255,255,255))
    cop2=op2.get_rect(center=(int(x/2-110),int(y/2+100)))
    op3=font1.render(S,True,(255,255,255))
    cop3=op3.get_rect(center=(int(x/2-150),int(y/2+200))) 
    op2l=font1.render(ML[0:k2],True,(0,255,0))
    op3l=font1.render(S[0:k3],True,(0,255,0))
    pantalla.blit(op1,cop1)
    pantalla.blit(op2,cop2)
    pantalla.blit(op3,cop3)
    pantalla.blit(op1l,cop1)
    pantalla.blit(op2l,cop2)
    pantalla.blit(op3l,cop3)
pantalla = p.display.set_mode((x,y))
p.display.set_caption("Shut 'em all")
class Img:
    def __init__(self,a):
        self.ubicacion=a
    def img(self):
        return p.image.load("Imagenes\\"+self.ubicacion).convert_alpha()
fondo=[Img("0.png").img(),Img("1.png").img(),Img("2.png").img()]
count_Fondo=2
#Coup
Coup=Img("T.png").img()
#Botones
arrow=p.image.load("Imagenes\\arrow.png")
ang=0
xr,yr=np.zeros(20),np.zeros(20)
tetha=0
dang=2
nombre=nombres[text-1]
escotilla=[]
for i in range(10):
    escotilla.append(Img("Escotilla\\Esctilla"+str(i)+".png").img())
basura=Img("Escotilla\\B.png").img()
xes=[int(x/2-200),int(x/2),int(x/2+200)]
selectesc=[False,False,False]
selectesc[text-1]=True
countesc=[0,0,0]
def name(k=[9,9,9]):
    global y
    global text
    Titulo=font.render("Shut 'em all",True,(255,255,255))
    ctitulo=Titulo.get_rect(center=(int(x/2),100))
    for i in range(3):
        if i==text-1:
            nom=fonttext2.render(nombre,True,(255,255,255))
            cnom=nom.get_rect(center=(xes[text-1],int(y/2-170)))
        else:
            nom=fonttext2.render(nombres[i],True,(255,255,255))
            cnom=nom.get_rect(center=(xes[i],int(y/2-170)))
        cb=basura.get_rect(center=(xes[i],int(y/2-65)))
        por=fonttext2.render(str(25*int(nivelesg[i]))+"%",True,(255,255,255))
        cpor=por.get_rect(center=(xes[i],int(y/2-145)))
        cent=escotilla[k[i]].get_rect(center=(xes[i],int(y/2-150)))
        p.draw.rect(pantalla,(0,0,0),(xes[i]-55,int(y/2-205),110,110))
        pantalla.blit(nom,cnom)
        pantalla.blit(por,cpor)
        p.draw.rect(pantalla,(255,255,255),(xes[i]-30,int(y/2-130),60,7))
        p.draw.rect(pantalla,(0,255,0),(xes[i]-30,int(y/2-130),int(int(nivelesg[i])*25*60/100),7))
        pantalla.blit(escotilla[k[i]],cent)
        pantalla.blit(basura,cb)
    pantalla.blit(Titulo,ctitulo)
Boton=Img("Boton.png").img()
#Mostrar
def mostrar(x,y,im,a=0,t=1):
    img=p.transform.rotozoom(im,a,t)
    centro=img.get_rect(center=(int(x),int(y)))
    pantalla.blit(img,centro)
Nave=[]
k=0
for i in range(1,61):
    ub="NaveSprite\\"
    ub+=str(i)+".png"
    im=Img(ub)
    Nave.append(im.img())
p.mouse.set_visible(0)
niveles=[False,False,False,False,False]
puntaje=False
win=False
Run=True
mx,my=p.mouse.get_pos()
while Run:
    mx,my=p.mouse.get_pos()
    p.time.Clock().tick(60)
    for event in p.event.get():
        if event.type== p.QUIT:
            Run=False
        if event.type == p.KEYDOWN:
            if nombre=="Nombre":
                nombre=""
            if event.key == p.K_BACKSPACE:
                nombre=nombre[:-1]
            else:
                if len(nombre)<=6:
                    nombre+=event.unicode
        if event.type == p.MOUSEBUTTONDOWN:
            if event.button==1:
                if 710<=mx<=877 and 336<=my<=377:
                    select[0]=True
                    if nombre!=nombres[text-1]:
                        Save=open(str(text)+".txt","w")
                        Save.close()
                        Save=open(str(text)+".txt","a")
                        Save.write(nombre+"\n")
                        Save.write(str(scores[text-1])+"\n")
                        Save.write(str(nivelesg[text-1])+"\n")
                        Save.write(str(scoresi[text-1])+"\n")
                        Save.close()
                elif 710<=mx<=877 and 436<=my<=477:
                    select[1]=True
                    if nombre!=nombres[text-1]:
                        Save=open(str(text)+".txt","w")
                        Save.close()
                        Save=open(str(text)+".txt","a")
                        Save.write(nombre+"\n")
                        Save.write(str(scores[text-1])+"\n")
                        Save.write(str(nivelesg[text-1])+"\n")
                        Save.write(str(scoresi[text-1])+"\n")
                        Save.close()
                elif 710<=mx<=877 and 536<=my<=577:
                    select[2]=True
                if 145<=my<=268:
                    if 381<=mx<=497: 
                        selectesc=[True,False,False]
                        text=1
                        nombre=nombres[0]
                    elif 581<=mx<=697:
                        text=2
                        nombre=nombres[1]
                        selectesc=[False,True,False]
                    elif 781<=mx<=897:
                        text=3
                        nombre=nombres[2]
                        selectesc=[False,False,True]
                if 13<my<87 and 1193<mx<1264:
                    puntaje=True
                    Save=open("1.txt","r")
                    nombre1=Save.readline().replace('\n',"")
                    score1=Save.readline().replace('\n',"")
                    nivel1=Save.readline().replace('\n',"")
                    scorei1=Save.readline().replace('\n',"")
                    Save.close()
                    Save=open("2.txt","r")
                    nombre2=Save.readline().replace('\n',"")
                    score2=Save.readline().replace('\n',"")
                    nivel2=Save.readline().replace('\n',"")
                    scorei2=Save.readline().replace('\n',"")
                    Save.close()
                    Save=open("3.txt","r")
                    nombre3=Save.readline().replace('\n',"")
                    score3=Save.readline().replace('\n',"")
                    nivel3=Save.readline().replace('\n',"")
                    scorei3=Save.readline().replace('\n',"")
                    Save.close()
                    nombres=[nombre1,nombre2,nombre3]
                    scores=[score1,score2,score3]
                    nivelesg=[nivel1,nivel2,nivel3]
                    scoresi=[scorei1,scorei2,scorei3]
                if 272<=my<=311:
                    if 424<mx<454:
                        Save=open(str(1)+".txt","w")
                        Save.close()
                        Save=open(str(1)+".txt","a")
                        Save.write("Nombre"+"\n")
                        Save.write(str(0)+"\n")
                        Save.write(str(0)+"\n")
                        Save.write(str(0)+"\n")
                        Save.close()
                        nombre="Nombre"
                        print("Erase1")
                    elif 624<mx<654:
                        Save=open(str(2)+".txt","w")
                        Save.close()
                        Save=open(str(2)+".txt","a")
                        Save.write("Nombre"+"\n")
                        Save.write(str(0)+"\n")
                        Save.write(str(0)+"\n")
                        Save.write(str(0)+"\n")
                        Save.close()
                        nombre="Nombre"
                        print("Erase2")
                        print(mx,my)
                    elif 824<mx<854:
                        Save=open(str(3)+".txt","w")
                        Save.close()
                        Save=open(str(3)+".txt","a")
                        Save.write("Nombre"+"\n")
                        Save.write(str(0)+"\n")
                        Save.write(str(0)+"\n")
                        Save.write(str(0)+"\n")
                        Save.close()
                        nombre="Nombre"
                        print("Erase3")
                    Save=open("1.txt","r")
                    nombre1=Save.readline().replace('\n',"")
                    score1=Save.readline().replace('\n',"")
                    nivel1=Save.readline().replace('\n',"")
                    scorei1=Save.readline().replace('\n',"")
                    Save.close()
                    Save=open("2.txt","r")
                    nombre2=Save.readline().replace('\n',"")
                    score2=Save.readline().replace('\n',"")
                    nivel2=Save.readline().replace('\n',"")
                    scorei2=Save.readline().replace('\n',"")
                    Save.close()
                    Save=open("3.txt","r")
                    nombre3=Save.readline().replace('\n',"")
                    score3=Save.readline().replace('\n',"")
                    nivel3=Save.readline().replace('\n',"")
                    scorei3=Save.readline().replace('\n',"")
                    Save.close()
                    nombres=[nombre1,nombre2,nombre3]
                    scores=[score1,score2,score3]
                    nivelesg=[nivel1,nivel2,nivel3]
                    scoresi=[scorei1,scorei2,scorei3]
    mostrar(x/2,y/2,fondo[int(count_Fondo)])
    p.draw.rect(pantalla,(0,0,0),(int(x/2-245),int(y/2+175),50,50))
    p.draw.rect(pantalla,(0,0,0),(int(x/2-245),int(y/2+75),50,50))
    p.draw.rect(pantalla,(0,0,0),(int(x/2-245),int(y/2-25),50,50))
    mostrar(x/2-220,y/2,Nave[int(k)],0,0.5)
    mostrar(x/2-220,y/2+200,arrow,ang,1)
    mostrar(x/2,y/2,Boton)
    mostrar(x/2,y/2+100,Boton)
    mostrar(x/2,y/2+200,Boton)
    for i in range(6):
        xr[i]=15*np.sqrt(2)*np.cos(tetha-0.5*i)/(np.sin(tetha-0.5*i)**2+1)
        yr[i]=15*np.sqrt(2)*np.sin(tetha-0.5*i)*np.cos(tetha-0.5*i)/(np.sin(tetha-0.5*i)**2+1)
        p.draw.circle(pantalla,(0,255,0), (int(xr[i])+int(x/2-220),int(yr[i])+int(y/2+100)), 2, 0)
    if tetha>-4*np.pi:
        tetha-=0.3
    else:
        tetha=0
    if ang>10:
        dang*=-1
    elif ang<-10:
        dang*=-1
    ang+=dang
    name(countesc)
    for i in range(3):
        if selectesc[i]:
            if countesc[i]<9:
                countesc[i]+=1
        else:
            if countesc[i]>0:
                countesc[i]-=1

    if 710<=mx<=877 and 336<=my<=377:
        pantalla.blit(Jugar,(760,int((377+336)/2-15)))
        if k1<len(MH):
            k1+=1
        else:
            k1=0
        if k1s==0:
            canaltap.play(tap)
            k1s=1
    else:
        k1,k1s=0,0
    if 710<=mx<=877 and 436<=my<=477:
        pantalla.blit(Jugar,(760,int((477+436)/2-15)))
        if k2<len(ML):
            k2+=0.8
        else:
            k2=0
        if k2s==0:
            canaltap.play(tap)
            k2s=1
    else:
        k2,k2s=0,0
    if 710<=mx<=877 and 536<=my<=577:
        pantalla.blit(salir,(768,int((577+536)/2-15)))
        if k3<len(S):
            k3+=0.5
        else:
            k3=0
        if k3s==0:
            canaltap.play(tap)
            k3s=1
    else:
        k3,k3s=0,0
    if puntaje:
        Cinematica_1_1.puntos()
        puntaje=False
    if select[2]:
        if countsonido<15:
            canalbala.play(Balas)
            countsonido+=1
        else:
            countsonido=0
            select[2]=False
            Run=False        
    elif select[0]:
        if countsonido<15:
            canalbala.play(Balas)
            countsonido+=1
        else:
            countsonido=0
            Save=open("Guardado.txt","w")
            Save.write(str(text))
            Save.close()
            Save=open(str(text)+".txt","r")
            nombre1=Save.readline().replace('\n',"")
            score=Save.readline().replace('\n',"")
            nivel=Save.readline().replace('\n',"")
            Save.close()
            niveles=[False,False,False,False,False]
            for i in range(4):
                if int(nivel)<=4:
                    niveles[int(nivel)]=True
            if niveles[0]:
                pantalla.fill((0,0,0))
                p.display.flip()
                mixer.music.pause()
                Run,win=Nivel_1.niv_1()
                if win and Run:
                    niveles[1]=True
                    niveles[0]=False
                    win=False
            if niveles[1]:
                pantalla.fill((0,0,0))
                p.display.flip()
                mixer.music.pause()
                Run,win=Nivel_2.niv_2()
                if win and Run:
                    niveles[2]=True
                    niveles[1]=False
                    win=False
            if niveles[2]:
                pantalla.fill((0,0,0))
                p.display.flip()
                mixer.music.pause()
                Run,win=Nivel_3.niv_3()
                if win and Run:
                    niveles[3]=True
                    niveles[2]=False
                    win=False
            if niveles[3]:
                pantalla.fill((0,0,0))
                p.display.flip()
                mixer.music.pause()
                Run,win=Nivel_4.niv_4()
                if win and Run:
                    niveles[3]=False
                    niveles[4]=True
                    win=False
            elif niveles[4]:
                Save=open(str(text)+".txt","w")
                Save.write(nombre+'\n')
                Save.write(str(0)+'\n')
                Save.write(str(0)+"\n")
                Save.write(str(scoresi[text-1]))
                Save.close()
                Save=open(str(text)+".txt","r")
                nombre1=Save.readline().replace('\n',"")
                score=Save.readline()
                nivel=Save.readline()
                Save.close()
                niveles[4]=False
                niveles[0]=True
            if not Run:
                break    
            else:
                Icono = p.image.load('Imagenes\\Icono.png')
                p.display.set_icon(Icono)
                Save=open("1.txt","r")
                nombre1=Save.readline().replace('\n',"")
                score1=Save.readline().replace('\n',"")
                nivel1=Save.readline().replace('\n',"")
                scorei1=Save.readline().replace('\n',"")
                Save.close()
                Save=open("2.txt","r")
                nombre2=Save.readline().replace('\n',"")
                score2=Save.readline().replace('\n',"")
                nivel2=Save.readline().replace('\n',"")
                scorei2=Save.readline().replace('\n',"")
                Save.close()
                Save=open("3.txt","r")
                nombre3=Save.readline().replace('\n',"")
                score3=Save.readline().replace('\n',"")
                nivel3=Save.readline().replace('\n',"")
                scorei3=Save.readline().replace('\n',"")
                Save.close()
                nombres=[nombre1,nombre2,nombre3]
                scores=[score1,score2,score3]
                nivelesg=[nivel1,nivel2,nivel3]
                scoresi=[scorei1,scorei2,scorei3]
                mixer.music.load("Sonidos\\MyVeryOwnDeadShip.ogg")
                mixer.music.play()      
            select[0]=False
    elif select[1]:
        mixer.music.pause()
        if countsonido<15:
            canalbala.play(Balas)
            countsonido+=1
        else:
            Save=open("Guardado.txt","w")
            Save.write(str(text))
            Save.close()
            countsonido=0
            Run=Nivel_I.niv_I()
            select[1]=False
        if not Run:
            break
        else:
            Icono = p.image.load('Imagenes\\Icono.png')
            p.display.set_icon(Icono)
            mixer.music.load("Sonidos\\MyVeryOwnDeadShip.ogg")
            mixer.music.play()
    Save=open("Guardado.txt","w")
    Save.write(str(text))
    Save.close()
    Save=open(str(text)+".txt","r")
    nombre1=Save.readline().replace('\n',"")
    score=Save.readline().replace('\n',"")
    nivel=Save.readline().replace('\n',"")
    Save.close()
    niveles=[False,False,False,False,False]
    for i in range(4):
        if int(nivel)<=4:
            niveles[int(nivel)]=True 
    opciones(int(k1),int(k2),int(k3),niveles[4])
    if k<len(Nave)-1:
        k+=1
    else:
        k=0
    mostrar(1230,50,Coup)
    mostrar(mx+15,my+15,Nave[int(k)],135,0.5)
    p.display.update()