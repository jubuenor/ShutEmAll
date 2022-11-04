import random as r
import numpy as np
import pygame as p
from pygame import mixer
import Cinematica_4
import Nivel_4_Jefe
import Cinematica_1_1
import sys
def niv_4():
    Save=open("Guardado.txt","r")
    text=Save.readline()
    Save.close()
    Save=open(text+".txt","r")
    nombre=Save.readline().replace('\n',"")
    score=int(Save.readline())
    Save.close()
    vida=600
    score0=score
    if vida>600:
        vida=600
    #Iniciar programa
    p.init()
    x=1280
    y=720


    #Música y sonidos
    Balas=mixer.Sound("Nivel 4\\Sonidos\\Bala.wav")
    Salud=mixer.Sound("Nivel 4\\Sonidos\\Salud.wav")
    Bombas=mixer.Sound("Nivel 4\\Sonidos\\Bomba.wav")
    ExpHSound=mixer.Sound("Nivel 4\\Sonidos\\ExplosionH.wav")
    HelicopteroS=mixer.Sound("Nivel 4\\Sonidos\\Helicoptero.wav")
    Expbomba=mixer.Sound("Nivel 4\\Sonidos\\Explosion.wav")
    DSS=mixer.Sound("Nivel 4\\Sonidos\\Disparo.wav")
    colnave=mixer.Sound("Nivel 4\\Sonidos\\boom7.wav")
    explosionesA=mixer.Sound("Nivel 4\\Sonidos\\bombexplosion.ogg")
    plane=mixer.Sound("Nivel 4\\Sonidos\\plane.ogg")
    Spausa=mixer.Sound("Sonidos\\SpacyLoop.ogg")
    JetS=mixer.Sound("Nivel 4\\Sonidos\\Jet.ogg")
    lose=mixer.Sound("Sonidos\\lose music.ogg")
    mixer.music.load("Nivel 1\\Sonidos\\Invisible Enemy.mp3")
    mixer.music.play(-1)
    mixer.set_num_channels(13)
    canalsalud=mixer.Channel(0)
    canalsalud.set_volume(0.4)
    canalbala=mixer.Channel(1)
    canalbala.set_volume(0.2)
    canalbomba=mixer.Channel(2)
    canalbomba.set_volume(0.3)
    CEH=mixer.Channel(3)
    CEH.set_volume(0.3)
    canalHelicoptero=mixer.Channel(4)
    canalHelicoptero.set_volume(0.35)
    canalexpbomb=mixer.Channel(5)
    CDS=mixer.Channel(6)
    colnaves=mixer.Channel(7)
    colnaves.set_volume(0.3)
    canalbombaA=mixer.Channel(8)
    canalplane=mixer.Channel(9)
    canalplane.set_volume(0.5)
    canalJet=mixer.Channel(10)
    canalJet.set_volume(0.5)
    canalpausa=mixer.Channel(11)
    canalpausa.set_volume(0.3)
    canallose=mixer.Channel(12)
    canalpausa.pause()
    
    #Fonts
    font=p.font.Font('Nivel 4\\Fuentes\\BLADRMF_.TTF',28)
    fonttext=p.font.Font('Nivel 4\\Fuentes\\Timeless-Bold.ttf',40)
    fonttext2=p.font.Font('Nivel 4\\Fuentes\\Timeless-Bold.ttf',25)
    fonttext3=p.font.Font('Nivel 4\\Fuentes\\Open 24 Display St.ttf',30)


    #Imagenes clase
    class Img:
        def __init__(self,a):
            self.ubicacion=a
        def img(self):
            return p.image.load("Nivel 4\\Imagenes\\"+self.ubicacion).convert_alpha()


    #Titulos
    punt=2000
    Titulo="Nivel 4: The end of the line"
    live=[p.image.load("Nivel 4\\Imagenes\\Vida\\Vida0.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida1.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida2.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida3.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida4.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida5.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida6.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida7.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida8.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida9.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida10.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida11.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\Vida12.png"),p.image.load("Nivel 4\\Imagenes\\Vida\\cVida0.png")]
    def puntos(score,vida,cvl=0):
        hola1=fonttext.render(Titulo,True,(255,255,255))
        cent=hola1.get_rect(center=(int(x/2),50))
        civil=font.render("Civiles: "+str(cvl),True,(255,255,255))
        r,g,y,b=0,0,0,0
        puntos=font.render("Puntaje: "+str(score),True,(255,255,255))
        hola=fonttext2.render('Jugador: '+nombre,True,(255,255,255))
        pantalla.blit(hola,(1010,60))
        pantalla.blit(puntos,(25,25))
        pantalla.blit(civil,(25,60))
        pantalla.blit(live[0],(1000,25))
        pantalla.blit(hola1,cent)
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

    #Cosas varias
    pantalla = p.display.set_mode((x,y))
    Icono = p.image.load('Nivel 4\\Imagenes\\Icono.png')
    p.display.set_icon(Icono)
    fondo=p.image.load("Nivel 4\\Imagenes\\Fondo0.png").convert()
    cfondo=fondo.get_rect(center=(int(x/2),int(y/2)))
    p.display.set_caption("Shut 'em all")


    #Mostrar
    def mostrar(x,y,im,a=0):
        img=p.transform.rotozoom(im,a,1)
        centro=img.get_rect(center=(int(x),int(y)))
        pantalla.blit(img,centro)
    def colision(x1,y1,x2,y2,r=40):
        if (x1-x2)**2+(y1-y2)**2<=r**2:
            return True
        else:
            return False


    #Señora
    senora=[]
    for i in range(10):
        senora.append(p.image.load("Nivel 1\\Imagenes\\TorreControl\\"+str(i+1)+".png"))
    def mostrartext(texto,k,x,y,c=[0,1,0]):
        t=fonttext3.render(texto[0:int(k)],True,(c[0]*255,c[1]*255,c[2]*255))
        pantalla.blit(t,(int(x),int(y)))
    countsen=0
    count=0
    saltar=False
    k1=0
    nc=0
    k2=0
    dialogo1=["Ten cuidado con los kamikaze. No puedes dispararles,","puede ser peligroso."]
    akb=["Acaba con todos...",""]
    Dialogos=[dialogo1,akb]
    w,h=0,0

    #Gente
    clock = p.time.Clock()
    gented=[]
    gentei=[]
    for i in range(5):
        ub="Gente\\"+str(i)+".png"
        im=Img(ub)
        gented.append(im.img())
        ub="Gente\\i"+str(i)+".png"
        im=Img(ub)
        gentei.append(im.img())
    countgent=0
    cvls=0
    xg,yg=[],[]
    vxg=[]
    for i in range(20):
        xg.append(r.randint(0,1280))
        yg.append(700)
        vxg.append(3-6*r.randint(0,1))


    #Nave
    col,numcol=False,0
    col1,numcol1=False,0
    Nave=[]
    k=0
    xp,yp,velx,vely,velx1,vely1,angle=0,y/2,0,0,0,0,0
    for i in range(1,61):
        ub="NaveSprite\\"
        ub+=str(i)+".png"
        im=Img(ub)
        Nave.append(im.img())


    #Corazon
    n=1
    Heart=[]
    xheart=[r.randint(1500,3000),r.randint(1500,3000),r.randint(1500,3000)]
    yheart=[r.randint(40,400),r.randint(40,400),r.randint(40,400)]
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


    #bala
    nb=7
    B=False
    vb=7
    xb,yb=1000,1000
    bala=[]
    angleb=angle
    for i in range(1,15):
        ub="Misil\\"
        ub+=str(i)+".png"
        im=Img(ub)
        bala.append(im.img())
    BombaD,BombaI=[],[]
    T=False
    vbomb=4
    xbomb,ybomb=0,0
    nbomb=0
    direc=0
    for i in range(7):
        ub="Misil\\D"
        ub+=str(i)+".png"
        im=Img(ub)
        BombaD.append(im.img())
        ub="Misil\\I"
        ub+=str(i)+".png"
        im=Img(ub)
        BombaI.append(im.img())
    Bomba=[BombaD,BombaI]
    Explosion=[]
    countExp=0
    for i in range(24):
        ub="Misil\\Exp"
        ub+=str(i)+".png"
        im=Img(ub)
        Explosion.append(im.img())


    #Helicoptero
    HelicopteroD,HelicopteroI,HelicopteroD1,HelicopteroI1,HelicopteroD2,HelicopteroI2,HelicopteroD3,HelicopteroI3,Helicoptero=[],[],[],[],[],[],[],[],[]
    balaH=Img("Helicoptero\\Misil.png").img()
    explH=[]
    countHel=0
    xexph,yexph=[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]
    expcount=[0,0,0,0,0,0,0]
    countH=0
    colH=[]
    disparableH=[]
    xbH,ybH=[],[]
    vbH=[]
    xh,yh=[],[]
    vHy,vHx=[],[]
    H=[]
    HD=[]
    for i in range(7):
        colH.append(False)
        explH.append(False)
        vbH.append(5)
        disparableH.append(True)
        xbH.append(0)
        ybH.append(0)
        ub="Helicoptero\\"
        ub+=str(i)+".png"
        im=Img(ub)
        HelicopteroI.append(im.img())
        ub="Helicoptero\\D"
        ub+=str(i)+".png"
        im=Img(ub)
        HelicopteroD.append(im.img())
        ub="Helicoptero\\1"
        ub+=str(i)+".png"
        im=Img(ub)
        HelicopteroI1.append(im.img())
        ub="Helicoptero\\D1"
        ub+=str(i)+".png"
        im=Img(ub)
        HelicopteroD1.append(im.img())
        ub="Helicoptero\\2"
        ub+=str(i)+".png"
        im=Img(ub)
        HelicopteroI2.append(im.img())
        ub="Helicoptero\\D2"
        ub+=str(i)+".png"
        im=Img(ub)
        HelicopteroD2.append(im.img())
        ub="Helicoptero\\3"
        ub+=str(i)+".png"
        im=Img(ub)
        HelicopteroI3.append(im.img())
        ub="Helicoptero\\D3"
        ub+=str(i)+".png"
        im=Img(ub)
        HelicopteroD3.append(im.img())
        xh.append(1380-1480*r.randint(0,1))
        HD.append(0)
        if xh[i]<200:
            H.append(0)
            vHx.append(r.randint(3,5))
        else:
            H.append(1)
            vHx.append(-r.randint(3,5)) 
        yh.append(r.randint(100,500))
        vHy.append(4-8*r.randint(0,1))
    Helicoptero=[[HelicopteroD,HelicopteroI],[HelicopteroD1,HelicopteroI1],[HelicopteroD2,HelicopteroI2],[HelicopteroD3,HelicopteroI3]]


    #explosiones colisiones
    explosiones=[]
    for i in range(9):
        ub="Explosion\\"
        ub+=str(i)+".png"
        im=Img(ub)
        explosiones.append(im.img())


    #Avion
    varios=False
    xav,yav=[1380,-100],[r.randint(40,400),r.randint(40,400)]
    angleav=[180,0]
    velav=[-10,10]
    Avion=[]
    countA=0
    dca=0.2
    xa,ya=-100,0
    xexpA,yexpA=[0,0,0],[0,0,0]
    explA,countexpA=[False,False,False],0
    Jet=[]
    xj,yj=[],[]
    tj,aj=0,0
    vj=9
    countJ=0
    for i in range(8):
        ub="Aviones\\"
        ub+=str(i)+".png"
        im=Img(ub)
        Avion.append(im.img())
    for i in range(7):
        ub="Aviones\\J"
        ub+=str(i)+".png"
        im=Img(ub)
        Jet.append(im.img())
        xj.append(0-i*100)
        yj.append(200)


    #Soldadito
    countSol=0
    CorrerD,CorrerI=[],[]
    Disparar=[]
    Caer=[]
    caer=False
    correr=False
    disparar=False
    xs,ys=np.zeros(7),np.zeros(7)+200
    corrimiento=np.zeros(7)
    vsx=[4/7,4/7,4/7,-4/7,-4/7,-4/7,-4/7]
    vsy=-5
    numcaida=1
    countc,countd=0,0
    Misil=Img("Soldado\\Misil.png").img()
    xm,ym,vm=np.zeros(7)-10,680*np.ones(7),0
    for i in range(11):
        ub="Soldado\\"
        ub+=str(i)+".png"
        im=Img(ub)
        CorrerI.append(im.img())
        ub="Soldado\\Der"
        ub+=str(i)+".png"
        im=Img(ub)
        CorrerD.append(im.img())
        ub="Soldado\\D"
        ub+=str(i)+".png"
        im=Img(ub)
        if i%2==0:
            Disparar.append(im.img())
    Correr=[CorrerI,CorrerD]
    for i in range(5):
        ub="Soldado\\caer"
        ub+=str(i)+".png"
        im=Img(ub)
        Caer.append(im.img())


    #Pausa y game over
    Pausa=False
    fin=["Haz perdido, presiona 'enter' para reintentarlo","Puntaje total: ",""]
    muerte=[]
    for i in range(11):
        muerte.append(p.image.load("Nivel 4\\Imagenes\\Muerte\\"+str(i+1)+".png").convert_alpha())
    go=0
    game_over=False
    def G_o(a,i):
        pantalla.blit(muerte[0],(0,0))
        pantalla.blit(muerte[int(i)],(0,0))
        hola=font.render(a[0],True,(255,255,255))
        cent=hola.get_rect(center=(int(1280/2),int(700)))
        pantalla.blit(hola,cent)

    #Transición al jefe
    Jefe_4=False
    entrada=True

    #Variables Booleanas
    nivel_4=True

    while nivel_4:
        p.mouse.set_visible(0)
        for event in p.event.get():
            if event.type== p.QUIT:
                nivel_4=False
                sys.exit()
                return False
            if event.type == p.KEYDOWN:
                if event.key == p.K_w:
                    vely1=-10
                if event.key == p.K_s:
                    vely=10
                if event.key == p.K_d:
                    velx=10
                if event.key==p.K_a:
                    velx1=-10
                if event.key==p.K_SPACE:
                    if B==False:
                        B=True
                        canalbala.play(Balas)
                        angleb=angle
                        xb,yb=xp,yp
                if event.key==p.K_ESCAPE:
                        if Pausa==False:
                            Pausa=True
                        else:
                            Pausa=False
                if event.key==p.K_e:
                    if not T:
                        canalbomba.play(Bombas)
                        T=True
                        xbomb,ybomb=xp,yp
                        nbomb=0
                        if angle!=0:
                            direc=1
                        else:
                            direc=0
            if event.type==p.KEYUP:
                if event.key == p.K_d:
                    velx=0
                if event.key==p.K_a:
                    velx1=0
                if event.key == p.K_w:
                    vely1=0
                if event.key==p.K_s:
                    vely=0
        pantalla.blit(fondo,cfondo)
        puntos(score,vida,cvls)
        if Jefe_4:
            pantalla.fill((0,0,0))
            p.display.flip()
            p.time.Clock().tick(60)
            Cinematica_4.trans()
            mixer.music.pause()
            win,menu=Nivel_4_Jefe.Jefe_4(vida,score)
            mixer.music.stop()
            if win:
                mixer.music.load("Nivel 4\\Sonidos\\Sad Strings theme.wav")
                mixer.music.set_volume(1)
                mixer.music.play(-1)
                pantalla.fill((0,0,0))
                p.display.flip()
                Cinematica_4.c2()
                pantalla.fill((0,0,0))
                p.display.flip()
                Cinematica_4.creditos()
                return True, True
            if menu:
                pantalla.fill((0,0,0))
                p.display.flip()
                return True, win
        while entrada:
            if countsen==0:
                Cinematica_4.c1()
                mixer.music.stop()
                mixer.music.load("Nivel 4\\Sonidos\\p0ss_-_oga_-_rock_of_war.wav")
                countsen+=1
                mixer.music.play(-1)
                canalpausa.play(Spausa,-1)
                canalpausa.pause()
                canalHelicoptero.play(HelicopteroS,-1)
            for event in p.event.get():
                if event.type== p.QUIT:
                    nivel_4=False
                    entrada=False
                    sys.exit()
                if event.type == p.KEYDOWN:
                    if event.key == p.K_RETURN:
                        if saltar:
                            nc=2
                        else:
                            saltar=True
            pantalla.blit(fondo,cfondo)
            puntos(score,vida,cvls)
            if countgent<len(gented)-0.1:
                countgent+=0.1
            else:
                countgent=0 
            for i in range(20):
                xg[i]+=vxg[i]
                if xg[i]>1280 or xg[i]<0 or r.randint(0,100)==i:
                    vxg[i]=-vxg[i]   
                if vxg[i]>0:
                    mostrar(xg[i],yg[i],gented[int(countgent)])
                else:
                    mostrar(xg[i],yg[i],gentei[int(countgent)])
            #Nave
            if k<=58:
                k+=1
            else:
                k=0
            if xp<640:
                xp+=10
            mostrar(xp,yp,Nave[int(k)],angle)
            p.draw.rect(pantalla,(0,0,0),(120,600,int(w*700),int(h*100)))
            if saltar:
                mostrartext('Presiona "Enter" para continuar',len('Presiona "Enter" para continuar'),150,550,[1,1,1])
            if nc!=2:
                mostrartext(Dialogos[nc][0],int(k1),150,610)
                mostrartext(Dialogos[nc][1],int(k2),150,650)
                if countsen<4*len(senora)-0.4:
                    countsen+=0.4
                else:
                    if w<1:
                        w+=0.05
                        h+=0.05
                    else:
                        if k1<len(Dialogos[nc][0]):
                            k1+=0.3
                        else:
                            if k2<len(Dialogos[nc][1]):
                                k2+=0.3
                            else:
                                if count<300:
                                    count+=1
                                else:
                                    count=0
                                    nc+=1
                                    k1,k2=0,0
            else:
                if w>0:
                    w-=0.05
                    h-=0.05
                else:
                    if countsen>0.5:
                        countsen-=0.5
                    else:
                        k=0
                        entrada=False
                        break
            mostrar(50,650,senora[int(countsen)//4])
            clock.tick(60)
            p.display.update()

        #Gente
        if countgent<len(gented)-0.1:
            countgent+=0.1
        else:
            countgent=0 
        for i in range(20):
            if colision(xg[i],yg[i],xbomb,ybomb,50) and 1<=int(countExp)<=7 :
                xg[i],yg[i]=r.randint(0,1280),700
                cvls+=1
            xg[i]+=vxg[i]
            if xg[i]>1280 or xg[i]<0 or r.randint(0,100)==i:
                vxg[i]=-vxg[i]   
            if vxg[i]>0:
                mostrar(xg[i],yg[i],gented[int(countgent)])
            else:
                mostrar(xg[i],yg[i],gentei[int(countgent)])

        #Helicoptero
        if countH<len(Helicoptero[0][0])-0.2:
            countH+=0.2
        else:
            countH=0
        for i in range(7):
            mostrar(xh[i],yh[i],Helicoptero[HD[i]][H[i]][int(countH)])
            yh[i]+=vHy[i]
            xh[i]+=vHx[i]
            if 100>yh[i] or yh[i]>500 or r.randint(0,200)==2:
                vHy[i]*=-1
            if xh[i]<-100 or xh[i]>1380:
                vHx[i]*=-1
                if H[i]==0:
                    H[i]=1
                else:
                    H[i]=0
            if colision(xbH[i],ybH[i],xp,yp):
                disparableH[i]=True
                col=True
            if disparableH[i]:
                if r.randint(0,200)==2:
                    disparableH[i]=False
                    xbH[i],ybH[i]=xh[i],yh[i]
                    if not H[i]==0:
                        vbH[i]=-6
                    else:
                        vbH[i]=6
            else:
                xbH[i]+=vbH[i]
                if vbH[i]>0:
                    mostrar(xbH[i],ybH[i],balaH,180)
                else:
                    mostrar(xbH[i],ybH[i],balaH)
                if xbH[i]<0 or xbH[i]>1280:
                    disparableH[i]=True
            if colision(xh[i],yh[i],xb,yb):
                colH[i]=True
            if colision(xh[i],yh[i],xp,yp):
                col1=True
            if colH[i]:
                B=False
                if HD[i]==0:
                    HD[i]=1
                elif HD[i]==1:
                    HD[i]=2
                elif HD[i]==2:
                    HD[i]=3
                elif HD[i]==3:
                    if not explH[i]:
                        score+=punt
                        CEH.play(ExpHSound)
                        xexph[i],yexph[i]=xh[i],yh[i]
                    explH[i]=True
                    xh[i],yh[i]=-200,-100
                colH[i]=False
            if explH[i]:
                if expcount[i]<len(explosiones)-0.4:
                    expcount[i]+=0.4
                    mostrar(xexph[i],yexph[i],explosiones[int(expcount[i])])
        if countHel!=5:
            varios=False
            canalHelicoptero.unpause()
        else:
            n=0
            varios=True
            canalHelicoptero.pause()
        #Reiniciar H
        if explH[0] and explH[1] and explH[2] and explH[3] and explH[4] and explH[5] and explH[6]:
            if countHel<5:
                countHel+=1
            else:
                explH=[False,False,False,False,False,False,False]
            if countHel<=3:
                HD=[0,0,0,0,0,0,0]
                expcount=[0,0,0,0,0,0,0]
                explH=[False,False,False,False,False,False,False]
                xh,yh=[1380-1480*r.randint(0,1),1380-1480*r.randint(0,1),1380-1480*r.randint(0,1),1380-1480*r.randint(0,1),1380-1480*r.randint(0,1),1380-1480*r.randint(0,1),1380-1480*r.randint(0,1)],[r.randint(100,500),r.randint(100,500),r.randint(100,500),r.randint(100,500),r.randint(100,500),r.randint(100,500),r.randint(100,500)]

        #Corazon
        if vida>600:
            vida=600
        for i in range(n):
            if countheart<len(Heart)-0.1:
                countheart+=0.1
            else:
                countheart=0
            if xheart[i]>=-160:
                xheart[i]-=3
                mostrar(xheart[i],yheart[i],Heart[int(countheart)])
            else:
                xheart=[r.randint(1500,3000),r.randint(1500,3000),r.randint(1500,3000)]
                yheart=[r.randint(40,400),r.randint(40,400),r.randint(40,400)]
            if colision_corazon(xheart[i],yheart[i],xp,yp):
                canalsalud.play(Salud)
                xheart[i]-=r.randint(2000,3000)
                yheart[i]=r.randint(40,400)
                if vida<600:
                    vida+=50

        #Avion
        canalplane.play(plane,-1)
        if not 0<=countA<len(Avion)-0.2:
            dca*=-1
        countA+=dca
        if xa==-100:
            u=100*r.randint(2,4)
        if xa<=1380:
            xa+=10
        else:
            xa=-100
        if colision(xa,ya,xp,yp):
            col=True
            canalbombaA.play(explosionesA)
            xexpA[2],yexpA[2]=xa,ya
            xa=-100
            explA[2]=True
            countexpA=0
        if explA[2]:
            if countexpA<len(explosiones)-0.4:
                countexpA+=0.4
            else:
                explA[2]=False
            mostrar(xexpA[2],yexpA[2],explosiones[int(countexpA)])
        a1=-4*u/(1280)**2
        b1=-1280*a1
        ya=a1*xa**2+b1*xa
        mostrar(xa,ya,Avion[int(countA)])
        if varios:
            for i in range(2):
                mostrar(xav[i],yav[i],Avion[int(countA)],angleav[i])
                xav[i]+=velav[i]
                if xav[0]<-100:
                    xav[0]=1380
                    yav[0]=100*r.randint(1,4)
                if xav[1]>1380:
                    xav[1]=-100
                    yav[1]=100*r.randint(1,4)
                if colision(xav[i],yav[i],xp,yp):
                    col=True
                    canalbombaA.play(explosionesA)
                    xexpA[i],yexpA[i]=xav[i],yav[i]
                    xav[i]=-100
                    explA[i]=True
                    countexpA=0
                if explA[i]:
                    if countexpA<len(explosiones)-0.4:
                        countexpA+=0.4/2
                    else:
                        explA[i]=False
                    mostrar(xexpA[i],yexpA[i],explosiones[int(countexpA)])

        #Soldado
        if countc<len(Correr[0])-0.4:
            countc+=0.4
        else:
            countc=0

        #Jet y soldados
        if xj[6]>=-100:
            if 0<=countJ<len(Jet)-0.1:
                countJ+=0.1
                for i in range(7):
                    xs[i],corrimiento[i]=xj[i],xj[i]
            else:
                canalJet.pause()
                caer=True
                tj+=0.1
                aj+=tj
        if 0<xj[0]<1280 and not caer:
            canalJet.unpause()
            canalJet.play(JetS,-1)
        else:
            canalJet.pause()
        for i in range(7):
            yj[i]+=0.2*tj**2
            xj[i]+=vj
            if yj[i]<720:
                mostrar(xj[i],yj[i],Jet[int(countJ)],aj)
            if caer:
                if ys[i]<=50:
                    vsy*=-1/3
                    numcaida=0
                ys+=vsy/7
                if vsy>0:
                    xs=20*np.cos(ys/20)+corrimiento
                if not ys[1]>700:
                    mostrar(xs[i],ys[i],Caer[numcaida],10*np.sin(ys[i]/21))
                else:
                    correr=True
            if correr:
                if colision(xs[i],ys[i],xbomb,ybomb,50) and 1<=int(countExp)<=7:
                    xs[i],ys[i]=-1500,1500
                countJ=-1
                vsy=0
                caer=False
                xs+=vsx
                if xs[i]<20 or xs[i]>1260:
                    vsx[i]*=-1
                if vsx[i]!=0:
                    if xs[i]>-100:
                        mostrar(xs[i],ys[i],Correr[int((vsx[i]/abs(vsx[i])+1)/2)][int(countc)])
                if vm==0:
                    if r.randint(0,500)==2:
                        disparar=True
                else:
                    if ym[i]!=800:
                        ym[i]+=vm
                    mostrar(xm[i],ym[i],Misil,90)
                    if colision(xp,yp,xm[i],ym[i]):
                        ym[i]=800
                        col=True
                    if ym[i]<-100:
                        ym=700*np.ones(7)
                        vm=0
            if disparar:
                if colision(xs[i],ys[i],xbomb,ybomb,50) and 1<=int(countExp)<=7 :
                    xs[i],ys[i]=-1500,1500
                vsx[i]=0
                if countd<len(Disparar)-0.15/7:
                    correr=False
                    countd+=0.15/7
                else:
                    CDS.play(DSS)
                    ym=np.ones(7)*680
                    xm[0],xm[1],xm[2],xm[3],xm[4],xm[5],xm[6]=xs[0],xs[1],xs[2],xs[3],xs[4],xs[5],xs[6]
                    vm=-5
                    vsx=[4/7-8/7*r.randint(0,1),4/7-8/7*r.randint(0,1),4/7-8/7*r.randint(0,1),4/7-8/7*r.randint(0,1),4/7-8/7*r.randint(0,1),4/7-8/7*r.randint(0,1),4/7-8/7*r.randint(0,1)]
                    disparar=False
                    countd=0
                    correr=True
                mostrar(xs[i],ys[i]-10,Disparar[int(countd)])

        #Reiniciar Soldados
        if -2000<=xs[0]<=-1000 and -2000<=xs[1]<=-1000 and -2000<=xs[2]<=-1000 and -2000<=xs[3]<=-1000 and -2000<=xs[4]<=-1000 and -2000<=xs[5]<=-1000 and -2000<=xs[6]<=-1000:
            if countSol<3:
                countSol+=1
                caer,correr,disparar=False,False,False
            if countSol<=2:
                tj=0
                aj=0
                vsy=-5
                xs,ys=np.zeros(7),np.zeros(7)+200
                score+=7*punt
                xj=[0,-100,-200,-300,-400,-500,-600]
                yj=[200,200,200,200,200,200,200]
                countJ=0
                caer,correr,disparar=False,False,False

        #Cambio de fase
        if countSol==3 and countHel==5:
            countSol+=1
            countHel+=1
            Jefe_4=True
        
        #Nave
        if xp<=40:
            xp=40
        elif xp>=1240:
            xp=1240
        xp+=velx+velx1
        if yp<=40:
            yp=40
        elif yp>=400:
            yp=400
        yp+=vely+vely1
        if velx1:
            angle=180
        if velx:
            angle=0
        if k<=58:
            k+=1
        else:
            k=0

        #colision nave
        if col:
            if numcol<10:
                numcol+=1
                pantalla.blit(live[-1],(1000,25))
            else:
                if vida>0:
                    vida-=50
                    colnaves.play(colnave)
                numcol=0
                col=False

        if col1:
            if numcol1<10:
                numcol1+=1
                pantalla.blit(live[-1],(1000,25))
            else:
                if vida>0:
                    vida-=25
                numcol1=0
                colnaves.play(colnave)
                col1=False

        #Bala
        if nb<=12:
            nb+=0.5
        else:
            nb=0
        if B:
            if xb<0 or xb>1280:
                B=False
            if angleb==0:
                vb=30
            else:
                vb=-30
            xb+=vb
            mostrar(xb,yb,bala[int(nb)],angleb)
        else:
            xb,yb=-100,-100
        
        #Bomba
        if nbomb<len(BombaD)-0.15:
            nbomb+=0.15
        if T:
            if ybomb>=700:
                if countExp<len(Explosion)-0.3:
                    if 0.9-0.01<=countExp<=0.9+0.01:
                        canalexpbomb.play(Expbomba)
                    countExp+=0.3
                    mostrar(xbomb,700-30,Explosion[int(countExp)])
                else:
                    countExp=0
                    T=False
            else:
                ybomb+=vbomb
                mostrar(xbomb,ybomb,Bomba[direc][int(nbomb)])
        else:
            xbomb,ybomb=-100,-100
        mostrar(xp,yp,Nave[k],angle)
        clock.tick(60)
        while Pausa:
            canalpausa.unpause()
            mixer.music.pause()
            clock.tick(60)
            canalHelicoptero.pause()
            canalplane.pause()
            canalJet.pause()
            menu=Cinematica_1_1.pause()
            if menu:
                nivel_4=False
                mixer.music.stop()
                canalpausa.stop()
                return True,False
            Pausa=False
            canalpausa.pause()
            mixer.music.unpause()
            clock.tick(60)
            if countHel!=5:
                canalHelicoptero.unpause()
            canalplane.unpause()
            if 0<xj[0]<1280 and not caer:
                canalJet.unpause()            
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
            canalHelicoptero.pause()
            canalplane.pause()
            canalJet.pause()
            for event in p.event.get():
                if event.type== p.QUIT:
                    game_over=False
                    nivel_4=False
                    return False
                if event.type == p.KEYDOWN:
                    if event.key == p.K_RETURN:
                        vida=300
                        score=score0
                        go=0
                        cvls=0
                        countH=0
                        HD=[0,0,0,0,0,0,0]
                        expcount=[0,0,0,0,0,0,0]
                        explH=[False,False,False,False,False,False,False]
                        xh,yh=[1380-1480*r.randint(0,1),1380-1480*r.randint(0,1),1380-1480*r.randint(0,1),1380-1480*r.randint(0,1),1380-1480*r.randint(0,1),1380-1480*r.randint(0,1),1380-1480*r.randint(0,1)],[r.randint(100,500),r.randint(100,500),r.randint(100,500),r.randint(100,500),r.randint(100,500),r.randint(100,500),r.randint(100,500)]
                        tj=0
                        aj=0
                        vsy=-5
                        countHel=0
                        xs,ys=np.zeros(7),np.zeros(7)+200
                        countSol=0
                        xj=[0,-100,-200,-300,-400,-500,-600]
                        yj=[200,200,200,200,200,200,200]
                        countJ=0
                        xa=-100
                        col,col1=False,False
                        explA=[False,False,False]
                        caer,correr,disparar=False,False,False
                        xp,yp=1280/2,720/2
                        velx,vely,velx1,vely1=0,0
                        canalHelicoptero.unpause()
                        canalplane.unpause()
                        mixer.music.unpause()
                        if game_over==True:
                            game_over=False
            p.display.update()
        p.display.update()