import random as r
import math as m
import pygame as p
import sys
from pygame import mixer
def c1():
    Save=open("Guardado.txt","r")
    text=int(Save.readline())
    Save.close()
    Save=open(str(text)+".txt","r")
    nombre=Save.readline().replace('\n',"")
    Save.close()
    x=1280
    y=720
    pantalla = p.display.set_mode((x,y))
    p.display.set_caption("Shut 'em all")
    Icono = p.image.load('Nivel 1\\Imagenes\\Icono.png')
    p.display.set_icon(Icono)
    cinematica=True
    font=p.font.Font('Nivel 1\\Fuentes\\Open 24 Display St.ttf',30)
    continuar=['Presiona "enter"', "para continuar."]
    colcont=[0,0,0]
    countcolor=0
    Dialogo0=["Día cero:", nombre+" : Recuerdo ese día cada día de mi vida, ¿cómo olvidarlo?, fue el día en que los problemas", "empezaron..."]
    k1=0
    k2=0
    k3=0
    Fondo1=p.image.load('Nivel 1\\Imagenes\\Cinematica\\0.jpg').convert()
    trans1=0
    Dialogo1=["Día cero:", nombre+" : En el sistema planetario C0L0M814, un sistema en el que la paz no es la que reina,", "puesto existen grupos anarquicos a lo largo de todo el sistema."]
    Fondo2=p.image.load('Nivel 1\\Imagenes\\Cinematica\\1.1.jpg').convert()
    nave=p.image.load('Nivel 1\\Imagenes\\Cinematica\\1.2.png').convert_alpha()
    xn,yn=-600,int(720/2-80)
    trans2=0
    Dialogo2=[nombre+" : El planeta M3TR4110 se encuentra bajo ataque de un grupo subversivo conocido como la", "F.A.R. He sido asignado para la defensa de este planeta."]
    Fondo3=p.image.load('Nivel 1\\Imagenes\\Cinematica\\2.0.png').convert()
    tanques=p.image.load('Nivel 1\\Imagenes\\Cinematica\\2.1.png').convert_alpha()
    xt,yt=[],[]
    for i in range(5):
        xt.append(0-i*150)
        yt.append(450)
    Dialogo3=[nombre+" : Así que es hora de defendernos del ataque enemigo..."]
    def mostrartext(texto,k,x,y,c=[1,1,1]):
        t=font.render(texto[0:int(k)],True,(c[0]*255,c[1]*255,c[2]*255))
        pantalla.blit(t,(int(x),int(y)))
    saltar=False
    scene0=True
    scene1=False
    scene2=False
    scene3=False
    while cinematica:
        while scene0:
            p.time.Clock().tick(60)
            for event in p.event.get():
                if event.type== p.QUIT:
                    scene0=False
                    nivel=False
                    cinematica=False
                    sys.exit()
                    return nivel
                if event.type==p.KEYDOWN:
                    if event.key==p.K_RETURN:
                        if saltar:
                            scene0=False
                            scene1=True
                            k1,k2,k3=0,0,0
                            saltar=False
                        else:
                            saltar=True
            pantalla.fill((0,0,0))
            if k1<len(Dialogo0[0]):
                k1+=0.4
            else:
                if k2<len(Dialogo0[1]):
                    k2+=0.4
                else:
                    if k3<len(Dialogo0[2]):
                        k3+=0.4
                    else:
                        saltar=True
            mostrartext(Dialogo0[0],k1,10,20)
            mostrartext(Dialogo0[1],k2,20,600)
            mostrartext(Dialogo0[2],k3,80,650)
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
            p.display.update()
        while scene1:
            p.time.Clock().tick(60)
            for event in p.event.get():
                if event.type== p.QUIT:
                    scene1=False
                    nivel=False
                    cinematica=False
                    return nivel
                if event.type==p.KEYDOWN:
                    if event.key==p.K_RETURN:
                        if saltar:
                            scene1=False
                            k1,k2,k3=0,0,0
                            saltar=False
                            scene2=True
                        else:
                            saltar=True
            pantalla.fill((0,0,0))
            if trans1<255:
                trans1+=1
            Fondo1.set_alpha(trans1)
            pantalla.blit(Fondo1,(-100,0))
            if k1<len(Dialogo1[0]):
                k1+=0.4
            else:
                if k2<len(Dialogo1[1]):
                    k2+=0.4
                else:
                    if k3<len(Dialogo1[2]):
                        k3+=0.4
                    else:
                        saltar=True
            mostrartext(Dialogo1[0],k1,10,20)
            mostrartext(Dialogo1[1],k2,20,600)
            mostrartext(Dialogo1[2],k3,80,650)
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
            p.display.update()
        while scene2:
            p.time.Clock().tick(60)
            for event in p.event.get():
                if event.type== p.QUIT:
                    scene2=False
                    nivel=False
                    cinematica=False
                    return nivel
                if event.type==p.KEYDOWN:
                    if event.key==p.K_RETURN:
                        if saltar:
                            scene2=False
                            k1,k2,k3=0,0,0
                            saltar=False
                            cinematica=False
                            scene3=True
                        else:
                            saltar=True
            pantalla.fill((0,0,0))
            if trans1>0:
                trans1-=3
                Fondo1.set_alpha(trans1)
                pantalla.blit(Fondo1,(-100,0))
            if trans2<255:
                trans2+=1
            if xn<100:
                xn+=2
            Fondo2.set_alpha(trans2)
            pantalla.blit(Fondo2,(0,0))
            nave.set_alpha(trans2)
            pantalla.blit(nave,(xn,yn))
            if k1<len(Dialogo2[0]):
                k1+=0.4
            else:
                if k2<len(Dialogo2[1]):
                    k2+=0.4
                else:
                    saltar=True
            mostrartext(Dialogo2[0],k1,20,600)
            mostrartext(Dialogo2[1],k2,80,650)
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
            p.display.update()
        while scene3:
            p.time.Clock().tick(60)
            for event in p.event.get():
                if event.type== p.QUIT:
                    scene3=False
                    nivel=False
                    cinematica=False
                    return nivel
                if event.type==p.KEYDOWN:
                    if event.key==p.K_RETURN:
                        if saltar:
                            scene3=False
                            k1,k2,k3=0,0,0
                            saltar=False
                            cinematica=False
                            nivel=True
                            return nivel
                        else:
                            saltar=True
            pantalla.fill((0,0,0))
            if trans2>0:
                trans2-=3
                Fondo2.set_alpha(trans2)
                pantalla.blit(Fondo2,(0,0))
                if xn<100:
                    xn+=2
                nave.set_alpha(trans2)
                pantalla.blit(nave,(xn,yn))
            if trans1<255:
                trans1+=1
            Fondo3.set_alpha(trans1)
            tanques.set_alpha(trans1)
            pantalla.blit(Fondo3,(0,0))
            for i in range(5):
                if xt[4]<100:
                    xt[i]+=0.5
                pantalla.blit(tanques,(int(xt[i]),int(yt[i])))            
            if k1<len(Dialogo2[0]):
                k1+=0.4
            else:
                saltar=True
            mostrartext(Dialogo3[0],k1,20,600)
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
            p.display.update()
        p.display.update()
