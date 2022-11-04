import random as r
import math as m
import numpy as np
import pygame as p
from pygame import mixer
import sys
p.init()
mixer.init()
def trans():    
    Save=open("Guardado.txt","r")
    text=int(Save.readline())
    Save.close()
    Save=open(str(text)+".txt","r")
    nombre=Save.readline().replace('\n',"")
    Save.close()
    x,y=1280,720
    pantalla=p.display.set_mode((x,y))
    Icono = p.image.load('Nivel 4\\Imagenes\\Icono.png')
    p.display.set_icon(Icono)
    fondo=p.image.load("Nivel 4\\Imagenes\\Transicion.png").convert()
    p.display.set_caption("Shut 'em all")
    font=p.font.Font('Nivel 4\\Fuentes\\Open 24 Display St.ttf',30)
    xf0=1280/2
    xf1=1280/2+1280
    def mostrartext(texto,k,x,y,c=[1,1,1]):
        t=font.render(texto[0:int(k)],True,(c[0]*255,c[1]*255,c[2]*255))
        pantalla.blit(t,(int(x),int(y)))
    def mostrar(x,y,img,a=0,j=1):
        im=p.transform.rotozoom(img,a,j)
        centro=im.get_rect(center=(int(x),int(y)))
        pantalla.blit(im,centro)
    
    #Dialogos
    Dialogo0=["Muy bien hecho "+nombre+", a pesar de tu buen trabajo los sistemas de la nave", "han quedado destruidos."]
    Dialogo1=["Gracias a tu última misión, hemos conseguido muchísima información, a pesar de", "los civiles con los que acabaste."]
    Dialogo2=["No hay tiempo para lamentarse "+nombre+" debemos continuar acabando con todos", "nuestros enemigos."] 
    Dialogo3=["Por orden del general Riube, debes acabar con un extraño ejercito, según", "nuestras fuentes tienen varios lideres con los cuales debes acabar."]
    Dialogo4=["Ten cuidado, nuestros recursos son bastante límitados, te hemos dado una  bomba", "gravitacional, solo la puedes usar de forma límitada, así que usala con sabiduría."]
    Dialogo5=["Puedes cambiar la gravedad de esta usando la tecla 'e'.",""]
    Dialogo6=["Sin embargo, aún tienes tus disparos, sólo uno como antes, no ha siido posible", "arreglar tu sistema de defensa, lo sentimos."]
    Dialogo7=["Contamos contigo "+nombre+"...",""]
    k1,k2=0,0
    saltar=False
    continuar=['Presiona "enter"',"Para continuar."]
    col=0
    Dialogos=[Dialogo0,Dialogo1,Dialogo2,Dialogo3,Dialogo4,Dialogo5,Dialogo6,Dialogo7]
    n=0

    #señora :v
    Senora=[]
    counts=0
    xr,yr=0,0
    for i in range(10):
        Senora.append(p.image.load("Nivel 4\\Imagenes\\TorreControl\\"+str(i+1)+".png").convert_alpha())

    #Nave
    Nave=[]
    k=0
    xp,yp,t=0,y/2,0
    for i in range(1,61):
        Nave.append(p.image.load("Nivel 4\\Imagenes\\Navesprite\\"+str(i)+".png").convert_alpha())
    Run=True
    while Run:
        p.time.Clock().tick(60)
        for event in p.event.get():
            if event.type== p.QUIT:
                Run=False
                sys.exit()
            if event.type==p.KEYDOWN:
                if event.key==p.K_RETURN:
                    if saltar:
                        n+=1
                        k1,k2=0,0
                        saltar=False
                    else:
                        saltar=True
        pantalla.fill((0,0,0))
        mostrar(xf0,y/2,fondo)
        mostrar(xf1,y/2,fondo,180)
        if k<len(Nave)-1:
            k+=1
        else:
            k=0
        if t<2*np.pi*5:
            t+=1/5
        else:
            t=0
        if xp<x/2:
            xp+=40
        else:
            if xf0>-1280/2+80:
                xf0-=80
            else:
                xf0=1280+1280/2
            if xf1>-1280/2+80:
                xf1-=80
            else:
                xf1=1280+1280/2
            if n<8:
                mostrar(100,600,Senora[int(counts)])
                if counts<len(Senora)-0.5:
                    counts+=0.5
                else:
                    p.draw.rect(pantalla,(0,0,0),(200,500,int(yr*950),int(xr*170)))
                    if xr<1:
                        xr+=0.1
                        yr+=0.1
                    else:
                        if k1<len(Dialogos[n][0]):
                            k1+=1
                        else:
                            if k2<len(Dialogos[n][1]):
                                k2+=1
                            else:
                                saltar=True
                        mostrartext(Dialogos[n][0],k1,220,550,[0,1,0])
                        mostrartext(Dialogos[n][1],k2,220,600,[0,1,0])
            else:
                if counts>0.5:
                    counts-=0.5
                    mostrar(100,600,Senora[int(counts)])
                if xr>0.1:
                    xr-=0.1
                    yr-=0.1
                    p.draw.rect(pantalla,(0,0,0),(200,500,int(yr*950),int(xr*170)))
                xp+=20
        if saltar:
            if col<10:
                col+=1
            else:
                col=0
            if col<5:
                mostrartext(continuar[0],len(continuar[0]),1050,20)
                mostrartext(continuar[1],len(continuar[1]),1050,70)
            else:
                mostrartext(continuar[0],len(continuar[0]),1050,20,[0,1,0])
                mostrartext(continuar[1],len(continuar[1]),1050,70,[0,1,0])
        if xp>1380:
            break
        yp=50*np.sin(t)+y/2
        mostrar(xp,yp,Nave[int(k)])
        p.display.update()

