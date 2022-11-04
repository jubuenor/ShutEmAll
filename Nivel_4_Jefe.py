import random as r
import math as m
import numpy as np
import pygame as p
from pygame import mixer
import sys
import Cinematica_1_1
def Jefe_4(vida=300,score=1000):
    info = open("Guardado.txt", "r")
    text=info.readline().replace("\n","")
    info.close()
    info=open(text+".txt","r")
    nombre = str(info.readline()).replace("\n","")
    puntaje = int(info.readline().replace("\n",""))
    nvl=int(info.readline().replace("\n",""))
    scorei=int(info.readline().replace("\n",""))
    info.close()
    p.init() #Iniciar programa
    Icono = p.image.load('Nivel 4\\Imagenes\\Icono.png')
    p.display.set_icon(Icono)
    clock = p.time.Clock()
    vida0=vida
    
    #Pantalla
    x=1280
    y=720
    pantalla = p.display.set_mode((x,y))
    p.display.set_caption("Shut 'em all")
    fondo=p.image.load("Nivel 4\\Imagenes\\Fondo.png").convert()
    cfondo=fondo.get_rect(center=(int(x/2),int(y/2)))


    #Fonts
    font=p.font.Font('Nivel 4\\Fuentes\\BLADRMF_.TTF',28)
    font1=p.font.Font('Nivel 4\\Fuentes\\BLADRMF_.TTF',15)
    fonttext=p.font.Font('Nivel 4\\Fuentes\\Timeless-Bold.ttf',40)
    fonttext2=p.font.Font('Nivel 4\\Fuentes\\Timeless-Bold.ttf',25)


    #Titulos :v pa pa pa
    Titulo="Nivel 4: The end of the line"
    live=[p.image.load("Nivel 4\\Imagenes\\Vida\\Vida0.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida1.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida2.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida3.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida4.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida5.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida6.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida7.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida8.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida9.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida10.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida11.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida12.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\cVida0.png")]
    def name():
        hola=fonttext.render(Titulo,True,(255,255,255))
        cent=hola.get_rect(center=(int(x/2),50))
        pantalla.blit(hola,cent)
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
    class Img:
        def __init__(self,a):
            self.ubicacion=a
        def img(self):
            return p.image.load("Nivel 4\\Imagenes\\"+self.ubicacion).convert_alpha()

    #Sonido
    Trueno=mixer.Sound("Nivel 4\\Sonidos\\Thunder.wav")
    Electricidad=mixer.Sound("Nivel 4\\Sonidos\\Electricidad.wav")
    Bomba=mixer.Sound("Nivel 4\\Sonidos\\Bomba.wav")
    Cambio=mixer.Sound("Nivel 4\\Sonidos\\Cambio.wav")
    Balas=mixer.Sound("Nivel 4\\Sonidos\\Bala.wav")
    Horn=mixer.Sound("Nivel 4\\Sonidos\\Scary Sound2.wav")
    Dragon=mixer.Sound("Nivel 4\\Sonidos\\dragon_attack_01.ogg")
    navesound=mixer.Sound("Nivel 4\\Sonidos\\boom7.wav")
    Expbomb=mixer.Sound("Nivel 4\\Sonidos\\boom1.wav")
    Salud=mixer.Sound("Nivel 4\\Sonidos\\Salud.wav")
    Fuego=mixer.Sound("Nivel 4\\Sonidos\\FIRELOOP.wav")
    DJ4=mixer.Sound("Nivel 4\\Sonidos\\DJ4.wav")
    teleportsound=mixer.Sound("Nivel 4\\Sonidos\\tesla_tower.ogg")
    Spausa=mixer.Sound("Sonidos\\SpacyLoop.ogg")
    lose=mixer.Sound("Sonidos\\lose music.ogg")
    mixer.music.load("Nivel 4\\Sonidos\\Juhani Junkala - Epic Boss Battle.wav")
    mixer.music.play(-1)
    mixer.music.set_volume(0.25)
    inicio=True
    mixer.set_num_channels(11)
    canal1=mixer.Channel(1)
    canal1.set_volume(0.3)
    canal2=mixer.Channel(0)
    canal2.set_volume(0.3)
    canal3=mixer.Channel(2)
    canal3.set_volume(0.3)
    canalbala=mixer.Channel(3)
    canalbala.set_volume(0.3)
    canalnave=mixer.Channel(4)
    canalnave.set_volume(0.3)
    canalsalud=mixer.Channel(5)
    canalfuego=mixer.Channel(6)
    canaldisparo4=mixer.Channel(7)
    canaltele=mixer.Channel(8)
    canalfuego.play(Fuego,-1)
    canalfuego.pause()
    canalpausa=mixer.Channel(9)
    canalpausa.set_volume(0.3)
    canalpausa.play(Spausa,-1)
    canallose=mixer.Channel(10)
    canalpausa.pause()

    #Rayos
    rayo=False
    numrayo=0   

    #Jefe
    vidaJ=24000
    Vida=[p.image.load("Nivel 4\\Imagenes\\Vida\\cVidaj.png")]
    for i in range(13):
        ub="Vida\\Vidaj"
        ub+=str(i)+".png"
        im=Img(ub)
        Vida.append(im.img())

    def mostrar(x,y,im,a=0):
        imr=p.transform.rotozoom(im,a,1)
        centro=imr.get_rect(center=(int(x),int(y)))
        pantalla.blit(imr,centro)

    def saludJ(vidaJ):
        mostrar(x/2,700,Vida[1])
        r,g,y,b=0,0,0,0
        if 0<vidaJ<=2000:
            r=1
        elif 2000<vidaJ<=4000:
            r=2
        elif 4000<vidaJ:
            r=3
        else:
            r=0
        if 6000<vidaJ<=4*2000:
            y=4
        elif 4*2000<vidaJ<=5*2000:
            y=5
        elif 10000<vidaJ:
            y=6
        else:
            y=0
        if 12000<vidaJ<=14000:
            g=7
        elif 14000<vidaJ<=16000:
            g=8
        elif 16000<vidaJ:
            g=9
        else:
            g=0
        if 18000<vidaJ<=20000:
            b=10
        elif 20000<vidaJ<=22000:
            b=11
        elif 22000<vidaJ:
            b=12
        else:
            b=0
        if r>0:
            mostrar(x/2,700,Vida[r+1])
        if y>0:
            mostrar(x/2,700,Vida[y+1]) 
        if g>0:
            mostrar(x/2,700,Vida[g+1])
        if b>0:
            mostrar(x/2,700,Vida[b+1])
        Nombre=font1.render("Castro Chavistas",True,(255,255,255))
        cnombre=Nombre.get_rect(center=(int(1280/2),int(700)))
        pantalla.blit(Nombre,cnombre)
    a1=Img("Jefe\\Jefe1.png")
    b=Img("Jefe\\cJefe1.png")
    a3=Img("Jefe\\Jefe3.png")
    b3=Img("Jefe\\cJefe3.png")
    inv3=Img("Jefe\\inJefe3.png")
    injefe1=Img("Jefe\\inJefe1.png")
    injefe2=Img("Jefe\\inJefe2.png")
    jefe2=Img("Jefe\\Jefe2.png")
    cjefe2=Img("Jefe\\cJefe2.png")
    ojo2=Img("Jefe\\OjoJefe2.png")
    cojo2=Img("Jefe\\cOjoJefe2.png")
    ojo=[ojo2.img(),cojo2.img()]
    Jefe=[a1.img(),b.img(),jefe2.img(),cjefe2.img(),injefe1.img(),injefe2.img()]
    Jefe3=[a3.img(),b3.img(),inv3.img()]
    Jefe4=[Img("Jefe\\Jefe4.png").img(),Img("Jefe\\cJefe4.png").img(),Img("Jefe\\inJefe4.png").img()]

    #Corazon
    Heart=[]
    xheart=[r.randint(1500,3000),r.randint(1500,3000),r.randint(1500,3000)]
    yheart=[r.randint(100,620),r.randint(100,620),r.randint(100,620)]
    countheart=0
    def colision_corazon(x1,y1,x2,y2):
        if (x1-x2)**2+(y1-y2)**2<40**2:
            return True
        else:
            return False
    for i in range(8):
        ub="Corazon\\"
        ub+=str(i+1)+".png"
        im=Img(ub)
        Heart.append(im.img())


    #Nave
    #fase 1
    veld,veli=0,0
    a=m.pi


    #Explosiones
    obja=Img("Objetivoa.png").img()
    anguloobja=r.uniform(0,2*m.pi)
    numobjs=10
    cambiar=0
    objr=Img("Objetivor.png").img()
    fijarr=0
    coordsobj=[300*m.cos(anguloobja)+x/2,300*m.sin(anguloobja)+y/2,300*m.cos(anguloobja+2*m.pi/numobjs)+x/2,300*m.sin(anguloobja+2*m.pi/numobjs)+y/2,300*m.cos(anguloobja+4*m.pi/numobjs)+x/2,300*m.sin(anguloobja+4*m.pi/numobjs)+y/2,300*m.cos(anguloobja+6*m.pi/numobjs)+x/2,300*m.sin(anguloobja+6*m.pi/numobjs)+y/2,300*m.cos(anguloobja+8*m.pi/numobjs)+x/2,300*m.sin(anguloobja+8*m.pi/numobjs)+y/2,300*m.cos(anguloobja+10*m.pi/numobjs)+x/2,300*m.sin(anguloobja+10*m.pi/numobjs)+y/2,300*m.cos(anguloobja+12*m.pi/numobjs)+x/2,300*m.sin(anguloobja+12*m.pi/numobjs)+y/2,300*m.cos(anguloobja+14*m.pi/numobjs)+x/2,300*m.sin(anguloobja+14*m.pi/numobjs)+y/2,300*m.cos(anguloobja+16*m.pi/numobjs)+x/2,300*m.sin(anguloobja+16*m.pi/numobjs)+y/2,300*m.cos(anguloobja+18*m.pi/numobjs)+x/2,300*m.sin(anguloobja+18*m.pi/numobjs)+y/2]
    def objetivo1(a):
        mostrar(a[0],a[1],obja)
        mostrar(a[2],a[3],obja)
        mostrar(a[4],a[5],obja)
        mostrar(a[6],a[7],obja)
        mostrar(a[8],a[9],obja)
        mostrar(a[10],a[11],obja)
        mostrar(a[12],a[13],obja)
        mostrar(a[14],a[15],obja)
        mostrar(a[16],a[17],obja)
        mostrar(a[18],a[19],obja)
    Explo=[]
    arma1=Img("ArmaJefe1.png").img()
    for i in range(1,8):
        ub="Explo\\explo"
        ub+=str(i)+".png"
        im=Img(ub)
        Explo.append(im.img())
    cexp=0
    dx=30/5
    invencible=False
    xfijar=x/2
    yfijar=y/2
    def explos(a,k):
        mostrar(a[0],a[1],Explo[k//3])
        mostrar(a[2],a[3],Explo[k//3])
        mostrar(a[4],a[5],Explo[k//3])
        mostrar(a[6],a[7],Explo[k//3])
        mostrar(a[8],a[9],Explo[k//3])
        mostrar(a[10],a[11],Explo[k//3])
        mostrar(a[12],a[13],Explo[k//3])
        mostrar(a[14],a[15],Explo[k//3])
        mostrar(a[16],a[17],Explo[k//3])
        mostrar(a[18],a[19],Explo[k//3])
    endf1=False
    xj=x/2


    #fase 2
    endf2=False
    numinv2=0
    arma2=Img("dragonarma.png").img()
    angle=0
    xe=-700
    xe1=1280+700
    xp,yp,velx,vely,velx1,vely1=x/2,y/2,0,0,0,0
    coords=[xp,yp]
    Nave=[]
    k=31
    for i in range(1,61):
        ub="NaveSprite\\"
        ub+=str(i)+".png"
        im=Img(ub)
        Nave.append(im.img())
    def nave(a,x,y,i):
        nave=p.transform.rotozoom(Nave[i],a,1)
        cnave=nave.get_rect(center=(int(x),int(y)))
        pantalla.blit(nave,cnave)


    #Armas Jefe
    xder=1330
    xizq=-50
    vels=8
    yizq=[]
    yder=[]
    for i in range(5):
        yizq.append(r.randint(150,570))
        yder.append(r.randint(150,570))
    bomba=Img("Bomba.png").img()
    def Shuriken(x1,x2,y1,y2,a):
        mostrar(x1,y1[0],arma2,a)
        mostrar(x1,y1[1],arma2,a)
        mostrar(x1,y1[2],arma2,a)
        mostrar(x1,y1[3],arma2,a)
        mostrar(x1,y1[4],arma2,a)
        mostrar(x2,y2[0],arma2,a)
        mostrar(x2,y2[1],arma2,a)
        mostrar(x2,y2[2],arma2,a)
        mostrar(x2,y2[3],arma2,a)
        mostrar(x2,y2[4],arma2,a)


    #Fase3
    endf3=False
    entrada3=True
    yj3=720+360
    laser=Img("BalaJefe3.png").img()
    xbj31=1280
    Bombas=[]
    for i in range(20):
        ub="Bombas\\"
        ub+=str(i)+".png"
        im=Img(ub)
        Bombas.append(im.img())
    excl=[Img("excl.png").img(),Img("excl1.png").img()]
    boom=[]
    for i in range(8):
        ub="Boom\\"
        ub+=str(i)+".png"
        im=Img(ub)
        boom.append(im.img())
    bombitas=[]
    xbombi=1280/2
    ybombi=720
    yboom=0
    t=0
    countbombp=0
    countboom=0
    for i in range(8):
        ub="Bombap\\"
        ub+=str(i)+".png"
        im=Img(ub)
        bombitas.append(im.img())
    rayos=Img("Rayos.png").img()
    xl1=np.array([930,930,930,930,930,930,930,930,930])
    yl1=np.array([480,480,480,480,480,480,480,480,480])
    yl1ref=np.array([])
    actlaser,actlaser2=False,False
    for i in range(0,721,90):
        yl1ref=np.append(yl1ref,480-i)
    angulol1=np.arctan(yl1ref/930)*180/np.pi
    coordsbomby=np.random.randint(50,670,10)
    coordsbombx=np.random.randint(40,500,10)
    countbomb=0


    #Fase 4
    ent4=False
    Salida4=False
    xd=[]
    xup=[]
    yd=[]
    yup=[]
    tf=[]
    yupi=[]
    ydi=[]
    xdi=[]
    xupi=[]
    n=0
    corrimiento1,corrimiento2=-310,1030
    fuego=Img("dragonarma2.png").img()
    for i in range(16):
            xd.append(i*1280/16+40)
            yd.append(0)
            ydi.append(yd[i])
            xdi.append(xd[i])
            xup.append(i*1280/16+40)
            yup.append(0)
            xupi.append(xup[i])
            yupi.append(yup[i])
            tf.append(i)
    Tele=[]
    countT=10
    disparosnave=Img("Disparoj4.png").img()
    coordj=[-1000,-1000,-1000,-1000,-1000,-1000]
    vdj=10
    for i in range(10):
        ub="Teleport\\"
        ub+=str(i)+".png"
        im=Img(ub)
        Tele.append(im.img())
    countT2=-10
    tel=False
    xn,yn=1380,720/2
    tn=0
    vn=3
    disparar=False
    Calavera=[Img("calaveraD.png").img(),Img("calaveraI.png").img()]
    xc,yc=[r.randint(40,1240),r.randint(40,1240)],[-100,820]
    vcx=[5,11]
    vcy=[6,10]


    #colisiones
    col=False
    col1=False
    colb=False
    def colisioness(x1,y1,x2,y2,r=40):
        if x1-r<=x2<=x1+r and y1-r<=y2<=y1+r:
            return True
        else:
            return False


    #Disparos
    numcolj=0
    colision=False
    nb=7
    B=False
    vb=10
    xb,yb=1000,1000
    vbomb=-5
    bala=[]
    for i in range(1,15):
        ub="Misil\\"
        ub+=str(i)+".png"
        im=Img(ub)
        bala.append(im.img())
    def tiro(a,x,y,i=0):
        nave=p.transform.rotozoom(bala[int(i)],a,1)
        cnave=nave.get_rect(center=(int(x),int(y)))
        pantalla.blit(nave,cnave)


    #Pausa y fin
    muy_bien=["Haz  conseguido derrotar al villano, Felicitaciones.","Presiona 'esc' para salir."]
    Pausa=False
    Win=False
    color=0
    wn=0
    cp=0
    ganar=[]
    for i in range(11):
        ganar.append(p.image.load("Nivel 4\\Imagenes\\Ganaste\\"+str(i+1)+".png").convert_alpha())
    def WIN(a,color,i):
        pantalla.blit(ganar[0],(0,0))
        pantalla.blit(ganar[int(i)],(0,0))
        hola=font.render(a[0],True,(color*255,color*255,color*255))
        KK=font.render(a[1],True,(color*255,color*255,color*255))
        centh=hola.get_rect(center=(int(1280/2),int(680-100)))
        centK=KK.get_rect(center=(int(1280/2),int(680)))
        pantalla.blit(hola,centh)
        pantalla.blit(KK,centK)


    #Game over
    fin=["Haz perdido, presiona 'enter' para reintentarlo","Puntaje total: ",""]
    muerte=[]
    for i in range(11):
        muerte.append(p.image.load("Nivel 4\\Imagenes\\Muerte\\"+str(i+1)+".png").convert_alpha())
    game_over=False
    go=0
    def G_o(a,i):
        pantalla.blit(muerte[0],(0,0))
        pantalla.blit(muerte[int(i)],(0,0))
        hola=font.render(a[0],True,(255,255,255))
        cent=hola.get_rect(center=(int(1280/2),int(700)))
        pantalla.blit(hola,cent)


    #Booles de funcionamiento
    nivel_4=True
    Fase1=True
    Fase2=False
    Fase3=False
    Fase4=False
    ############################################################################################################################
    ############################################################################################################################
    ############################################################################################################################
    ############################################################################################################################
    while nivel_4:
        while Fase1:
            p.mouse.set_visible(0)
            for event in p.event.get():
                if event.type== p.QUIT:
                    Fase1=False
                    nivel_4=False
                    sys.exit()
                if event.type == p.KEYDOWN:
                    if event.key == p.K_a:
                        veli=2
                    if event.key==p.K_d:
                        veld=-2
                    if event.key==p.K_SPACE:
                        if B==False:
                            B=True
                            canalbala.play(Balas)
                            xb,yb=coords[0],coords[1]
                            ab=-(a*180/m.pi+180)
                    if event.key==p.K_ESCAPE:
                        if Pausa==False:
                            mixer.music.pause()
                            canalpausa.unpause()
                            Pausa=True
                        else:
                            Pausa=False
                if event.type==p.KEYUP:
                    if event.key == p.K_a:
                        veli=0
                    if event.key == p.K_d:
                        veld=0
            a+=veld*m.pi/180+veli*m.pi/180
            pantalla.blit(fondo,cfondo)
            clock.tick(60)
            mostrar(x/2,y/2,Jefe[0])
            coords=[300*m.cos(a)+x/2,300*m.sin(a)+y/2]
            if cambiar<=100:
                cambiar+=1
                if cambiar<=50:
                    objetivo1(coordsobj)
                    cexp=0
                elif cambiar>=50:
                    if cexp<=14:
                        canal2.play(Electricidad)
                        explos(coordsobj,cexp)
                        cexp+=1
                        if colisioness(coordsobj[0],coordsobj[1],coords[0],coords[1],30) or colisioness(coordsobj[2],coordsobj[3],coords[0],coords[1],30) or colisioness(coordsobj[4],coordsobj[5],coords[0],coords[1],30) or colisioness(coordsobj[6],coordsobj[7],coords[0],coords[1],30) or colisioness(coordsobj[8],coordsobj[9],coords[0],coords[1],30) or colisioness(coordsobj[10],coordsobj[11],coords[0],coords[1],30) or colisioness(coordsobj[12],coordsobj[13],coords[0],coords[1],30) or  colisioness(coordsobj[14],coordsobj[15],coords[0],coords[1],30) or colisioness(coordsobj[16],coordsobj[17],coords[0],coords[1],30) or  colisioness(coordsobj[18],coordsobj[19],coords[0],coords[1],30):
                            col=True
                    else:
                        cexp=0
            else:
                anguloobja=a
                coordsobj=[300*m.cos(anguloobja)+x/2,300*m.sin(anguloobja)+y/2,300*m.cos(anguloobja+2*m.pi/numobjs)+x/2,300*m.sin(anguloobja+2*m.pi/numobjs)+y/2,300*m.cos(anguloobja+4*m.pi/numobjs)+x/2,300*m.sin(anguloobja+4*m.pi/numobjs)+y/2,300*m.cos(anguloobja+6*m.pi/numobjs)+x/2,300*m.sin(anguloobja+6*m.pi/numobjs)+y/2,300*m.cos(anguloobja+8*m.pi/numobjs)+x/2,300*m.sin(anguloobja+8*m.pi/numobjs)+y/2,300*m.cos(anguloobja+10*m.pi/numobjs)+x/2,300*m.sin(anguloobja+10*m.pi/numobjs)+y/2,300*m.cos(anguloobja+12*m.pi/numobjs)+x/2,300*m.sin(anguloobja+12*m.pi/numobjs)+y/2,300*m.cos(anguloobja+14*m.pi/numobjs)+x/2,300*m.sin(anguloobja+14*m.pi/numobjs)+y/2,300*m.cos(anguloobja+16*m.pi/numobjs)+x/2,300*m.sin(anguloobja+16*m.pi/numobjs)+y/2,300*m.cos(anguloobja+18*m.pi/numobjs)+x/2,300*m.sin(anguloobja+18*m.pi/numobjs)+y/2]
                cambiar=0
            if B:
                xb-=vb*m.cos(-(-ab-180)*m.pi/180)
                yb+=vb*m.sin(-(-ab-180)*m.pi/180)
                tiro(ab,xb,yb,nb)
            if m.sqrt((x/2-xb)**2+(y/2-yb)**2)<=80:
                xb,yb=coords[0],coords[1]
                B=False
                if not invencible:
                    vidaJ-=6000/50
                    colision=True
            if invencible:
                mostrar(x/2,y/2,Jefe[4])
            if vidaJ<=21000:
                if fijarr<=400:
                    fijarr+=1
                    if 0<=fijarr<=150:
                        xobjr,yobjr=coords[0],coords[1]
                        mostrar(xobjr,yobjr,objr)
                        a1=a
                    if 150<=fijarr<=200:
                        if 150<=fijarr<=151:
                            canal3.play(mixer.Sound("Nivel 4\\Sonidos\\DJ1.wav"))
                        xfijar+=dx*m.cos(a1)
                        yfijar+=dx*m.sin(a1)
                        invencible=True
                        coordobjr=[xfijar,yfijar]
                        if coordobjr[0]-10<=coords[0]<=coordobjr[0]+10 and coordobjr[1]-10<=coords[1]<=coordobjr[1]+10:
                            col1=True
                        mostrar(coordobjr[0],coordobjr[1],arma1)
                    if fijarr>300:
                        invencible=False
                else:
                    xfijar,yfijar=x/2,y/2
                    fijarr=0
            name()
            puntos(score,vida)

            #Corazon
            if vida>600:
                vida=600
            for i in range(1):
                if countheart<len(Heart)-0.1:
                    countheart+=0.1
                else:
                    countheart=0
                if xheart[i]>=-160:
                    xheart[i]-=3
                    mostrar(xheart[i],yheart[i],Heart[int(countheart)])
                else:
                    xheart=[r.randint(1500,3000),r.randint(1500,3000),r.randint(1500,3000)]
                    yheart=[r.randint(100,620),r.randint(100,620),r.randint(100,620)]
                if colision_corazon(xheart[i],yheart[i],coords[0],coords[1]):
                    canalsalud.play(Salud)
                    xheart[i]=r.randint(1500,3000)
                    yheart[i]=r.randint(40,680)
                    if vida<600:
                        vida+=50

            #Colisiones nave
            if col1:
                coordobjr=[x/2,y/2]
                if vida>0:
                    vida-=50/3
                pantalla.blit(live[-1],(1000,25))
                col1=False
                canalnave.play(navesound)
            if col:
                if vida>0:
                    vida-=1
                pantalla.blit(live[-1],(1000,25))
                col=False
                canalnave.play(navesound)
            nave(-(a*180/m.pi+180),coords[0],coords[1],k)
            saludJ(vidaJ)
            if vidaJ<=18000:
                xj=x/2
                endf1=True
                Fase1=False

            #Colision
            if colision:
                if numcolj<=10:
                    numcolj+=1
                    mostrar(x/2,y/2,Jefe[1])
                    mostrar(x/2,700,Vida[0])
                else:
                    numcolj=0
                    colision=False

            #Rayo
            if r.randint(0,1000)==1:
                canal1.play(Trueno)
                rayo=True
            if rayo:
                if 5<=numrayo<=15:
                    pantalla.fill((255,255,255))
                if numrayo<=15:
                    numrayo+=1
                else:
                    numrayo=0
                    rayo=False

            #Game over
             
            if vida<=0:
                game_over=True
                canallose.play(lose)
             
            while game_over:
                p.mouse.set_visible(1)
                G_o(fin,go)
                if go<10:
                    if go<0.9:
                        go+=0.1
                    else:
                        go+=0.2
                mixer.music.pause()
                for event in p.event.get():
                    if event.type== p.QUIT:
                        game_over=False
                        sys.exit()
                    if event.type == p.KEYDOWN:
                        if event.key == p.K_RETURN:
                            mixer.music.unpause()
                            B=False
                            vb=10
                            inicio=True
                            vidaJ=24000
                            invencible=False
                            endf1=False
                            xj=x/2
                            endf2=False
                            angle=0
                            xe=-700
                            xe1=1280+700
                            xp,yp,velx,vely,velx1,vely1=x/2,y/2,0,0,0,0
                            k=31
                            xder=1330
                            xizq=-50
                            vels=8
                            endf3=False
                            entrada3=True
                            yj3=720+360
                            xbj31=1280
                            xbombi=1280/2
                            ybombi=720
                            yboom=0
                            t=0
                            countbombp=0
                            countboom=0
                            actlaser,actlaser2=False,False
                            ent4=False
                            Salida4=False
                            coordj=[-1000,-1000,-1000,-1000,-1000,-1000]
                            xn,yn=1380,720/2
                            tn=0
                            xc,yc=[r.randint(40,1240),r.randint(40,1240)],[-100,820]
                            vida=vida0
                            Fase1=True
                            Fase2=False
                            Fase3=False
                            Fase4=False
                            game_over=False
                p.display.update()

            #Pause
            while Pausa:
                canalpausa.unpause()
                mixer.music.pause()
                clock.tick(60)
                canal1.pause()
                canal2.pause()
                canal3.pause()
                menu=Cinematica_1_1.pause()
                if menu:
                    mixer.music.stop()
                    canalpausa.stop()
                    return Win, True
                Pausa=False
                canalpausa.pause()
                mixer.music.unpause()
                canal1.pause()
                canal2.pause()
                canal3.pause()           
                p.display.update()
            p.display.update()

        while endf1:
            for event in p.event.get():
                if event.type== p.QUIT:
                    endf1=False
                    nivel_4=False
            pantalla.blit(fondo,cfondo)
            clock.tick(60)
            xj-=5
            coordsobj=[300*m.cos(anguloobja)+xj,300*m.sin(anguloobja)+y/2,300*m.cos(anguloobja+2*m.pi/numobjs)+xj,300*m.sin(anguloobja+2*m.pi/numobjs)+y/2,300*m.cos(anguloobja+4*m.pi/numobjs)+xj,300*m.sin(anguloobja+4*m.pi/numobjs)+y/2,300*m.cos(anguloobja+6*m.pi/numobjs)+xj,300*m.sin(anguloobja+6*m.pi/numobjs)+y/2,300*m.cos(anguloobja+8*m.pi/numobjs)+xj,300*m.sin(anguloobja+8*m.pi/numobjs)+y/2,300*m.cos(anguloobja+10*m.pi/numobjs)+xj,300*m.sin(anguloobja+10*m.pi/numobjs)+y/2,300*m.cos(anguloobja+12*m.pi/numobjs)+xj,300*m.sin(anguloobja+12*m.pi/numobjs)+y/2,300*m.cos(anguloobja+14*m.pi/numobjs)+xj,300*m.sin(anguloobja+14*m.pi/numobjs)+y/2,300*m.cos(anguloobja+16*m.pi/numobjs)+xj,300*m.sin(anguloobja+16*m.pi/numobjs)+y/2,300*m.cos(anguloobja+18*m.pi/numobjs)+xj,300*m.sin(anguloobja+18*m.pi/numobjs)+y/2]
            anguloobja+=0.03
            explos(coordsobj,6)
            mostrar(xj,y/2,Jefe[0])
            name()
            puntos(score,vida)
            coords=[300*m.cos(a)+x/2,300*m.sin(a)+y/2]
            if not (x/2-320<=coords[0]<=x/2-280 and y/2-20<=coords[1]<=y/2+20):
                a-=0.02
            nave(-(a*180/m.pi+180),coords[0],coords[1],k)
            saludJ(vidaJ)
            if xj<=-300 and (x/2-320<=coords[0]<=x/2-280 and y/2-20<=coords[1]<=y/2+20):
                Fase2=True
                velx,vely,velx1,vely=0,0,0,0
                endf1=False
                xp,yp=coords[0],coords[1]
                break
            p.display.update()
            
    ############################################################################################################################
    ############################################################################################################################
    ############################################################################################################################
    ############################################################################################################################
        while Fase2:
            p.mouse.set_visible(0)
            for event in p.event.get():
                if event.type== p.QUIT:
                    Fase2=False
                    nivel_4=False
                    sys.exit()
                if event.type == p.KEYDOWN:
                    if event.key == p.K_a:
                        velx1=-10
                    if event.key==p.K_d:
                        velx=10
                    if event.key == p.K_w:
                        vely1=-10
                    if event.key==p.K_s:
                        vely=10
                    if event.key==p.K_SPACE:
                        if B==False:
                            canal2.play(Bomba)
                            B=True
                            xb,yb=coords[0],coords[1]
                    if event.key==p.K_e:
                        vbomb*=-1
                        canal3.play(Cambio)
                    if event.key==p.K_ESCAPE:
                        if Pausa==False:
                            mixer.music.pause()
                            canalpausa.unpause()
                            Pausa=True
                        else:
                            Pausa=False
                if event.type==p.KEYUP:
                    if event.key == p.K_a:
                        velx1=0
                    if event.key == p.K_d:
                        velx=0
                    if event.key == p.K_w:
                        vely1=0
                    if event.key == p.K_s:
                        vely=0

            if inicio:
                canal1.play(Horn)
                inicio=False
            pantalla.blit(fondo,cfondo)
            clock.tick(60)
            mostrar(x/2,y/2,ojo[0])
            if xe<x/2+40:
                xe+=10
            else:
                if xe1>x/2+50:
                    xe1-=10
            mostrar(xe,50,Jefe[2])
            mostrar(xe1,670,Jefe[2],180)
            angle+=10
            Shuriken(xder,xizq,yder,yizq,angle)
            if xe1==x/2+50:
                if xder>=-50:
                    xder-=vels
                else:
                    xder=1330
                    yder=[r.randint(150,570),r.randint(150,570),r.randint(150,570),r.randint(150,570),r.randint(150,570)]
                if xizq<=1330:
                    xizq+=vels
                else:
                    xizq=-50
                    yizq=[r.randint(150,570),r.randint(150,570),r.randint(150,570),r.randint(150,570),r.randint(150,570)]
            xp+=velx+velx1
            if xp<=40:
                xp=40
            elif xp>=1240:
                xp=1240 
            yp+=vely+vely1
            if yp<=150:
                yp=150
            elif yp>=570:
                yp=570
            coords=[xp,yp]
            if k<=58:
                k+=1
            else:
                k=0

            #Disparo
            if B:
                yb+=vbomb
                if vbomb<0:
                    mostrar(xb,yb,bomba,180)
                    if yb<=100:
                        yb=1000
                        B=False
                        if numinv2>130:
                            vidaJ-=6000/20
                            colision=True
                else:
                    mostrar(xb,yb,bomba,0)
                    if yb>=620:
                        yb=-1000
                        B=False
                        if numinv2<=130:
                            vidaJ-=6000/30
                            colision=True   

            #Cambio de invencibilidad
            if numinv2<=260:
                numinv2+=1
                if numinv2<=130:
                    mostrar(xe,50,Jefe[5])
                else:
                    mostrar(xe1,670,Jefe[5],180)
            else:
                numinv2=0

            #Colision
            if xe1==x/2+50:
                saludJ(vidaJ)
                if colision:
                    if numcolj<=5:
                        numcolj+=1
                        if numinv2<=130:
                            mostrar(xe1,670,Jefe[3],180)
                        else:
                            mostrar(xe,50,Jefe[3])
                        mostrar(x/2,y/2,ojo[1])
                        mostrar(x/2,700,Vida[0])
                    else:
                        canal3.play(Dragon)
                        numcolj=0
                        colision=False

            #Colisiones con la nave
            puntos(score,vida)
            if colisioness(xizq,yizq[0],xp,yp) or colisioness(xizq,yizq[1],xp,yp) or colisioness(xizq,yizq[2],xp,yp) or colisioness(xizq,yizq[3],xp,yp) or colisioness(xizq,yizq[4],xp,yp):
                col=True
            if colisioness(xder,yder[0],xp,yp) or colisioness(xder,yder[1],xp,yp) or colisioness(xder,yder[2],xp,yp) or colisioness(xder,yder[3],xp,yp) or colisioness(xder,yder[4],xp,yp):
                col=True
            if col:
                if vida>0:
                    vida-=10
                pantalla.blit(live[-1],(1000,25))
                col=False
                canalnave.play(navesound)
            if vidaJ<=15000:
                vels=12
            name()

            #Corazon
            if vida>600:
                vida=600
            for i in range(1):
                if countheart<len(Heart)-0.1:
                    countheart+=0.1
                else:
                    countheart=0
                if xheart[i]>=-160:
                    xheart[i]-=3
                    mostrar(xheart[i],yheart[i],Heart[int(countheart)])
                else:
                    xheart=[r.randint(1500,3000),r.randint(1500,3000),r.randint(1500,3000)]
                    yheart=[r.randint(100,620),r.randint(100,620),r.randint(100,620)]
                if colision_corazon(xheart[i],yheart[i],coords[0],coords[1]):
                    canalsalud.play(Salud)
                    xheart[i]=r.randint(1500,3000)
                    yheart[i]=r.randint(40,680)
                    if vida<600:
                        vida+=50
            nave(0,coords[0],coords[1],int(k//1))

            #rayo
            if r.randint(0,1000)==1:
                canal1.play(Trueno)
                rayo=True
            if rayo:
                if 5<=numrayo<=15:
                    pantalla.fill((255,255,255))
                if numrayo<=15:
                    numrayo+=1
                else:
                    numrayo=0
                    rayo=False

            #Finalizar fase
            if vidaJ <= 12000:
                endf2=True
            while endf2:
                for event in p.event.get():
                    if event.type== p.QUIT:
                        endf2=False
                        nivel_4=False
                pantalla.blit(fondo,cfondo)
                clock.tick(60)
                mostrar(xe,50,Jefe[2])
                mostrar(xe1,670,Jefe[2],180)
                if xe<1280+700:
                    xe+=10
                if xe>=1280+700:
                    xe1-=10
                puntos(score,vida)
                name()
                nave(0,coords[0],coords[1],int(k//1))
                saludJ(vidaJ)
                if k<=58:
                    k+=1
                else:
                    k=0
                if xe1<=-700:
                    endf2=False
                    Fase2=False
                    Fase3=True
                    velx,vely,velx1,vely1=0,0,0,0
                    xp,yp=coords[0],coords[1]
                    break
                p.display.update()

            #Pause
            while Pausa:
                canalpausa.unpause()
                mixer.music.pause()
                clock.tick(60)
                canal1.pause()
                canal2.pause()
                canal3.pause()
                menu=Cinematica_1_1.pause()
                if menu:
                    mixer.music.stop()
                    canalpausa.stop()
                    return Win, True
                Pausa=False
                canalpausa.pause()
                mixer.music.unpause()
                canal1.pause()
                canal2.pause()
                canal3.pause()           
                p.display.update()
            
            #Game over
             
            if vida<=0:
                game_over=True
                canallose.play(lose)
             
            while game_over:
                p.mouse.set_visible(1)
                G_o(fin,go)
                if go<10:
                    if go<0.9:
                        go+=0.1
                    else:
                        go+=0.2
                mixer.music.pause()
                for event in p.event.get():
                    if event.type== p.QUIT:
                        game_over=False
                        sys.exit()
                    if event.type == p.KEYDOWN:
                        if event.key == p.K_RETURN:
                            B=False
                            vb=10
                            inicio=True
                            vidaJ=24000
                            invencible=False
                            endf1=False
                            xj=x/2
                            endf2=False
                            angle=0
                            xe=-700
                            xe1=1280+700
                            xp,yp,velx,vely=x/2,y/2,0,0
                            k=31
                            xder=1330
                            xizq=-50
                            vels=8
                            endf3=False
                            entrada3=True
                            yj3=720+360
                            xbj31=1280
                            xbombi=1280/2
                            ybombi=720
                            yboom=0
                            t=0
                            countbombp=0
                            countboom=0
                            actlaser,actlaser2=False,False
                            ent4=False
                            Salida4=False
                            coordj=[-1000,-1000,-1000,-1000,-1000,-1000]
                            xn,yn=1380,720/2
                            tn=0
                            xc,yc=[r.randint(40,1240),r.randint(40,1240)],[-100,820]
                            vida=vida0
                            Fase1=True
                            Fase2=False
                            Fase3=False
                            Fase4=False
                            vb=10
                            mixer.music.unpause()
                            game_over=False
                p.display.update()
            if Fase1 or Fase3:
                break
            p.display.update()
    ############################################################################################################################################################################
    ############################################################################################################################################################################
    ############################################################################################################################################################################
    ############################################################################################################################################################################
        while Fase3:
            p.mouse.set_visible(0)
            for event in p.event.get():
                if event.type== p.QUIT:
                    Fase3=False
                    sys.exit()
                    nivel_4=False
                if event.type == p.KEYDOWN:
                    if event.key == p.K_a:
                        velx1=-10
                    if event.key==p.K_d:
                        velx=10
                    if event.key == p.K_w:
                        vely1=-10
                    if event.key==p.K_s:
                        vely=10
                    if event.key==p.K_SPACE:
                        if B==False:
                            canalbala.play(Balas)
                            B=True
                            xb,yb=coords[0],coords[1]
                    if event.key==p.K_ESCAPE:
                        if Pausa==False:
                            Pausa=True
                        else:
                            Pausa=False
                if event.type==p.KEYUP:
                    if event.key == p.K_a:
                        velx1=0
                    if event.key == p.K_d:
                        velx=0
                    if event.key == p.K_w:
                        vely1=0
                    if event.key == p.K_s:
                        vely=0
            pantalla.blit(fondo,cfondo)
            clock.tick(60)

            while entrada3:
                pantalla.blit(fondo,cfondo)
                clock.tick(60)
                mostrar(1025,yj3,Jefe3[0])
                p.draw.rect(pantalla,(0,255,243),(int(1280/2),0,10,int(-(1280/(1080-540))*yj3+1280*1080/((-540+1080)))))
                coords=[xp,yp]
                if xp>=1280/2-40:
                    xp-=10
                if yj3>540:
                    yj3-=10
                elif yj3<=540 and xp<1280/2-40:
                    entrada3=False
                if k<=58:
                    k+=1
                else:
                    k=0
                puntos(score,vida)
                name()
                nave(0,coords[0],coords[1],int(k))
                saludJ(vidaJ)
                p.display.update()

            if 9000<=vidaJ<=12001:
                vels=6
            else:
                vels=10
            s=r.randint(0,600)
            if actlaser:
                s=0
                invencible=True
                for i in range(9): 
                    mostrar(xl1[i],yl1[i],rayos,-45-angulol1[i])
                    if colisioness(coords[0],coords[1],xl1[i],yl1[i]):
                        col=True
                        canalnave.play(navesound)
                xl1=xl1-vels*np.cos(angulol1*np.pi/180)
                yl1=yl1-vels*np.sin(angulol1*np.pi/180)
                if xl1[0]<=-100:
                    xl1=np.array([930,930,930,930,930,930,930,930,930])
                    yl1=np.array([480,480,480,480,480,480,480,480,480])
                    actlaser=False
                    invencible=False
            mostrar(1025,540,Jefe3[0])

            #laser
            if actlaser2:
                s=0
                invencible=True
                if xbj31+10*30>=0:
                    xbj31-=5
                    for i in range(11):
                        mostrar(xbj31+i*30,360*m.sin((xbj31+i*30)/200)+360,laser)
                        mostrar(xbj31+i*30,360*-m.sin((xbj31+i*30)/200)+360,laser)
                        if colisioness(coords[0],coords[1],xbj31+i*30,360*m.sin((xbj31+i*30)/200)+360) or colisioness(coords[0],coords[1],xbj31+i*30,-360*m.sin((xbj31+i*30)/200)+360):
                            col=True
                            canalnave.play(navesound)
                else:
                    xbj31=1280+r.randint(0,100)
                    actlaser2=False
                    invencible=False
            if s==1:
                actlaser=True
                canal2.play(mixer.Sound("Nivel 4\\Sonidos\\DJ1.wav"))
            elif s==2:
                actlaser2=True
                canal2.play(mixer.Sound("Nivel 4\\Sonidos\\rocket_launch.wav"))
            p.draw.rect(pantalla,(0,255,243),(int(1280/2),0,10,1280))     

            #Disparo
            if B:
                vb=20
                xb+=vb
                tiro(0,xb,yb,int(nb))
                if xb>=900 and yb>=360:
                    xb=-1000
                    yb=-1000
                    B=False
                    if not invencible:
                        vidaJ-=6000/30
                        colision=True
                elif xb>=1300 and yb<=360:
                    xb=-1000
                    yb=-1000
                    B=False
            puntos(score,vida)

            #Invencible
            if invencible:
                mostrar(1025,540,Jefe3[2])

            #Bombas
            if countbomb<=36:
                countbomb+=0.1
                if 6<=countbomb<=25:
                    for i in range (9):
                        mostrar(coordsbombx[i],coordsbomby[i],Bombas[int(countbomb-6)])
                        if colisioness(coords[0],coords[1],coordsbombx[i],coordsbomby[i]):
                            countbomb=26
                            break
                elif 2<=countbomb<6:
                    if int(countbomb)%2==0:
                        for i in range (9):
                            mostrar(coordsbombx[i],coordsbomby[i],excl[0])
                    else:
                        for i in range (9):
                            mostrar(coordsbombx[i],coordsbomby[i],excl[1])
                elif 25<countbomb<=31:
                    countbomb+=0.2
                    for i in range (9):
                        mostrar(coordsbombx[i],coordsbomby[i],boom[int(countbomb-25)])
                        if colisioness(coords[0],coords[1],coordsbombx[i],coordsbomby[i]):
                            if vida>0:
                                vida-=2
                            pantalla.blit(live[-1],(1000,25))   
                    if 26.6<countbomb<=27:
                        canal3.play(Expbomb)        
            else:
                countbomb=0
                coordsbomby=np.random.randint(50,670,10)
                coordsbombx=np.random.randint(40,1280/2,10)

            #Mostrar cosas :v
            name()

            #Corazon
            if vida>600:
                vida=600
            for i in range(1):
                if countheart<len(Heart)-0.1:
                    countheart+=0.1
                else:
                    countheart=0
                if xheart[i]>=-160:
                    xheart[i]-=3
                    mostrar(xheart[i],yheart[i],Heart[int(countheart)])
                else:
                    xheart=[r.randint(1500,3000),r.randint(1500,3000),r.randint(1500,3000)]
                    yheart=[r.randint(500,700),r.randint(500,700),r.randint(500,700)]
                if colision_corazon(xheart[i],yheart[i],coords[0],coords[1]):
                    canalsalud.play(Salud)
                    xheart[i]=r.randint(1500,3000)
                    yheart[i]=r.randint(500,700)
                    if vida<600:
                        vida+=50
            nave(0,coords[0],coords[1],int(k))
            saludJ(vidaJ)

            #Movimiento nave
            xp+=velx+velx1
            if xp<=40:
                xp=40
            elif xp>=1280/2:
                if vida>0:
                    vida-=1
                pantalla.blit(live[-1],(1000,25))
                if xp>=1280:
                    xp=1280
            yp+=vely+vely1
            if yp<=50:
                yp=50
            elif yp>=670:
                yp=670
            coords=[xp,yp]
            if k<=58:
                k+=1
            else:
                k=0

            #Colision con jefe
            if colision:
                if numcolj<=5:
                    numcolj+=1
                    mostrar(1025,540,Jefe3[1])
                    mostrar(x/2,700,Vida[0])
                else:
                    numcolj=0
                    colision=False
            if nb<=12:
                nb+=0.5
            else:
                nb=0

            #Bombita
            if colisioness(xbombi,ybombi,coords[0],coords[1]):
                t=0
                yboom=ybombi
                colb=True
                canal3.play(Expbomb)
            if colb:
                mostrar(xbombi,yboom,boom[int(countboom)])
                if countboom<len(boom)-1:
                    countboom+=0.3
                    if vida>0:
                        vida-=1
                    pantalla.blit(live[-1],(1000,25))
                else:
                    colb=False
                    countboom=0
            else:
                if countbombp<len(bombitas)-1:
                    countbombp+=0.3
                else:
                    countbombp=0
                ybombi=(0.5)/2*t**2-m.sqrt(0.5*720)*t+720
                mostrar(xbombi,ybombi,bombitas[int(countbombp)])
                if ybombi<=1280:
                    t+=0.5
                else:
                    xbombi,ybombi,t=coords[0],0,0

            #colision con nave
            if col:
                if vida>0:
                    vida-=4
                pantalla.blit(live[-1],(1000,25))
                col=False

            #rayo
            if r.randint(0,1000)==1:
                canal1.play(Trueno)
                rayo=True
            if rayo:
                if 5<=numrayo<=15:
                    pantalla.fill((255,255,255))
                if numrayo<=15:
                    numrayo+=1
                else:
                    numrayo=0
                    rayo=False
            if vidaJ <= 6000:
                endf3=True

            while endf3:
                for event in p.event.get():
                    if event.type== p.QUIT:
                        endf3=False
                        nivel_4=False
                pantalla.blit(fondo,cfondo)
                clock.tick(60)
                mostrar(1025,yj3,Jefe3[0])
                if yj3<720+360:
                    yj3+=10
                else:
                    endf3=False
                    Fase3=False
                    Fase4=True
                    velx,vely,velx1,vely1=0,0,0,0
                    ent4=True
                    break
                puntos(score,vida)
                name()
                nave(0,coords[0],coords[1],int(k//1))
                saludJ(vidaJ)
                p.display.update()
            if ent4:
                break
            
            #Pause
            while Pausa:
                canalpausa.unpause()
                mixer.music.pause()
                clock.tick(60)
                canal1.pause()
                canal2.pause()
                canal3.pause()
                menu=Cinematica_1_1.pause()
                if menu:
                    mixer.music.stop()
                    canalpausa.stop()
                    return Win, True
                Pausa=False
                canalpausa.pause()
                mixer.music.unpause()
                canal1.pause()
                canal2.pause()
                canal3.pause()           
                p.display.update()

            #Game over
             
            if vida<=0:
                game_over=True
                canallose.play(lose)
             
            while game_over:
                p.mouse.set_visible(1)
                G_o(fin,go)
                if go<10:
                    if go<0.9:
                        go+=0.1
                    else:
                        go+=0.2
                mixer.music.pause()
                for event in p.event.get():
                    if event.type== p.QUIT:
                        game_over=False
                        sys.exit()
                    if event.type == p.KEYDOWN:
                        if event.key == p.K_RETURN:
                            inicio=True
                            B=False
                            vidaJ=24000
                            invencible=False
                            endf1=False
                            xj=x/2
                            endf2=False
                            angle=0
                            xe=-700
                            xe1=1280+700
                            xp,yp,velx,vely,velx1,vely1=x/2,y/2,0,0,0,0
                            k=31
                            xder=1330
                            xizq=-50
                            vels=8
                            endf3=False
                            entrada3=True
                            yj3=720+360
                            xbj31=1280
                            xbombi=1280/2
                            ybombi=720
                            yboom=0
                            t=0
                            countbombp=0
                            countboom=0
                            actlaser,actlaser2=False,False
                            ent4=False
                            Salida4=False
                            coordj=[-1000,-1000,-1000,-1000,-1000,-1000]
                            xn,yn=1380,720/2
                            tn=0
                            xc,yc=[r.randint(40,1240),r.randint(40,1240)],[-100,820]
                            vida=vida0
                            Fase1=True
                            Fase2=False
                            Fase3=False
                            Fase4=False
                            vb=10
                            mixer.music.unpause()
                            game_over=False
                p.display.update()
            if Fase4 or Fase1:
                break
            p.display.update()
    ############################################################################################################################################################################
    ############################################################################################################################################################################
    ############################################################################################################################################################################
    ############################################################################################################################################################################    
        while Fase4:
            p.mouse.set_visible(0)
            for event in p.event.get():
                if event.type== p.QUIT:
                    Fase4=False
                    nivel_4=False
                    sys.exit()
                if event.type == p.KEYDOWN:
                    if event.key == p.K_a:
                        velx1=-10
                    if event.key==p.K_d:
                        velx=10
                    if event.key == p.K_w:
                        vely1=-10
                    if event.key==p.K_s:
                        vely=10
                    if event.key==p.K_SPACE:
                        if B==False:
                            canalbala.play(Balas)
                            B=True
                            xb,yb=coords[0],coords[1]
                    if event.key==p.K_ESCAPE:
                        if Pausa==False:
                            Pausa=True
                            canalpausa.unpause()
                        else:
                            Pausa=False
                if event.type==p.KEYUP:
                    if event.key == p.K_a:
                        velx1=0
                    if  event.key == p.K_d:
                        velx=0
                    if event.key == p.K_w:
                        vely1=0
                    if event.key == p.K_s:
                        vely=0
            pantalla.blit(fondo,cfondo)
            clock.tick(60)
            while ent4:
                for event in p.event.get():
                    if event.type== p.QUIT:
                        Fase4=False
                        nivel_4=False
                        ent4=False
                pantalla.blit(fondo,cfondo)
                if coords[1]<720/2-2:
                    coords[1]+=2
                elif coords[1]>720/2+2:
                    coords[1]-=2
                if coords[0]<1280/2-2:
                    coords[0]+=2
                elif coords[0]>1280/2+2:
                    coords[0]-=2
                if  xn>990:
                    xn-=2
                else:
                    if corrimiento1<720/4:
                        corrimiento1+=2
                        corrimiento2-=2
                    else:
                        coords[1]=yd[7]-200
                        if yc[0]<60:
                            yc[0]+=2
                            yc[1]-=2
                        else:
                            xp,yp=coords[0],coords[1]
                            ent4=False
                for i in range(2):
                    if vcx[i]>0:
                        mostrar(xc[i],yc[i],Calavera[0])
                    else:
                        mostrar(xc[i],yc[i],Calavera[1])
                for i in range(16):
                    yup[i]=(310/2)*m.sin(tf[i]/4)+corrimiento1
                    yd[i]=(310/2)*m.sin(tf[i]/4)+corrimiento2
                    mostrar(xup[i],yup[i],fuego,4*tf[i])
                    mostrar(xd[i],yd[i],fuego,4*tf[i])
                    tf[i]+=0.15
                mostrar(xn,yn,Jefe4[0])
                if k<=58:
                    k+=1
                else:
                    k=0
                tn-=2
                nave(0,coords[0],coords[1],int(k))
                yn=40*np.sin(tn/20)+720/2
                name()
                saludJ(vidaJ)
                puntos(score,vida)
                p.display.update()
                clock.tick(60)

            #Movimiento nave
            coords=[xp,yp]
            xp+=velx+velx1
            if xp<=40:
                xp=40
            elif xp>=1240:
                xp=1240
            yp+=vely+vely1
            if yp<=50:
                yp=50
            elif yp>=670:
                yp=670
            if k<=58:
                k+=1
            else:
                k=0

            #Disparo
            if B:
                vb=30
                xb+=vb
                tiro(0,xb,yb,int(nb))
                if colisioness(xb,yb,xn,yn,41):
                    xb=-1000
                    yb=-1000
                    B=False
                    colision=True
                if xb>=1280:
                    xb=-1000
                    yb=-1000
                    B=False

            #Fuego
            canalfuego.unpause()
            for i in range(16):
                yup[i]=(310/2)*m.sin(tf[i]/4)+720/4
                yd[i]=(310/2)*m.sin(tf[i]/4)+720/4+350
                mostrar(xup[i],yup[i],fuego,4*tf[i])
                mostrar(xd[i],yd[i],fuego,4*tf[i])
                tf[i]+=0.15
                if colisioness(coords[0],coords[1],xup[i],yup[i]) or colisioness(coords[0],coords[1],xd[i],yd[i]):
                    canalnave.play(navesound)
                    col1=True
            puntos(score,vida)
            if col1:
                if vida>0:
                    vida-=2
                pantalla.blit(live[-1],(1000,25))
                col1=False

            #Teletransporte
            if countT<len(Tele)-1:
                countT+=0.1
                mostrar(xn,yn,Tele[int(countT)])
            else:
                if tel:
                    canaltele.play(teleportsound)
                    yn=r.randint(70,600)
                    tel=False
                if countT2>0.1:
                    countT2-=0.1
                    mostrar(xn,yn,Tele[int(countT2)])
                    disparar=True
                else:
                    if yn<70:
                        vn=-vn
                    elif yn>600:
                        vn=-vn
                    yn+=vn
                    mostrar(xn,yn,Jefe4[0])
                    if r.randint(0,400)==5:
                        countT=0
                        countT2=len(Tele)-1
                        tel=True
                        if coordj[0]==-1000:
                            canaldisparo4.play(DJ4)
                            coordj[0],coordj[1]=xn,yn
                        elif coordj[2]==-1000:
                            canaldisparo4.play(DJ4)
                            coordj[2],coordj[3]=xn,yn
                        elif coordj[4]==-1000:
                            canaldisparo4.play(DJ4)
                            coordj[4],coordj[5]=xn,yn
            if colisioness(xn,yn,coords[0],coords[1]):
                canalnave.play(navesound)
                if vida>0:
                    vida=0
                pantalla.blit(live[-1],(1000,25))
            if disparar:
                for i in range(3):
                    if coordj[2*i]!=-1000:
                        mostrar(coordj[2*i],coordj[2*i+1],disparosnave,90)
                    if coordj[2*i]>0:
                        coordj[2*i]-=vdj
                    else:
                        coordj[2*i]=-1000
                        disparar=False                  
                    if colisioness(coords[0],coords[1],coordj[2*i],coordj[2*i+1]):
                        canalnave.play(navesound)
                        if vida>0:
                            vida-=25
                        coordj[2*i],coordj[2*i+1]=-1000,-1000
            for i in range(2):
                xc[i]+=vcx[i]
                yc[i]+=vcy[i]
                if xc[i]<40 or xc[i]>1280-40:
                    vcx[i]=-vcx[i]
                if yc[i]<40 or yc[i]>720-40:
                    vcy[i]=-vcy[i]
                if vcx[i]>0:
                    mostrar(xc[i],yc[i],Calavera[0])
                else:
                    mostrar(xc[i],yc[i],Calavera[1])
                if colisioness(coords[0],coords[1],xc[i],yc[i]):
                    canalnave.play(navesound)
                    if vida>0:
                        vida-=2
                    pantalla.blit(live[-1],(1000,25))
            name()

            #Corazon
            if vida>600:
                vida=600
            for i in range(1):
                if countheart<len(Heart)-0.1:
                    countheart+=0.1
                else:
                    countheart=0
                if xheart[i]>=-160:
                    xheart[i]-=3
                    mostrar(xheart[i],yheart[i],Heart[int(countheart)])
                else:
                    xheart=[r.randint(1500,3000),r.randint(1500,3000),r.randint(1500,3000)]
                    yheart=[r.randint(100,620),r.randint(100,620),r.randint(100,620)]
                if colision_corazon(xheart[i],yheart[i],coords[0],coords[1]):
                    canalsalud.play(Salud)
                    xheart[i]-=r.randint(2000,3000)
                    yheart[i]=r.randint(100,620)
                    if vida<600:
                        vida+=50

            nave(0,coords[0],coords[1],int(k))
            saludJ(vidaJ)
            if colision:
                if numcolj<=5:
                    numcolj+=1
                    mostrar(xn,yn,Jefe4[1])
                    mostrar(x/2,700,Vida[0])
                else:
                    vidaJ-=6000/30
                    numcolj=0
                    colision=False
                    
            #Rayo
            if r.randint(0,1000)==1:
                canal1.play(Trueno)
                rayo=True
            if rayo:
                if 5<=numrayo<=15:
                    pantalla.fill((255,255,255))
                if numrayo<=15:
                    numrayo+=1
                else:
                    numrayo=0
                    rayo=False
            if vidaJ<=1:
                for i in range(16):
                    yupi[i]=yup[i]
                    ydi[i]=yd[i]
                    xdi[i]=xd[i]
                    xupi[i]=xup[i]
                Salida4=True
                countbomb=0
            while Salida4:
                for event in p.event.get():
                    if event.type== p.QUIT:
                        Fase4=False
                        nivel_4=False
                        Salida4=False
                pantalla.blit(fondo,cfondo)
                mostrar(990,yn,Jefe4[0])
                for i in range(2):
                    if vcx[i]>0:
                        mostrar(xc[i],yc[i],Calavera[0])
                    else:
                        mostrar(xc[i],yc[i],Calavera[1])
                for i in range(16):
                    yupi[i]=(yup[i]-yn)/(xup[i]-990)*(xupi[i]-990)+yn
                    ydi[i]=(yd[i]-yn)/(xd[i]-990)*(xupi[i]-990)+yn
                    mostrar(xupi[i],yupi[i],fuego,xupi[i])
                    mostrar(xdi[i],ydi[i],fuego,xdi[i])
                    if xdi[i]<996:
                        xdi[i]+=10
                        xupi[i]+=10
                    if xdi[i]>996:
                        xdi[i]-=10
                        xupi[i]-=10
                    if 993<xdi[i]<997:
                        if ydi[i]>yn:
                            ydi[i]-=2
                if countbomb<len(boom)-0.2:
                    countbomb+=0.2
                else:
                    canal3.play(Expbomb) 
                    countbomb=0
                    n+=1
                mostrar(990+50,yn-20,boom[int(countbomb)])
                mostrar(990-30,yn-20,boom[int(countbomb)])
                mostrar(990+10,yn,boom[int(countbomb)])
                if n==10:
                    Salida4=False
                    Win=True
                if k<=58:
                    k+=1
                else:
                    k=0
                nave(0,coords[0],coords[1],int(k))
                name()
                saludJ(vidaJ)
                puntos(score,vida)
                p.display.update()
                clock.tick(60)

            while Win:
                if cp<=200:
                    cp+=1
                else:
                    cp=0
                if cp<=100:
                    color=1
                else:
                    color=0
                if wn<10:
                    wn+=0.3
                WIN(muy_bien,color,wn)
                for event in p.event.get():
                    if event.type== p.QUIT:
                        Win=False
                        nivel_4=False
                        Fase4=False
                    if event.type == p.KEYDOWN:
                        if event.key == p.K_ESCAPE:
                            Save=open("Guardado.txt","r")
                            text=int(Save.readline())
                            Save.close()
                            Save=open(str(text)+".txt","w")
                            Save.close()
                            Save=open(str(text)+".txt","a")
                            Save.write(nombre+"\n")
                            Save.write(str(int(score+vida))+"\n")
                            Save.write("4"+"\n")
                            Save.write(str(scorei))
                            Save.close()
                            if Win==True:
                                canal1.stop()
                                canal2.stop()
                                canal3.stop()
                                canalbala.stop()
                                canalnave.stop()
                                canalsalud.stop()
                                canalfuego.stop()
                                canaldisparo4.stop()
                                canaltele.stop()
                                canalpausa.stop()
                                canallose.stop()
                                return Win,True
                p.display.update()

            #Pause
            while Pausa:
                canalpausa.unpause()
                mixer.music.pause()
                canalfuego.pause()
                clock.tick(60)
                canal1.pause()
                canal2.pause()
                canal3.pause()
                menu=Cinematica_1_1.pause()
                if menu:
                    mixer.music.stop()
                    canalpausa.stop()
                    return Win, True
                Pausa=False
                canalpausa.pause()
                mixer.music.unpause()
                canalfuego.unpause()
                canal1.unpause()
                canal2.unpause()
                canal3.unpause()           
                p.display.update()

            #Game over
             
            if vida<=0:
                game_over=True
                canallose.play(lose)
             
            while game_over:
                canalfuego.pause()
                p.mouse.set_visible(1)
                G_o(fin,go)
                if go<10:
                    if go<0.9:
                        go+=0.1
                    else:
                        go+=0.2
                mixer.music.pause()
                for event in p.event.get():
                    if event.type== p.QUIT:
                        game_over=False
                        sys.exit()
                    if event.type == p.KEYDOWN:
                        if event.key == p.K_RETURN:
                            mixer.music.unpause()
                            B=False
                            inicio=True
                            vidaJ=24000
                            invencible=False
                            endf1=False
                            xj=x/2
                            endf2=False
                            angle=0
                            xe=-700
                            xe1=1280+700
                            xp,yp,velx,vely,velx1,vely1=x/2,y/2,0,0,0,0
                            k=31
                            xder=1330
                            xizq=-50
                            vels=8
                            endf3=False
                            entrada3=True
                            yj3=720+360
                            xbj31=1280
                            xbombi=1280/2
                            ybombi=720
                            yboom=0
                            t=0
                            countbombp=0
                            countboom=0
                            actlaser,actlaser2=False,False
                            ent4=False
                            Salida4=False
                            coordj=[-1000,-1000,-1000,-1000,-1000,-1000]
                            xn,yn=1380,720/2
                            tn=0
                            xc,yc=[r.randint(40,1240),r.randint(40,1240)],[-100,820]
                            vida=vida0
                            Fase1=True
                            Fase2=False
                            Fase3=False
                            Fase4=False
                            vb=10
                            mixer.music.unpause()
                            game_over=False
                p.display.update()
            p.display.update()
            if vidaJ==24000:
                break
        p.display.update()