def c2():
    #p.init()
    Save=open("Guardado.txt","r")
    text=int(Save.readline())
    Save.close()
    Save=open(str(text)+".txt","r")
    nombre=Save.readline().replace('\n',"")
    Save.close()
    x=1280
    y=720
    pantalla = p.display.set_mode((x,y))
    p.display.set_caption("Shut 'em all")
    Icono = p.image.load('Nivel 1\\Imagenes\\Icono.png')
    p.display.set_icon(Icono)
    cinematica=True
    font=p.font.Font('Nivel 1\\Fuentes\\Open 24 Display St.ttf',30)
    continuar=['Presiona "enter"', "para continuar."]
    colcont=[0,0,0]
    countcolor=0
    k1=0
    k2=0
    k3=0
    Dialogo0=["Día 7:",nombre+" : Tras una semana de duro combate. A pesar de nuestra excelente defensa las bajas", "fueron inevitables, entre ellas la perdida del lider del sistema planetario."]
    Fondo0=p.image.load('Nivel 1\\Imagenes\\Cinematica\\3.1.png').convert()
    Fuego=[]
    xF=[]
    yF=[]
    for i in range(20):
        Fuego.append(p.image.load('Nivel 1\\Imagenes\\Cinematica\\F'+str(i)+'.png').convert_alpha())
    for i in range(8):
        xF.append(100+i*140)
        yF.append(r.randint(0,400))
    countf=0
    trans0=0
    trans1=0
    Dialogo1=[nombre+' : Tras la muerte del mayor, subió al poder un tal "Riube", este sujeto perdió a su padre','en los últimos enfrentamientos con la F.A.R. A pesar de que apareció de la nada', 'asegura que combatirá hasta derrotar a la F.A.R.']
    Fondo1=p.image.load('Nivel 1\\Imagenes\\Cinematica\\3.2.png').convert()
    Dialogo2=[nombre+" : Por lo tanto es nuestro turno de tomar el contraataque, es hora de tomar venganza..."]
    Fondo2=p.image.load('Nivel 1\\Imagenes\\Cinematica\\3.3.jpg').convert()
    Nave=[]
    k=0
    xp,yp,velx,vely=200,500,2,0.5
    for i in range(1,61):
        Nave.append(p.image.load("Nivel 1\\Imagenes\\Cinematica\\Navesprite\\"+str(i)+".png").convert_alpha())
    def mostrartext(texto,k,x,y,c=[1,1,1]):
        t=font.render(texto[0:int(k)],True,(c[0]*255,c[1]*255,c[2]*255))
        pantalla.blit(t,(int(x),int(y)))
    saltar=False
    scene0=True
    scene1=False
    scene2=False
    while cinematica:
        while scene0:
            p.time.Clock().tick(60)
            for event in p.event.get():
                if event.type== p.QUIT:
                    scene0=False
                    nivel=False
                    cinematica=False
                    return nivel
                if event.type==p.KEYDOWN:
                    if event.key==p.K_RETURN:
                        if saltar:
                            scene0=False
                            scene1=True
                            k1,k2,k3=0,0,0
                            saltar=False
                            cinematica=False
                        else:
                            saltar=True
            pantalla.fill((0,0,0))
            if trans0<255:
                trans0+=1
            Fondo0.set_alpha(trans0)
            pantalla.blit(Fondo0,(0,0))

            if countf<len(Fuego)-0.3:
                countf+=0.3
            else:
                countf=0
            Fuego[int(countf)]=p.image.load('Nivel 1\\Imagenes\\Cinematica\\F'+str(int(countf))+'.png').convert_alpha()
            alpha_img = p.Surface(Fuego[0].get_size(), p.SRCALPHA)
            alpha_img.fill((255, 255, 255, trans0))
            Fuego[int(countf)].blit(alpha_img, (0, 0), special_flags=p.BLEND_RGBA_MULT)
            for i in range(8):
                pantalla.blit(Fuego[int(countf)],(xF[i],yF[i]))
            if k1<len(Dialogo0[0]):
                k1+=0.4
            else:
                if k2<len(Dialogo0[1]):
                    k2+=0.4
                else:
                    if k3<len(Dialogo0[2]):
                        k3+=0.4
                    else:
                        saltar=True
            mostrartext(Dialogo0[0],k1,10,20)
            mostrartext(Dialogo0[1],k2,20,600)
            mostrartext(Dialogo0[2],k3,80,650)
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
            p.display.update()
        while scene1:
            p.time.Clock().tick(60)
            for event in p.event.get():
                if event.type== p.QUIT:
                    scene1=False
                    nivel=False
                    cinematica=False
                    return nivel
                if event.type==p.KEYDOWN:
                    if event.key==p.K_RETURN:
                        if saltar:
                            scene1=False
                            scene2=True
                            k1,k2,k3=0,0,0
                            saltar=False
                        else:
                            saltar=True
            pantalla.fill((0,0,0))
            if trans0>0:
                trans0-=3
                if trans0<0:
                    trans0=0
                Fondo0.set_alpha(trans0)
                pantalla.blit(Fondo0,(0,0))
                if countf<len(Fuego)-0.3:
                    countf+=0.3
                else:
                    countf=0
                Fuego[int(countf)]=p.image.load('Nivel 1\\Imagenes\\Cinematica\\F'+str(int(countf))+'.png').convert_alpha()
                alpha_img = p.Surface(Fuego[0].get_size(), p.SRCALPHA)
                alpha_img.fill((255, 255, 255, trans0))
                Fuego[int(countf)].blit(alpha_img, (0, 0), special_flags=p.BLEND_RGBA_MULT)
                for i in range(8):
                    pantalla.blit(Fuego[int(countf)],(xF[i],yF[i]))
            if trans1<255:
                trans1+=1
            Fondo1.set_alpha(trans1)
            pantalla.blit(Fondo1,(0,0))
            if k1<len(Dialogo1[0]):
                k1+=0.4
            else:
                if k2<len(Dialogo1[1]):
                    k2+=0.4
                else:
                    if k3<len(Dialogo1[2]):
                        k3+=0.4
                    else:
                        saltar=True
            mostrartext(Dialogo1[0],k1,20,550)
            mostrartext(Dialogo1[1],k2,80,600)
            mostrartext(Dialogo1[2],k3,80,650)
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
            p.display.update()
        while scene2:
            p.time.Clock().tick(60)
            for event in p.event.get():
                if event.type== p.QUIT:
                    scene1=False
                    nivel=False
                    cinematica=False
                    return nivel
                if event.type==p.KEYDOWN:
                    if event.key==p.K_RETURN:
                        if saltar:
                            scene1=False
                            k1,k2,k3=0,0,0
                            saltar=False
                            return True
                        else:
                            saltar=True
            pantalla.fill((0,0,0))
            if trans1>0:
                trans1-=3
                if trans1<0:
                    trans1=0
                    Fondo1.set_alpha(trans1)
                    pantalla.blit(Fondo1,(0,0))
            if k<=58:
                k+=1
            else:
                k=0
            if trans0<255:
                trans0+=1
            Fondo2.set_alpha(trans0)
            pantalla.blit(Fondo2,(0,0))
            Nave[int(k)]=p.image.load("Nivel 1\\Imagenes\\Cinematica\\Navesprite\\"+str(int(k+1))+".png").convert_alpha()
            alpha_img = p.Surface(Nave[0].get_size(), p.SRCALPHA)
            alpha_img.fill((255, 255, 255, trans0))
            Nave[int(k)].blit(alpha_img, (0, 0), special_flags=p.BLEND_RGBA_MULT)
            if xp<x/2+100:
                xp+=velx
                yp-=vely
            pantalla.blit(Nave[k],(int(xp),int(yp)))
            if k1<len(Dialogo1[0]):
                k1+=0.4
            else:
                saltar=True
            mostrartext(Dialogo2[0],k1,20,600)
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
            p.display.update()
        p.display.update()