def c1():
    Save=open("Guardado.txt","r")
    text=int(Save.readline())
    Save.close()
    Save=open(str(text)+".txt","r")
    nombre=Save.readline().replace('\n',"")
    Save.close()
    x,y=1280,720
    pantalla=p.display.set_mode((x,y))
    Icono = p.image.load('Nivel 4\\Imagenes\\Icono.png')
    p.display.set_icon(Icono)
    p.display.set_caption("Shut 'em all")
    font=p.font.Font('Nivel 4\\Fuentes\\Open 24 Display St.ttf',30)
    def mostrartext(texto,k,x,y,c=[1,1,1]):
        t=font.render(texto[0:int(k)],True,(c[0]*255,c[1]*255,c[2]*255))
        pantalla.blit(t,(int(x),int(y)))

    #Dialogos
    countcolor=0
    continuar=['Presiona "enter"', "para continuar."]
    colcont=[0,0,0]
    Dialogo1=["Riube: Felicidades "+nombre+", tu última misión ha sido impecable. Sin embargo tu nave tuvo muchos", "problemas el sistema de disparo ha sido destruido."]
    Dialogo2=["Riube: Lo sentimos, ha sido imposible arreglar tu disparo, solo tienes una bala por disparo.",nombre+": Señor quiero reportar la última misión debido muchísimas irregularidades."]
    Dialogo3=[nombre+": Los capturados no se defendían y además algunos de ellos no han aparecido" ,"incluso algunos aparecen muertos y reportados como reveldes..."]
    Dialogo4=["Riube: SOLDADO ESOS TEMÁS NO SON DE SU INTERES, los capturados eran enemigos de la paz.","Las bajas en la guerra son inevitables, mejor discutamos acerca de tu nueva misión."]
    Dialogo5=["Riube: Hemos encontrado un campamento lleno de enemigos en una zona aparentemente pacífica,", "tu misión es acabar con todas las personas que se resistan."]
    Dialogo6=["Riube: Contamos contigo "+nombre+"...",""]
    k1,k2=0,0
    n=0
    Dialogos=[Dialogo1,Dialogo2,Dialogo3,Dialogo4,Dialogo5,Dialogo6]
    Fondos=[p.image.load("Nivel 4\\Imagenes\\Cinematica\\1.png").convert(),p.image.load("Nivel 4\\Imagenes\\Cinematica\\2.png").convert(),p.image.load("Nivel 4\\Imagenes\\Cinematica\\3.png").convert(),p.image.load("Nivel 4\\Imagenes\\Cinematica\\1.png").convert(),p.image.load("Nivel 4\\Imagenes\\Cinematica\\5.png").convert(),p.image.load("Nivel 4\\Imagenes\\Cinematica\\6.png").convert()]
    a1=0
    a2=0
    yf=0


    saltar=False
    Run=True
    while Run:
        p.time.Clock().tick(60)
        for event in p.event.get():
            if event.type== p.QUIT:
                Run=False
                sys.exit()
            if event.type==p.KEYDOWN:
                if event.key==p.K_RETURN:
                    if saltar:
                        k1,k2=0,0
                        n+=1
                        a2=255
                        a1=0
                        yf=0
                        saltar=False
                    else:
                        saltar=True
        if n==6:
            break
        pantalla.fill((0,0,0))
        if n>0:
            pantalla.blit(Fondos[n-1],(0,0))
            Fondos[n-1].set_alpha(a2)
        Fondos[n].set_alpha(a1)
        pantalla.blit(Fondos[n],(0,int(yf)))
        if n==5:
            p.draw.rect(pantalla,(0,0,0),(0,550,1280,170))
            if yf>-100:
                yf-=0.3
        if a2>0:
            a2-=2*3
        else:
            if a1<255:
                a1+=2
        if k1<len(Dialogos[n][0]):
            k1+=1
        else:
            if k2<len(Dialogos[n][1]):
                k2+=1
            else:
                saltar=True
        if saltar:
            if countcolor<20:
                countcolor+=1
            else:
                countcolor=0
            if countcolor<10:
                colcont=[0,1,0]
            else:
                colcont=[1,1,1]
            mostrartext(continuar[0],len(continuar[0]),1050,20,colcont)
            mostrartext(continuar[1],len(continuar[1]),1050,50,colcont)
        mostrartext(Dialogos[n][0],k1,20,600)
        if n!=1:
            mostrartext(Dialogos[n][1],k2,120,650)
        else:
            mostrartext(Dialogos[n][1],k2,20,650)
        p.display.update()

