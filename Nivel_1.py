import random
import math as m
import pygame as p
from pygame import mixer
import Cinematica_1_1
import Nivel_1_Jefe
def niv_1():
    Save=open("Guardado.txt","r")
    text=int(Save.readline())
    Save.close()
    Save=open(str(text)+".txt","r")
    nombre=Save.readline().replace('\n',"")
    score=int(Save.readline())
    Save.close()
    p.init()
    clock = p.time.Clock()
    #Sonidos
    mixer.init()
    saluds=mixer.Sound("Nivel 1\\Sonidos\\Salud.wav")
    exps=mixer.Sound("Nivel 1\\Sonidos\\Explosion.wav")
    sonidob=mixer.Sound("Nivel 1\\Sonidos\\Disparo.wav")
    Morse=mixer.Sound("Nivel 1\\Sonidos\\Morse1.wav")
    Spausa=mixer.Sound("Sonidos\\SpacyLoop.ogg")
    lose=mixer.Sound("Sonidos\\lose music.ogg")
    mixer.music.load("Nivel 1\\Sonidos\\Invisible Enemy.mp3")
    mixer.music.play(-1)
    channel1 = mixer.Channel(0)
    channel2 = mixer.Channel(1)
    channel3 = mixer.Channel(2)
    canalpausa=mixer.Channel(3)
    canalpausa.set_volume(0.3)
    canalpausa.play(Spausa,-1)
    canallose=mixer.Channel(4)
    canalpausa.pause()
    #Configuraciones de pantalla
    x=1280
    y=720
    pantalla = p.display.set_mode((x,y))
    p.display.set_caption("Shut 'em all")
    Icono = p.image.load('Nivel 1\\Imagenes\\Icono.png')
    p.display.set_icon(Icono)
    fondo = p.image.load('Nivel 1\\Imagenes\\Fondo2.png').convert()
    cfondo=fondo.get_rect(center=(int(x/2),int(y/2)))
    #Personaje
    vida=300
    torreta = p.image.load("Nivel 1\\Imagenes\\N1.png")
    Base=p.image.load("Nivel 1\\Imagenes\\Base.png")
    coord_p=[x/2,640,0,640,1280,640]
    angulo=90
    vel=0
    def torret(angulo,x_p,y_p):
        Rotar=p.transform.rotozoom(torreta,angulo,1)
        Recto=Rotar.get_rect(center=(int(x_p),int(y_p)))
        Rectobase=Base.get_rect(center=(int(x_p),int(y_p)))
        pantalla.blit(Base,Rectobase)
        pantalla.blit(Rotar,Recto)
    #Nombre
    Titulo="Nivel 1: Defiéndenos"
    font=p.font.Font('Nivel 1\\Fuentes\\BLADRMF_.TTF',28)
    fontp=p.font.Font('Nivel 1\\Fuentes\\BLADRMF_.TTF',20)
    fonttext=p.font.Font('Nivel 1\\Fuentes\\Timeless-Bold.ttf',40)
    fonttext2=p.font.Font('Nivel 1\\Fuentes\\Timeless-Bold.ttf',25)
    fonttorrecontrol=p.font.Font('Nivel 1\\Fuentes\\Open 24 Display St.ttf',24)
    olas=["Primera oleada","Segunda oleada","Tercer oleada","Jefe de la FAR"]
    numfase,fasecount=0,0
    x_f=-300
    cambiofase=True
    def ola(i,x):
        text=fonttext.render(olas[i],True,(255,255,255))
        ctext=text.get_rect(center=(int(x),int(y/2)))
        pantalla.blit(text,ctext)
    def name(a):
        hola=fonttext.render(a,True,(255,255,255))
        cent=hola.get_rect(center=(int(1280/2),50))
        pantalla.blit(hola,cent)
    #Introducción
    Introduccion=[]
    senora=[]
    k1=0
    k2=0
    activar,activar2,activar3,activar4=True,True,True,True
    for i in range(10):
        senora.append(p.image.load("Nivel 1\\Imagenes\\TorreControl\\"+str(i+1)+".png").convert_alpha())
    tutorial=False
    avisar=False
    avs=False
    countintro=-100
    def torrecontrol(i,j1,j2):
        text=fonttorrecontrol.render(Introduccion[int(i)][0:int(j1)],True,(0,255,0))
        text2=fonttorrecontrol.render(Introduccion[int(i+1)][0:int(j2)],True,(0,255,0))
        if Introduccion[int(i)][int(j1)-1]!=" " or Introduccion[int(i)][int(j1)-1]!="":
            if int(j1)%8==0:
                channel2.play(Morse)
        if Introduccion[int(i+1)][int(j2)-1]!=" " or Introduccion[int(i+1)][int(j2)-1]!="":
            if int(j2)%8==0:
                channel2.play(Morse)
        pantalla.blit(text,(150,630))
        pantalla.blit(text2,(150,660))
    #Balas pai :v
    bala=p.image.load("Nivel 1\\Imagenes\\Bala.png")
    coord_b=[-1000,-1000]
    coord_b1=coord_b
    a=0
    a1=a
    vel_b=6
    i=0
    r=100
    B=["Invisible","Invisible"]
    def disparar(a,x,y):
        Rotar=p.transform.rotozoom(bala,a,1)
        Recto=Rotar.get_rect(center=(int(x),int(y)))
        pantalla.blit(Rotar,Recto)
    #puntos
    punt=1000
    live=[p.image.load("Nivel 1\\Imagenes\\Vida\\Vida0.png"),p.image.load("Nivel 1\\Imagenes\\Vida\\Vida1.png"),p.image.load("Nivel 1\\Imagenes\\Vida\\Vida2.png"),p.image.load("Nivel 1\\Imagenes\\Vida\\Vida3.png"),p.image.load("Nivel 1\\Imagenes\\Vida\\Vida4.png"),p.image.load("Nivel 1\\Imagenes\\Vida\\Vida5.png"),p.image.load("Nivel 1\\Imagenes\\Vida\\Vida6.png"),p.image.load("Nivel 1\\Imagenes\\Vida\\Vida7.png"),p.image.load("Nivel 1\\Imagenes\\Vida\\Vida8.png"),p.image.load("Nivel 1\\Imagenes\\Vida\\Vida9.png"),p.image.load("Nivel 1\\Imagenes\\Vida\\Vida10.png"),p.image.load("Nivel 1\\Imagenes\\Vida\\Vida11.png"),p.image.load("Nivel 1\\Imagenes\\Vida\\Vida12.png"),p.image.load("Nivel 1\\Imagenes\\Vida\\cVida0.png")]
    def puntos(score,vida):
        r,g,y,b=0,0,0,0
        puntos=font.render("Puntaje: "+str(score),True,(255,255,255))
        hola=fonttext2.render('Jugador: '+nombre,True,(255,255,255))
        pantalla.blit(hola,(1010,60))
        pantalla.blit(puntos,(25,25))
        pantalla.blit(live[0],(1000,25))
        if 0<vida<=50:
            r=1
        elif 50<vida<=100:
            r=2
        elif vida>100:
            r=3
        else:
            r=0
        if 150<vida<=200:
            y=4
        elif 200<vida<=250:
            y=5
        elif vida>250:
            y=6
        else:
            y=0
        if 300<vida<=350:
            g=7
        elif 350<vida<=400:
            g=8
        elif vida>400:
            g=9
        else:
            g=0
        if 450<vida<=500:
            b=10
        elif 500<vida<=550:
            b=11
        elif vida>550:
            b=12
        else:
            b=0
        if r>0:
            pantalla.blit(live[r],(1000,25))
        if y>0:
            pantalla.blit(live[y],(1000,25))
        if g>0:
            pantalla.blit(live[g],(1000,25))
        if b>0:
            pantalla.blit(live[b],(1000,25))
    #Enemigos
    v_E=0.3
    n=0
    sprite=0
    en=[p.image.load("Nivel 1\\Imagenes\\Enemigo.png"),p.image.load("Nivel 1\\Imagenes\\Enemigo1.png")]
    coord_E=[random.randint(300,1000),-100,random.randint(300,1000),-100,random.randint(300,1000),-100]
    def enemy(n,coord_E,s):
        if n==1:
            pantalla.blit(en[s//75],(int(coord_E[0]),int(coord_E[1])))
        elif n==2:
            pantalla.blit(en[s//75],(int(coord_E[0]),int(coord_E[1])))
            pantalla.blit(en[s//75],(int(coord_E[2]),int(coord_E[3])))
        elif n==3:
            pantalla.blit(en[s//75],(int(coord_E[0]),int(coord_E[1])))
            pantalla.blit(en[s//75],(int(coord_E[2]),int(coord_E[3])))
            pantalla.blit(en[s//75],(int(coord_E[4]),int(coord_E[5])))
    def distancia(x1,y1,x2,y2):
        distancia=m.sqrt((x1-x2)**2+(y1-y2)**2)
        if distancia<=100:
            return True
    #Power ups
    podertxt=fontp.render("Poder",True,(255,0,0))
    p_u=p.image.load("Nivel 1\\Imagenes\\P1.png")
    salud=[p.image.load("Nivel 1\\Imagenes\\H.png"),p.image.load("Nivel 1\\Imagenes\\H1.png"),p.image.load("Nivel 1\\Imagenes\\H2.png"),p.image.load("Nivel 1\\Imagenes\\H3.png"),p.image.load("Nivel 1\\Imagenes\\H4.png"),p.image.load("Nivel 1\\Imagenes\\H5.png"),p.image.load("Nivel 1\\Imagenes\\H6.png"),p.image.load("Nivel 1\\Imagenes\\H7.png")]
    numsalud=0
    coord_p_u=[random.randint(300,1000),-300,random.randint(300,1000),-300,1000,1000]
    k=False
    s=False
    def Powers(s,a,k):
        if k:
            pantalla.blit(p_u,(int(a[0]),int(a[1])))
        elif s:
            pantalla.blit(salud[numsalud//10],(int(a[2]),int(a[3])))
    ##Torretasd
    disparo1,disparo2=False,False
    Tiempo_t=0
    dt=0
    act=False
    t_v=False
    b=random.randint(0,2)
    if b==1:
        c=2
    elif b==2:
        c=0
    elif b==0:
        c=1
    ent_torr1=[1400,640,-100]
    x1,y1=1200,640
    x2,y2=100,640
    v=6
    def poder(a,b,x1,x2,y1,y2):
        c=4
        if b==1:
            c=2
        elif b==2:
            c=0
        elif b==0:
            c=1
        if a[2*b+1]!=0:
            angulo1=-180*m.atan((640-(a[2*b+1]+50))/(1200-(a[2*b]-40)))/m.pi+180
            angulo2=180*m.atan((640-(a[2*c+1]+50))/((a[2*c]+40)-100))/m.pi
        else:
            angulo1=0
            angulo2=0
        disparar(angulo1,x1,y1)
        disparar(angulo2,x2,y2)
        Rotar1=p.transform.rotozoom(torreta,angulo1,1)
        Recto1=Rotar1.get_rect(center=(int(1200),int(640)))
        Rectobase=Base.get_rect(center=(int(1200),int(640)))
        pantalla.blit(Base,Rectobase)
        pantalla.blit(Rotar1,Recto1)
        Rotar2=p.transform.rotozoom(torreta,angulo2,1)
        Recto2=Rotar2.get_rect(center=(int(100),int(640)))
        Rectobase2=Base.get_rect(center=(int(100),int(640)))
        pantalla.blit(Base,Rectobase2)
        pantalla.blit(Rotar2,Recto2)
        return a[2*b+1],a[2*c+1],c,b
    def entrada(a):
        Rotar1=p.transform.rotozoom(torreta,90,1)
        Recto1=Rotar1.get_rect(center=(int(a[0]),int(a[1])))
        Rotar2=p.transform.rotozoom(torreta,90,1)
        Rectobase=Base.get_rect(center=(int(a[0]),int(a[1])))
        Recto2=Rotar2.get_rect(center=(int(a[2]),int(a[1])))
        Rectobase2=Base.get_rect(center=(int(a[2]),int(a[1])))
        pantalla.blit(Base,Rectobase)
        pantalla.blit(Base,Rectobase2)
        pantalla.blit(Rotar2,Recto2)
        pantalla.blit(Rotar1,Recto1)
    def colisiones_t(a,x,y,r,n):
        colision=False
        distancia=m.sqrt((a[2*n]+40-x)**2+(a[2*n+1]+40-y)**2)
        if distancia<=r:
            colision=True
        return colision
    #Colisiones
    colp=False
    numcolp=0
    def colisiones(n,a,b,r):
        colision=False
        distancia=m.sqrt((a[2*n]+40-b[0])**2+(a[2*n+1]+40-b[1])**2)
        if distancia<=r:
            colision=True
        return colision
    #Explosiones
    explo1=False
    explo2=False
    expb1=False
    expb2=False
    expt=False
    expen=False
    numexpen=0
    xe1,xe2,xe3,ye1,ye2,ye3=0,0,0,0,0,0
    xb1,yb1=0,0
    xb2,yb2=0,0
    xexp,yexp=0,0
    xexp2,yexp2=0,0
    numexp1,numexp2,numexb1,numexb2,numexpe=0,0,0,0,0
    explosion=[p.image.load("Nivel 1\\Imagenes\\Exp\\Exp1.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp2.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp3.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp4.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp5.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp6.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp7.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp8.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp9.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp10.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp11.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp12.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp13.png")]
    def expl(x,y,numexp):
        pantalla.blit(explosion[numexp//6],(int(x),int(y)))
    #Pausa
    Pausa=False

    #Game over
    fin=["Haz perdido, presiona 'enter' para reintentarlo","Puntaje total: ",""]
    muerte=[]
    for i in range(11):
        muerte.append(p.image.load("Nivel 1\\Imagenes\\Muerte\\"+str(i+1)+".png").convert_alpha())
    go=0
    game_over=False
    def G_o(a,i):
        pantalla.blit(muerte[0],(0,0))
        pantalla.blit(muerte[int(i)],(0,0))
        hola=font.render(a[0],True,(255,255,255))
        cent=hola.get_rect(center=(int(1280/2),int(700)))
        pantalla.blit(hola,cent)
    #Variables varias :v
    iniciar_jefe=0
    reset=0
    #Juego :v
    Cinematica=True
    nivel_1=True
    Jefe = True
    while nivel_1:
        p.mouse.set_visible(0)
        while Cinematica:
            nivel_1=Cinematica_1_1.c1()
            Cinematica_1_1.controles()
            Cinematica=False
            Introduccion=["Hola "+nombre+", he sido asignada para", "enviar instrucciones a tu escuadrón.", "Los enemigos de la Far quieren acabar","con nosotros.", "Ten cuidado, ahí vienen, con W, A, S, D","puedes mover la torreta.", "Mientras que con espacio puedes", "dispararla.","con e activar poderes increibles.", "Contamos contigo "+nombre+"..."]
            tutorial=True
        if nivel_1==False:
            break
            return False, False
        for event in p.event.get():
            if event.type== p.QUIT:
                nivel_1=False
                return False, False
            if event.type == p.KEYDOWN:
                if event.key == p.K_d or event.key==p.K_RIGHT:
                    vel=-1
                if event.key == p.K_a or event.key==p.K_LEFT:
                    vel=1
                if event.key==p.K_SPACE:
                    if i==0:
                        if B[0]=="Invisible":
                            channel3.play(sonidob)
                            B[0]="Visible"
                            a=angulo
                            coord_b[0],coord_b[1]=coord_p[0],coord_p[1]
                    elif i==1:
                        if B[1]=="Invisible":
                            channel3.play(sonidob)
                            B[1]="Visible"
                            a1=angulo
                            coord_b1[0],coord_b1[1]=coord_p[0],coord_p[1]
                if event.key==p.K_e or event.key==p.K_RETURN:
                    if t_v:
                        if not act:
                            dt=1
                            act=True
                            t_v=False
                if event.key==p.K_ESCAPE:
                    if Pausa==False:
                        mixer.music.pause()
                        canalpausa.unpause()
                        Pausa=True
            if event.type==p.KEYUP:
                if event.key == p.K_a or event.key == p.K_d or event.key==p.K_LEFT or event.key==p.K_RIGHT:
                    vel=0
        while tutorial:
            p.mouse.set_visible(0)
            pantalla.blit(fondo,cfondo)
            for event in p.event.get():
                if event.type== p.QUIT:
                    tutorial=False
                    nivel_1=False
                if event.type == p.KEYDOWN:
                    if event.key == p.K_d or event.key==p.K_RIGHT:
                        vel=-1
                    if event.key == p.K_a or event.key==p.K_LEFT:
                        vel=1
                    if event.key==p.K_SPACE:
                        if i==0:
                            if B[0]=="Invisible":
                                channel3.play(sonidob)
                                B[0]="Visible"
                                a=angulo
                                coord_b[0],coord_b[1]=coord_p[0],coord_p[1]
                        elif i==1:
                            if B[1]=="Invisible":
                                channel3.play(sonidob)
                                B[1]="Visible"
                                a1=angulo
                                coord_b1[0],coord_b1[1]=coord_p[0],coord_p[1]
                    elif event.key==p.K_ESCAPE:
                        if Pausa==False:
                            mixer.music.pause()
                            canalpausa.unpause()
                            Pausa=True
                    elif event.key==p.K_RETURN:
                        if not avisar:
                            avs=True
                            avisar=True
                        else:
                            countintro=1000 
                if event.type==p.KEYUP:
                    if event.key == p.K_a or event.key == p.K_d or event.key==p.K_LEFT or event.key==p.K_RIGHT:
                        vel=0
            clock.tick(300)
            name(Titulo)
            if countintro<1000:
                if countintro<-1:
                    pantalla.blit(senora[int((countintro+100)//10)],(-5,580))
                    p.draw.rect(pantalla,(0,0,0),(120,600,int(int(countintro+100)*450/100),int(int(countintro+100)*170/100)))
                    countintro+=1
                else:
                    pantalla.blit(senora[9],(-5,580))
                    p.draw.rect(pantalla,(0,0,0),(120,600,450,170))
                    countintro+=0.2
                if 0<=countintro<200:
                    if k1<len(Introduccion[0]):
                        k1+=0.1
                    else:
                        if k2<len(Introduccion[1]):
                            k2+=0.1
                    torrecontrol(0,k1,k2)
                elif 200<countintro<400:
                    if activar:
                        k1,k2=0,0
                        activar=False
                    if k1<len(Introduccion[2]):
                        k1+=0.1
                    else:
                        if k2<len(Introduccion[3]):
                            k2+=0.1
                    torrecontrol(2,k1,k2)
                elif 400<countintro<600:
                    if activar2:
                        k1,k2=0,0
                        activar2=False
                    if k1<len(Introduccion[4]):
                        k1+=0.1
                    else:
                        if k2<len(Introduccion[5]):
                            k2+=0.1
                    torrecontrol(4,k1,k2)
                elif 600<countintro<800:
                    if activar3:
                        k1,k2=0,0
                        activar3=False
                    if k1<len(Introduccion[6]):
                        k1+=0.1
                    else:
                        if k2<len(Introduccion[7]):
                            k2+=0.1
                    torrecontrol(6,k1,k2)
                elif 800<countintro<1000:
                    if activar4:
                        k1,k2=0,0
                        activar4=False
                    if k1<len(Introduccion[8]):
                        k1+=0.1
                    else:
                        if k2<len(Introduccion[9]):
                            k2+=0.1
                    torrecontrol(8,k1,k2)
            else:
                tutorial=False
            if avs:
                pantalla.blit(fonttext2.render("Presiona 'enter' para omitir.",True,(255,255,255)),(100,570))
            if angulo<0:
                angulo=0
                vel=0
            elif angulo>180:
                angulo=180
                vel=0
            else:
                angulo+=vel
            if B[0]=="Visible":
                if 800>=coord_b[1]>=0 and 1350>=coord_b[0]>=0:
                    coord_b[1]-=vel_b*m.sin((a*m.pi)/180)
                    coord_b[0]+=vel_b*m.cos((a*m.pi)/180)
                    disparar(a,coord_b[0],coord_b[1])
                else:
                    B[0]="Invisible"
                    coord_b=[-1000,-1000]
            #Bala 2
            if B[1]=="Visible":
                if 800>=coord_b1[1]>=0 and 1350>=coord_b1[0]>=0:
                    coord_b1[1]-=vel_b*m.sin((a1*m.pi)/180)
                    coord_b1[0]+=vel_b*m.cos((a1*m.pi)/180)
                    disparar(a1,coord_b1[0],coord_b1[1])
                else:
                    B[1]="Invisible"
                    coord_b1=[-1000,-1000]
            if coord_b[1]>=0:
                if m.sqrt((coord_b[1]-coord_p[1])**2+(coord_b[0]-coord_p[0])**2)>=r:
                    i=1
            else:
                i=0
            pantalla.blit(podertxt,(1010,680))
            p.draw.rect(pantalla,(int(255/2),int(255/2),int(255/2)),(990,600,140,80))
            p.draw.rect(pantalla,(0,0,0),(990,600,140,80),4)
            puntos(score,vida)
            torret(angulo,coord_p[0],coord_p[1])
            p.display.update()
            while Pausa:
                menu=Cinematica_1_1.pause()
                Pausa=False
                canalpausa.pause()
                mixer.music.unpause()
                if menu:
                    nivel_1=False
                    tutorial=False
                    mixer.music.stop()
                    return True, False
                p.display.update()
        #Fin tutorial
        pantalla.blit(fondo,cfondo)
        clock.tick(300)
        name(Titulo)
        if cambiofase:
            if x_f<=x/2 and 0<=fasecount<=500/3:
                x_f+=10
            elif 500/3<fasecount<=2*500/3:
                x_f+=0
            elif fasecount>=2*500/3:
                x_f+=10
            if fasecount<=500:
                ola(numfase,x_f)
                fasecount+=1
            else:
                fasecount=0
                cambiofase=False
                x_f=-300
        #Movimiento de la torreta            
        if angulo<0:
            angulo=0
            vel=0
        elif angulo>180:
            angulo=180
            vel=0
        else:
            angulo+=vel
        #disparo de la torreta alv
        #Bala 1
        if B[0]=="Visible":
            if 800>=coord_b[1]>=0 and 1350>=coord_b[0]>=0:
                coord_b[1]-=vel_b*m.sin((a*m.pi)/180)
                coord_b[0]+=vel_b*m.cos((a*m.pi)/180)
                disparar(a,coord_b[0],coord_b[1])
            else:
                B[0]="Invisible"
                coord_b=[-1000,-1000]
        #Bala 2
        if B[1]=="Visible":
            if 800>=coord_b1[1]>=0 and 1350>=coord_b1[0]>=0:
                coord_b1[1]-=vel_b*m.sin((a1*m.pi)/180)
                coord_b1[0]+=vel_b*m.cos((a1*m.pi)/180)
                disparar(a1,coord_b1[0],coord_b1[1])
            else:
                B[1]="Invisible"
                coord_b1=[-1000,-1000]
        if coord_b[1]>=0:
            if m.sqrt((coord_b[1]-coord_p[1])**2+(coord_b[0]-coord_p[0])**2)>=r:
                i=1
        else:
            i=0
        #Num enemigos
        if 0<=score<4000:
            if n==0:
                numfase=0
                coord_E=[random.randint(300,1000),-100,random.randint(300,1000),-100,random.randint(300,1000),-100]
            n=1
        elif 4000<=score<16000:
            if n==1:
                expen=True
                cambiofase=True
                numfase=1
                xe1,xe2,xe3,ye1,ye2,ye3=coord_E[0],coord_E[2],coord_E[4],coord_E[1],coord_E[3],coord_E[5]
                coord_E=[random.randint(300,1000),-100,random.randint(300,1000),-100,random.randint(300,1000),-100]
            n=2
            v_E=0.5
        elif 16000<=score<40000:
            if n==2:
                expen=True
                cambiofase=True
                numfase=2
                xe1,xe2,xe3,ye1,ye2,ye3=coord_E[0],coord_E[2],coord_E[4],coord_E[1],coord_E[3],coord_E[5]
                coord_E=[random.randint(300,1000),-100,random.randint(300,1000),-100,random.randint(300,1000),-100]
            n=3
            v_E=0.7
        if score>=40000:
            if n==3:
                expen=True
                cambiofase=True
                numfase=3
                xe1,xe2,xe3,ye1,ye2,ye3=coord_E[0],coord_E[2],coord_E[4],coord_E[1],coord_E[3],coord_E[5]
            n=4
            Jefe=True
        else:
            Jefe=False
        if Jefe:
            if iniciar_jefe>=250:
                while Jefe:
                    reset,nivel_1,win,menu=Nivel_1_Jefe.J(score,vida,nombre,t_v,act,ent_torr1,Tiempo_t,dt)
                    break
                if menu:
                    mixer.music.stop()
                    return True, False
                if win:
                    nivel_1=Cinematica_1_1.c2()
                    if not nivel_1:
                        return False, win
                if nivel_1 and win:
                    mixer.music.stop()
                    return True, win
                elif not nivel_1:
                    return False, win
            else:
                iniciar_jefe+=1
        if reset==1:
            Spausa=mixer.Sound("Sonidos\\SpacyLoop.ogg")
            canalpausa.play(Spausa,-1)
            canalpausa.pause()
            vida=300
            score=0
            n=0
            v_E=0.3
            t_v=False
            reset=0
        #Poderes
        if score == 4000 or score == 12000 or score == 24000:
            s=True
        elif score == 20000:
            k=True
        if coord_p_u[1]>=800 and k==True:
            k=False
            coord_p_u[1]=-300
        elif k==True:
            coord_p_u[1]+=0.5
        if coord_p_u[3]>=800 and s==True:
            s=False
            coord_p_u[3]=-300
        elif s==True:
            coord_p_u[3]+=0.5
        if s:
            if numsalud<=8*10-2:
                numsalud+=1
            else:
                numsalud=0
        Powers(s,coord_p_u,k) 
        #colisiones poderes
        if k:
            if colisiones(0,coord_p_u,coord_b,50):
                k=False
                t_v=True
                coord_p_u[1]=-300
            if colisiones(0,coord_p_u,coord_b1,50):
                k=False
                t_v=True
                coord_p_u[1]=-300
        if s:
            if colisiones(1,coord_p_u,coord_b,50):
                s=False
                channel1.play(saluds)
                vida+=50
                coord_p_u[3]=-300
            if colisiones(1,coord_p_u,coord_b1,50):
                s=False
                channel1.play(saluds)
                vida+=50
                coord_p_u[3]=-300
        #Enemigo
        if sprite<=2*75-2:
            sprite+=1
        else:
            sprite=0
        if n>0.5:
            if coord_E[1]<=800:
                coord_E[1]+=v_E
                enemy(n,coord_E,sprite)
            else:
                vida-=50
                coord_E[0],coord_E[1]=random.randint(300,1000),-100
        if n>1.5:
            if coord_E[3]<=800:
                coord_E[3]+=v_E
                enemy(n,coord_E,sprite)
            else:
                vida-=50
                coord_E[2],coord_E[3]=random.randint(300,1000),-100
        if n>2.5:
            if coord_E[5]<=800:
                coord_E[5]+=v_E
                enemy(n,coord_E,sprite)
            else:
                vida-=50
                coord_E[4],coord_E[5]=random.randint(300,1000),-100
        #Colisiones 1
        if colisiones(0,coord_E,coord_b,40)==True:
            xb1,yb1= coord_E[0],coord_E[1]
            expb1=True
            #print("Bala 1 de la torreta central")
            coord_b=[-100,-200]
            B[0]="Invisible"
            i=1
            score+=punt
            coord_E[0],coord_E[1]=random.randint(300,1000),-100
        if colisiones(0,coord_E,coord_b1,40)==True:
            xb2,yb2= coord_E[0],coord_E[1]
            expb2=True
            #print("Bala 2 de la torreta central")
            coord_b1=[-1000,-1000]
            B[1]="Invisible"
            i=0
            score+=punt
            coord_E[0],coord_E[1]=random.randint(300,1000),-100
        #Colisiones 2
        if colisiones(1,coord_E,coord_b,40)==True:
            xb1,yb1= coord_E[1*2],coord_E[1*2+1]
            expb1=True
            #print("Bala 1 de la torreta central")
            coord_b=[-1000,-1000]
            B[0]="Invisible"
            i=1
            score+=punt
            coord_E[2],coord_E[3]=random.randint(300,1000),-100
        if colisiones(1,coord_E,coord_b1,40)==True:
            xb2,yb2= coord_E[1*2],coord_E[1*2+1]
            expb2=True
            #print("Bala 2 de la torreta central")
            coord_b1=[-1000,-1000]
            B[1]="Invisible"
            i=0
            score+=punt
            coord_E[2],coord_E[3]=random.randint(300,1000),-100
        #Colisiones 3
        if colisiones(2,coord_E,coord_b,40)==True:
            xb1,yb1= coord_E[2*2],coord_E[2*2+1]
            #print("Bala 1 de la torreta central")
            expb1=True
            coord_b=[-1000,-1000]
            B[0]="Invisible"
            i=1
            score+=punt
            coord_E[4],coord_E[5]=random.randint(300,1000),-100
        if colisiones(2,coord_E,coord_b1,40)==True:
            xb2,yb2= coord_E[2*2],coord_E[2*2+1]
            expb2=True
            coord_b1=[-1000,-1000]
            #print("Bala 2 de la torreta central")
            B[1]="Invisible"
            i=0
            score+=punt
            coord_E[4],coord_E[5]=random.randint(300,1000),-100
        #Colisión torreta
        if colisiones(0,coord_E,coord_p,100):
            colp=True
            expt=True
            coord_E[0],coord_E[1]=random.randint(300,1000),-100
            vida-=50
        if colisiones(1,coord_E,coord_p,100):
            expt=True
            colp=True
            coord_E[2],coord_E[3]=random.randint(300,1000),-100
            vida-=50
        if colisiones(2,coord_E,coord_p,100):
            expt=True
            colp=True
            coord_E[4],coord_E[5]=random.randint(300,1000),-100
            vida-=50
        #p.draw.rect(pantalla,(255,0,0),(0,400,1000,100),0)
        #Poder torretas
        pantalla.blit(podertxt,(1010,680))
        p.draw.rect(pantalla,(int(255/2),int(255/2),int(255/2)),(990,600,140,80))
        p.draw.rect(pantalla,(0,0,0),(990,600,140,80),4)
        if t_v:
            coord_p_u[4],coord_p_u[5]=1000,600
            pantalla.blit(p_u,(coord_p_u[4],coord_p_u[5]))
        if act:
            if ent_torr1[2]>=100 and ent_torr1[0]<=1200:
                c1,c2,c,b=poder(coord_E,b,x1,x2,y1,y2)
                if abs(1200-coord_E[2*b])>=640:
                    angulo1=m.atan((640-(coord_E[2*b+1]+40))/(1200-(coord_E[2*b]-40)))
                else:
                    angulo1=m.atan((640-(coord_E[2*b+1]))/(1200-(coord_E[2*b]-40)))
                angulo2=m.atan((640-(coord_E[2*c+1]+40))/((coord_E[2*c]+40)-100))
                if c1>=200:
                    if 200<=c1<=201:
                        disparo1=True
                    x1-=v*m.cos(angulo1)
                    y1-=v*m.sin(angulo1)
                else:
                    x1,y1=1200,640
                if c2>=200:
                    if 200<=c2<=201:
                        disparo2=True
                    x2+=v*m.cos(angulo2)
                    y2-=v*m.sin(angulo2)
                else:
                    x2,y2=100,640
            else:
                ent_torr1[0]-=0.5
                ent_torr1[2]+=0.5
                entrada(ent_torr1)
        #Sonidos
        if disparo1 or disparo2:
            channel3.play(sonidob)
            disparo1,disparo2=False,False
        #Colision torretas
        if colisiones_t(coord_E,x1,y1,50,b):
            xexp=coord_E[2*b]
            yexp=coord_E[2*b+1]
            coord_E[2*b],coord_E[2*b+1]=random.randint(300,1000),-100
            score+=punt
            x1,y1=-100,-100
            #print("Bala Torreta 1")
            explo1=True
        if colisiones_t(coord_E,x2,y2,50,c):
            xexp2=coord_E[2*c]
            yexp2=coord_E[2*c+1]
            coord_E[2*c],coord_E[2*c+1]=random.randint(300,1000),-100
            score+=punt
            x2,y2=-100,-100
            #print("Bala Torreta 2")
            explo2=True
        Tiempo_t+=dt
        if Tiempo_t>=2600:
            if ent_torr1[2]>=-100 and ent_torr1[0]<=1400:
                act=False
                ent_torr1[0]+=0.5
                ent_torr1[2]-=0.5
                entrada(ent_torr1)
                if ent_torr1[2]==-100 and ent_torr1[0]==1400:
                    Tiempo_t=0
                    dt=0
        puntos(score,vida)
        torret(angulo,coord_p[0],coord_p[1])
        #Perder
        if vida<=0:
            game_over=True
            canallose.play(lose)
        #Explosiones
        if explo1:
            expl(xexp,yexp,numexp1)
            if numexp1<=7:
                channel2.play(exps)
            if numexp1<=13*6-2:
                numexp1+=1
            else:
                explo1=False
                numexp1=0
        if explo2:
            expl(xexp2,yexp2,numexp2)
            if numexp2<=7:
                channel2.play(exps)
            if numexp2<=13*6-2:
                numexp2+=1
            else:
                explo2=False
                numexp2=0
        if expb1:
            expl(xb1,yb1,numexb1)
            if numexb1<=7:
                channel2.play(exps)
            if numexb1<=13*6-2:
                numexb1+=1
            else:
                expb1=False
                numexb1=0
        if expb2:
            expl(xb2,yb2,numexb2)
            if numexb2<=7:
                channel2.play(exps)
            if numexb2<=13*6-2:
                numexb2+=1
            else:
                expb2=False
                numexb2=0 
        if expt:
            expl(coord_p[0]-30,coord_p[1]-30,numexpe)
            if numexpe<=7:
                channel2.play(exps)
            if numexpe<=13*6-2:
                numexpe+=1
            else:
                numexpe=0
                expt=False 
        if expen:
            expl(xe1,ye1,numexpen)
            expl(xe2,ye2,numexpen)
            expl(xe3,ye3,numexpen)
            if numexpen<=13*6-2:
                numexpen+=1
            if numexpen<=7:
                channel2.play(exps)
            else:
                numexpen=0
                expen=False 
        if colp:
            if numcolp<=7:
                pantalla.blit(live[-1],(1000,25))
                numcolp+=1
            else:
                numcolp=0
                colp=False
        if distancia(coord_E[0],coord_E[1],coord_E[2],coord_E[3]):
            coord_E[0]=random.randint(300,1000)
        if distancia(coord_E[0],coord_E[1],coord_E[4],coord_E[5]):
            coord_E[0]=random.randint(300,1000)
        if distancia(coord_E[4],coord_E[5],coord_E[2],coord_E[3]):
            coord_E[2]=random.randint(300,1000)
        while Pausa:
            menu=Cinematica_1_1.pause()
            Pausa=False
            canalpausa.pause()
            mixer.music.unpause()
            if menu:
                nivel_1=False
                mixer.music.stop()
                return True,False
            p.display.update()
        while game_over:
            mixer.music.pause()
            G_o(fin,go)
            if go<10:
                go+=0.3
            for event in p.event.get():
                if event.type== p.QUIT:
                    game_over=False
                    nivel_1=False
                if event.type == p.KEYDOWN:
                    if event.key == p.K_RETURN:
                        mixer.music.unpause()
                        vida=300
                        score=0
                        n=0
                        v_E=0.3
                        t_v=False
                        if game_over==True:
                            game_over=False
            p.display.update()
        p.display.update()