def pause():
    class Img:
        def __init__(self,a):
            self.ubicacion=a
        def img(self):
            return p.image.load("Imagenes\\"+self.ubicacion).convert_alpha()
    #p.init()
    #p.mixer.init()
    x=1280
    y=720
    pantalla = p.display.set_mode((x,y))
    p.display.set_caption("Shut 'em all")
    Icono = p.image.load('Imagenes\\Icono.png')
    p.display.set_icon(Icono)
    fondo=Img("0.png").img()
    fondo1=Img("2.png").img()
    fondo1.set_alpha(50)
    boton=Img("Boton1.png").img()
    tap=mixer.Sound("Sonidos\\boton_tap.wav")
    canaltap=mixer.Channel(0)
    k1s,k2s=0,0
    #Texto
    font=p.font.Font("Fuentes\\Coalition_v2.ttf",100)
    font1=p.font.Font("Fuentes\\Open 24 Display St.ttf",35)
    def name():
        Titulo=font.render("Pausa",True,(255,255,255))
        Tcentro=Titulo.get_rect(center=(int(x/2),150))
        pantalla.blit(Titulo,Tcentro)
    t=0
    MH="Reanudar"
    ML="Salir al menú"
    k1=0
    k2=0
    def opciones(k1,k2):
        op1=font1.render(MH,True,(255,255,255))
        cop1=op1.get_rect(center=(int(x/2),int(y/2)))
        op2=font1.render(ML,True,(255,255,255))
        cop2=op2.get_rect(center=(int(x/2),int(y/2+150)))
        op1l=font1.render(MH[0:k1],True,(0,255,0))
        op2l=font1.render(ML[0:k2],True,(0,255,0))
        pantalla.blit(op1,cop1)
        pantalla.blit(op2,cop2)
        pantalla.blit(op1l,cop1)
        pantalla.blit(op2l,cop2)
    #mostrar Nave
    def mostrar(x,y,im,a=0,t=1):
        img=p.transform.rotozoom(im,a,t)
        centro=img.get_rect(center=(int(x),int(y)))
        pantalla.blit(img,centro)
    Nave=[]
    xn,yn=1280,720/2
    k=0
    for i in range(1,61):
        ub="NaveSprite\\"
        ub+=str(i)+".png"
        im=Img(ub)
        Nave.append(im.img())
    p.mouse.set_visible(0)
    menu=False
    pause=True
    while pause:
        click=False
        p.time.Clock().tick(60)
        for event in p.event.get():
            if event.type== p.QUIT:
                pause=False
                sys.exit()
            elif event.type==p.KEYDOWN:
                if event.key==p.K_ESCAPE:
                    pause=False
                    break
            elif event.type==p.MOUSEBUTTONDOWN:
                if event.button==1:
                    click =True
        mx,my=p.mouse.get_pos()
        mostrar(x/2,y/2,fondo1)
        fondo1.set_alpha(50)
        mostrar(x/2,y/2,fondo,0,t)
        if k<len(Nave)-1:
            k+=1
        else:
            k=0
        name()
        mostrar(x/2,y/2,boton,0,t)
        mostrar(x/2,y/2+150,boton,0,t)
        if t<0.9:
            t+=0.1
        else:
            if 514<=mx<=764:
                if 329<=my<=389:
                    if k1<len(MH):
                        k1+=1
                    else:
                        k1=0
                    if k1s==0:
                        canaltap.play(tap)
                        k1s=1
                    if click:
                        pause=False
                        break
                else:
                    k1,k1s=0,0
                if 480<=my<=536:
                    if k2<len(ML):
                        k2+=1.5
                    else:
                        k2=0
                    if k2s==0:
                        canaltap.play(tap)
                        k2s=1
                    if click:
                        menu=True
                else:
                    k2,k2s=0,0
            opciones(k1,int(k2))
        if 250<mx<=982 and 10<my<668:
            mostrar(mx+15,my+15,Nave[int(k)],135,0.5)
        if menu:
            mostrar(x/2,y/2,fondo1)
            mostrar(xn,yn,Nave[int(k)],180)
            if xn>-40:
                xn-=30
            else:
                return menu
        p.display.update()