def c2():
    Save=open("Guardado.txt","r")
    text=int(Save.readline())
    Save.close()
    Save=open(str(text)+".txt","r")
    nombre=Save.readline().replace('\n',"")
    Save.close()
    x,y=1280,720
    pantalla=p.display.set_mode((x,y))
    Icono = p.image.load('Nivel 4\\Imagenes\\Icono.png')
    p.display.set_icon(Icono)
    p.display.set_caption("Shut 'em all")
    font=p.font.Font('Nivel 4\\Fuentes\\Open 24 Display St.ttf',30)
    def mostrartext(texto,k,x,y,c=[1,1,1]):
        t=font.render(texto[0:int(k)],True,(c[0]*255,c[1]*255,c[2]*255))
        pantalla.blit(t,(int(x),int(y)))

    #Dialogos
    countcolor=0
    continuar=['Presiona "enter"', "para continuar."]
    colcont=[0,0,0]
    Dialogo1=["Riube: Felicidades, muy buen trabajo "+nombre+"...",""]
    Dialogo2=[nombre+": No.","No más mentiras, estoy harto de obedecer ordenes sin saber qué es lo que pasa."]
    Dialogo3=["Riube: Soldado no se equivoque. Eso no le corresponde.",""]
    n1=r.randint(15,len(Dialogo3[0]))
    Dialogo4=[nombre+": No, dejeme hablar Sr. Riube, sus politicas bélicas no han dejado más que destrucción y", "miedo a su paso."]
    Dialogo5=[nombre+": Hemos acabado con cientos de vidas. En nombre de la 'paz' han muerto inocentes en el", "medio ¿Cree que no notamos que no se defienden de nuestros ataques?"]
    Dialogo6=[nombre+": Lo único que hacen es correr por sus vidas, saben el peligro que representamos","Una guerra absurda por sus deseos de venganza, ¿verdad?"]
    Dialogo7=["Riube: Soldado no desacate mis ordenes.",""]
    n2=r.randint(15,len(Dialogo7[0]))
    Dialogo8=[nombre+": Nos prometio paz, pero lo que tienen las personas es miedo","La violencia está peor que cuándo usted subió al poder."]
    Dialogo9=[nombre+": Ciudades destruidas, vidas perdidas y todo por una falsa seguridad.","Por lo tanto presento mi salida del equipo, no continuaré trabajando para un régimén así."]
    Dialogo10=["Riube:...",""]
    Dialogo11=["Riube: Vayan tras él.",""]
    k1,k2=0,0
    n=0
    Dialogos=[Dialogo1,Dialogo2,Dialogo3,Dialogo4,Dialogo5,Dialogo6,Dialogo7,Dialogo8,Dialogo9,Dialogo10,Dialogo11]
    Fondos=[]
    t=[1]
    a=[0]
    xf,yf=[1280/2],[720/2]
    for i in range(8):
        Fondos.append(p.image.load("Nivel 4\\Imagenes\\Cinematica\\1"+str(i)+".png").convert_alpha())
        if i==1 or i==5:
            Fondos.append(p.image.load("Nivel 4\\Imagenes\\Cinematica\\1"+str(i)+".png").convert_alpha())
        t.append(2)
        a.append(r.randint(-45,45))
        xf.append(r.randint(250,1030))
        yf.append(r.randint(250,470))
    Fondos.append(p.image.load("Nivel 4\\Imagenes\\Cinematica\\18.png").convert())

    def mostrar(x,y,img,a=0,j=1):
        im=p.transform.rotozoom(img,a,j)
        centro=im.get_rect(center=(int(x),int(y)))
        pantalla.blit(im,centro)

    saltar=False
    Run=True
    while Run:
        p.time.Clock().tick(60)
        for event in p.event.get():
            if event.type== p.QUIT:
                Run=False
                sys.exit()
            if event.type==p.KEYDOWN:
                if event.key==p.K_RETURN:
                    if saltar:
                        k1,k2=0,0
                        n+=1
                        saltar=False
                    else:
                        saltar=True
        if n==11:
            break
        pantalla.fill((0,0,0))
        if 0<n<9:
            for i in range(n+1):
                if i!=2 and i!=6:
                    mostrar(xf[i],yf[i],Fondos[i],a[i],t[i])
            if t[n]>1:
                t[n]-=0.1
                a[n]+=1
        if n==10:
            mostrar(x/2,y/2,Fondos[-1])
        p.draw.rect(pantalla,(0,0,0),(0,550,1280,170))
        if n==2:
            if int(k1)>=n1-1:
                k1,k2=0,0
                n+=1
        elif n==6:
            if int(k1)>=n2-1:
                k1,k2=0,0
                n+=1
        if k1<len(Dialogos[n][0]):
            if n==0 or n==2 or n==6:
                k1+=0.8
            else:
                k1+=2
        else:
            if k2<len(Dialogos[n][1]):
                k2+=2
            else:
                saltar=True
        if saltar:
            if countcolor<20:
                countcolor+=1
            else:
                countcolor=0
            if countcolor<10:
                colcont=[0,1,0]
            else:
                colcont=[1,1,1]
            mostrartext(continuar[0],len(continuar[0]),1050,20,colcont)
            mostrartext(continuar[1],len(continuar[1]),1050,50,colcont)
        mostrartext(Dialogos[n][0],k1,20,600)
        mostrartext(Dialogos[n][1],k2,120,650)
        p.display.update()