def puntos():
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
    niveles=[nivel1,nivel2,nivel3]
    scoresi=[scorei1,scorei2,scorei3]
    p.init()
    Icono = p.image.load('Imagenes\\Icono.png')
    p.display.set_icon(Icono)
    x=1280
    y=720
    pantalla = p.display.set_mode((x,y))
    p.display.set_caption("Shut 'em all")
    class Img:
        def __init__(self,a):
            self.ubicacion=a
        def img(self):
            return p.image.load("Imagenes\\"+self.ubicacion).convert_alpha()
        def most(self,x,y):
            cent=self.img().get_rect(center=(int(x),int(y)))
            pantalla.blit(self.img(),cent)
    #Fuentes
    font=p.font.Font("Fuentes\\Coalition_v2.ttf",25)
    fondo=p.image.load("Imagenes\\fond.png").convert()
    xi=[x/2-400,x/2,x/2+400]
    def todo():
        for i in range(3):
            n=font.render(nombres[i],True,(255,255,255))
            cn=n.get_rect(center=(int(xi[i]),200))
            nv=font.render(scores[i],True,(255,255,255))
            cnv=nv.get_rect(center=(int(xi[i]),350))
            por=font.render(str(int(niveles[i])*25)+"%",True,(255,255,255))
            cpor=por.get_rect(center=(int(xi[i]),400))
            inf=font.render(scoresi[i],True,(255,255,255))
            ci=inf.get_rect(center=(int(xi[i]),525))
            pantalla.blit(n,cn)
            pantalla.blit(nv,cnv)
            pantalla.blit(por,cpor)
            pantalla.blit(inf,ci)
        T=font.render("Modo Historia",True,(255,255,255))
        cT=T.get_rect(center=(int(x/2),300))
        T2=font.render("Modo Infinito",True,(255,255,255))
        cT2=T2.get_rect(center=(int(x/2),475))
        pantalla.blit(T,cT)
        pantalla.blit(T2,cT2)
    #Ksa
    ksa=Img("Home.png")
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
    Run=True
    while Run:
        p.time.Clock().tick(60)
        for event in p.event.get():
            if event.type== p.QUIT:
                Run=False
                sys.exit()
            if event.type == p.MOUSEBUTTONDOWN:
                if event.button==1:
                    if 1190<=mx<=1270 and 9<=my<=87:
                        Run=False
        if k<len(Nave)-1:
            k+=1
        else:
            k=0
        mx,my=p.mouse.get_pos()
        pantalla.blit(fondo,(0,0))
        ksa.most(1230,50)
        todo()
        mostrar(mx+15,my+15,Nave[int(k)],135,0.5)
        p.display.update()
def controles():
    p.init()
    Icono = p.image.load('Imagenes\\Icono.png')
    p.display.set_icon(Icono)
    x=1280
    y=720
    pantalla = p.display.set_mode((x,y))
    p.display.set_caption("Shut 'em all")
    class Img:
        def __init__(self,a):
            self.ubicacion=a
        def img(self):
            return p.image.load("Imagenes\\"+self.ubicacion).convert_alpha()
        def most(self,x,y):
            cent=self.img().get_rect(center=(int(x),int(y)))
            pantalla.blit(self.img(),cent)
    #Fuentes
    font=p.font.Font("Fuentes\\Coalition_v2.ttf",50)
    font1=p.font.Font("Fuentes\\Coalition_v2.ttf",25)
    Titulo=font.render("Controles",True,(255,255,255))
    cT=Titulo.get_rect(center=(int(x/2),50))
    N,T=font1.render("Nave",True,(255,255,255)),font1.render("Torreta",True,(255,255,255))
    cN,ct=N.get_rect(center=(int(x/3)-100,150)),T.get_rect(center=(int(2*x/3)+75,150))
    salt=font1.render("Presiona Enter para continuar.",True,(255,255,255))
    csalt=salt.get_rect(center=(int(x/2),680))
    at=[font1.render("Ataque",True,(255,255,255)),font1.render("Especial",True,(255,255,255))]
    cat=[at[0].get_rect(center=(int(x/2),int(y/2))),at[1].get_rect(center=(int(x/2),int(y/2)+25))]
    P=font1.render("Pause",True,(255,255,255))
    cP=P.get_rect(center=(int(x/2),int(y/2)+200))
    Fondo=p.image.load("Imagenes\\1.png").convert()
    esc=[Img("Esc0.png"),Img("Esc1.png")]
    nesc=0
    W=[Img("W0.png"),Img("W1.png")]
    nW=0
    A=[Img("A0.png"),Img("A1.png")]
    nA=0
    S=[Img("S0.png"),Img("S1.png")]
    nS=0
    D=[Img("D0.png"),Img("D1.png")]
    nD=0
    nAt=0
    nDt=0
    E=[Img("E0.png"),Img("E1.png")]
    nE=0
    Sp=[Img("Space0.png"),Img("Space1.png")]
    nSp=0
    nSpt=0
    #Mostrar
    def mostrar(x,y,im,a=0,t=1):
        img=p.transform.rotozoom(im,a,t)
        centro=img.get_rect(center=(int(x),int(y)))
        pantalla.blit(img,centro)
    #Nave
    Nave=[]
    k=0
    xn,yn=200,350
    xd,yd=425,300
    for i in range(1,61):
        ub="NaveSprite\\"
        ub+=str(i)+".png"
        im=Img(ub)
        Nave.append(im.img())
    balaN=[]
    xbn=xd
    movcount=1
    nb=0
    for i in range(1,15):
        ub="Nivel 4\\Imagenes\\Misil\\"
        ub+=str(i)+".png"
        balaN.append(p.image.load(ub).convert_alpha())
    def tiro(a,x,y,i=0):
        nave=p.transform.rotozoom(balaN[int(i)],a,1)
        cnave=nave.get_rect(center=(int(x),int(y)))
        pantalla.blit(nave,cnave)
    #Torreta
    torreta = p.image.load("Nivel 1\\Imagenes\\N1.png").convert_alpha()
    Base=p.image.load("Nivel 1\\Imagenes\\Base.png").convert_alpha()
    angulo=90
    da=8
    def torret(angulo,x_p,y_p):
        Rotar=p.transform.rotozoom(torreta,angulo,1)
        Recto=Rotar.get_rect(center=(int(x_p),int(y_p)))
        Rectobase=Base.get_rect(center=(int(x_p),int(y_p)))
        pantalla.blit(Base,Rectobase)
        pantalla.blit(Rotar,Recto)
    #disparos torreta
    bala=p.image.load("Nivel 1\\Imagenes\\Bala.png").convert_alpha()
    coord_b=[1080,350]
    def disparar(a,y):
        Rotar=p.transform.rotozoom(bala,a,1)
        Recto=Rotar.get_rect(center=(int(1080),int(y)))
        pantalla.blit(Rotar,Recto)
    #Explosion
    Explosion=[]
    countExp=0
    for i in range(24):
        ub="Nivel 4\\Imagenes\\Misil\\Exp"
        ub+=str(i)+".png"
        im=Img(ub)
        Explosion.append(p.image.load(ub).convert_alpha())
    p.mouse.set_visible(0)
    Run=True
    while Run:
        p.time.Clock().tick(60)
        for event in p.event.get():
            if event.type== p.QUIT:
                Run=False
                sys.exit()
            if event.type == p.KEYDOWN:
                if event.key == p.K_RETURN:
                    Run=False
        mostrar(x/2,y/2,Fondo)
        p.draw.rect(pantalla,(128,128,128),(100,100,1080,520))
        pantalla.blit(Titulo,cT)
        pantalla.blit(T,ct)
        pantalla.blit(N,cN)
        pantalla.blit(salt,csalt)
        W[nW].most(250,450)
        A[nA].most(180,515)
        S[nS].most(250,515)
        D[nD].most(320,515)
        A[nAt].most(790,482)
        D[nDt].most(920,482)
        E[nE].most(int(500/2+790/2),y/2-50)
        if nesc<1.9:
            nesc+=0.1
        else:
            nesc=0
        esc[int(nesc)].most(int(500/2+790/2),y/2+150)
        pantalla.blit(P,cP)
        Sp[nSp].most(480,482)
        Sp[nSpt].most(1080,482)
        if k<len(Nave)-1:
            k+=1
        else:
            k=0
        if nb<=11:
            nb+=1
        else:
            nb=0
        if xbn<=x/2-30:
            xbn+=10
            if xbn<=x/2-50:
                nSp=0
                tiro(0,xbn,yd,nb)
            else:
                nSp=1
        else:
            xbn=xd
        mostrar(xn,yn,Nave[int(k)])
        if movcount==1:
            if yn>=200:
                yn-=8
                nW=1
            else:
                nW=0
                movcount+=1
        elif movcount==2:
            if yn<=350:
                yn+=8
                nS=1
            else:
                nS=0
                movcount+=1
        elif movcount==3: 
            if xn<=xd-70:
                xn+=8
                nD=1
            else:
                nD=0
                movcount+=1
        elif movcount==4: 
            if xn>=200:
                xn-=8
                nA=1
            else:
                nA=0
                movcount=1
        mostrar(xd,yd,Nave[int(k)])
        if coord_b[1]>=150:
            coord_b[1]-=10
            if coord_b[1]>=180:
                nSpt=0
                disparar(90,coord_b[1])
            else:
                nSpt=1
        else:
            coord_b[1]=350
        if angulo>=180 or angulo<=0:
            da*=-1
        angulo+=da
        if da>0:
            nAt=1
            nDt=0
        else:
            nDt=1
            nAt=0
        if countExp<26:
            countExp+=1
            if countExp<len(Explosion)-1:
                mostrar(x/2,y/2-150,Explosion[int(countExp)])
                nE=0
            else:
                nE=1
        else:
            countExp=0
        for i in range(2):
            pantalla.blit(at[i],cat[i])        
        torret(angulo,int(920/2+790/2),350)
        torret(90,1080,350)
        p.display.update()