def creditos():
    Save=open("Guardado.txt","r")
    text=int(Save.readline())
    Save.close()
    Save=open(str(text)+".txt","r")
    nombre=Save.readline().replace('\n',"")
    score=int(Save.readline().replace("\n",""))
    Save.close()
    x,y=1280,720
    pantalla=p.display.set_mode((x,y))
    Icono = p.image.load('Nivel 4\\Imagenes\\Icono.png')
    p.display.set_icon(Icono)
    p.display.set_caption("Shut 'em all")
    font=p.font.Font('Nivel 4\\Fuentes\\Timeless-Bold.ttf',30)
    t=0
    yi=y/2
    count=0
    font1=p.font.Font("Fuentes\\Coalition_v2.ttf",t*100)
    titulo="Shut 'em all"
    Creditos=["Hecho por",
    "Juan Bueno     Jhon Moreno",
    "",
    "Nivel 1",
    "Jhon Moreno","",
    "Nivel 2",
    "Juan Bueno","",
    "Nivel 3",
    "Juan Bueno","",
    "Nivel 4",
    "Jhon Moreno","",
    "Cinemáticas",
    "Juan Bueno     Jhon Moreno",
    "",
    "¿Juego del año?",
    "Sí"]
    yc=800
    n=0
    Holi=[nombre+" gracias por jugar.","Tu puntaje: "+str(score)]
    Fondos=[]
    a1,a2=0,0
    for i in range(8):
        Fondos.append(p.image.load("Nivel 4\\Imagenes\\Cinematica\\C"+str(i)+".png").convert())

    def txt(texto,fonts,y):
        a=fonts.render(texto,True,(255,255,255))
        ca=a.get_rect(center=(int(x/2),int(y)))
        pantalla.blit(a,ca)

    Run=True
    while Run:
        p.time.Clock().tick(60)
        for event in p.event.get():
            if event.type== p.QUIT:
                Run=False
                sys.exit()
        pantalla.fill((0,0,0))
        if t<100:
            t+=1
        else:
            yi-=1
            yc-=1
            if count<216:
                count+=1
            else:
                count=0
                n+=1
                a2,a1=255,0
                if n==9:
                    t=0
                if n==10:
                    break
            if a2>0:
                a2-=3
            else:
                if a1<255:
                    a1+=2
            if 0<n<8:
                Fondos[n-1].set_alpha(a2)
                pantalla.blit(Fondos[n-1],(0,0))
            if n<8:
                Fondos[n].set_alpha(a1)
                pantalla.blit(Fondos[n],(0,0))
        if n<8:
            font1=p.font.Font("Fuentes\\Coalition_v2.ttf",int(t))
            txt(titulo,font1,yi)
        if n<9:
            for i in range(len(Creditos)):
                txt(Creditos[i],font,yc+i*50)
        if n==9:
            font1=p.font.Font("Fuentes\\Coalition_v2.ttf",int(t//3))
            txt(Holi[0],font1,y/2-100)
            txt(Holi[1],font1,y/2+100)
        p.display.update()