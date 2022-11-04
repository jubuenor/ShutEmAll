import random
import math as m
import pygame as p
from pygame import mixer
import Cinematica_1_1
#Configuraciones de pantalla
def J(score=300,vida=300,nombre="Holis",t_v="True",act=False,ent_torr1=[1400,640,-100],Tiempo_t=0,dt=0):
    info = open("Guardado.txt", "r")
    text=info.readline().replace("\n","")
    info.close()
    info=open(text+".txt","r")
    nombrein = str(info.readline()).replace("\n","")
    puntajein = int(info.readline().replace("\n",""))
    nvlin=int(info.readline().replace("\n",""))
    scorei=int(info.readline().replace("\n",""))
    info.close()
    p.init() #Iniciar programa
    clock = p.time.Clock()
    #Sonidos
    exps=mixer.Sound("Nivel 1\\Sonidos\\Explosion.wav")
    sonidob=mixer.Sound("Nivel 1\\Sonidos\\Disparo.wav")
    Spausa=mixer.Sound("Sonidos\\SpacyLoop.ogg")
    lose=mixer.Sound("Sonidos\\lose music.ogg")
    channel1 = mixer.Channel(0)
    channel2 = mixer.Channel(1)
    canalpausa=mixer.Channel(2)
    canalpausa.set_volume(0.3)
    canalpausa.play(Spausa,-1)
    canallose=mixer.Channel(3)
    canalpausa.pause()
    #vida=300
    x=1280
    y=720
    punt=500
    pantalla = p.display.set_mode((x,y))
    p.display.set_caption("Shut 'em all")
    fondo = p.image.load('Nivel 1\\Imagenes\\Fondo2.png').convert()
    cfondo=fondo.get_rect(center=(int(x/2),int(y/2)))
    #Personaje
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
    #nombre="Qlo"
    Titulo="Nivel 1: Defiéndenos"
    font=p.font.Font('Nivel 1\\Fuentes\\BLADRMF_.TTF',28)
    font1=p.font.Font('Nivel 1\\Fuentes\\BLADRMF_.TTF',15)
    fonttext=p.font.Font('Nivel 1\\Fuentes\\Timeless-Bold.ttf',40)
    fonttext2=p.font.Font('Nivel 1\\Fuentes\\Timeless-Bold.ttf',25)
    fontp=p.font.Font('Nivel 1\\Fuentes\\BLADRMF_.TTF',20)
    podertxt=fontp.render("Poder",True,(255,0,0))
    def name(a):
        hola=fonttext.render(a,True,(255,255,255))
        cent=hola.get_rect(center=(int(1280/2),50))
        pantalla.blit(hola,cent)
    #Balas pai :v
    bala=p.image.load("Nivel 1\\Imagenes\\Bala.png")
    coord_b=[-1000,-1000]
    coord_b1=coord_b
    a=0
    a1=a
    vel_b=8
    i=0
    r=100
    B=["Invisible","Invisible"]
    def disparar(a,x,y):
        Rotar=p.transform.rotozoom(bala,a,1)
        Recto=Rotar.get_rect(center=(int(x),int(y)))
        pantalla.blit(Rotar,Recto)
    #puntos
    #score=0
    colp=False
    numcolp=0
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
    #Jefe
    v_j=0.6
    j=0
    colJ=[p.image.load("Nivel 1\\Imagenes\\ColJ1.png"),p.image.load("Nivel 1\\Imagenes\\ColJ2.png"),p.image.load("Nivel 1\\Imagenes\\ColJ3.png"),p.image.load("Nivel 1\\Imagenes\\J3.png")]
    numcol,numcol2=0,0
    colvid1=False
    colvid2=False
    colvidt1,colvidt2=False,False
    numcolt1,numcolt2=0,0
    col=[p.image.load("Nivel 1\\Imagenes\\ColHealth.png"),p.image.load("Nivel 1\\Imagenes\\ColHealth2.png"),p.image.load("Nivel 1\\Imagenes\\ColHealth1.png"),p.image.load("Nivel 1\\Imagenes\\Health0.png")]
    ccol=col[3].get_rect(center=(int(x/2),int(690)))
    Nombre=font1.render("Jefe de la far",True,(255,255,255))
    cnombre=Nombre.get_rect(center=(int(x/2),int(690)))
    Jefe=[p.image.load("Nivel 1\\Imagenes\\J1.png"),p.image.load("Nivel 1\\Imagenes\\J2.png"),p.image.load("Nivel 1\\Imagenes\\J3.png"),p.image.load("Nivel 1\\Imagenes\\J3.png")]
    saludimg=[p.image.load("Nivel 1\\Imagenes\\Health.png"),p.image.load("Nivel 1\\Imagenes\\Health2.png"),p.image.load("Nivel 1\\Imagenes\\Health1.png"),p.image.load("Nivel 1\\Imagenes\\Health0.png")]
    salud_j=5000
    coord_J=[500,-200]
    coord_S=[140,800]
    def mov_Jefe(a,i):
        pantalla.blit(Jefe[i],(int(a[0]),int(a[1])))
    def salud_jefe(y,x1,j):
        Nombre=font1.render("Jefe de la far",True,(255,255,255))
        nombre=Nombre.get_rect(center=(int(x1/2),int(y)))
        psalud=saludimg[3].get_rect(center=(int(x1/2),int(y)))
        pantalla.blit(saludimg[3],psalud)
        pantalla.blit(saludimg[j],psalud)
        pantalla.blit(Nombre,nombre)
    #Misiles Jefe
    misiles=[p.image.load("Nivel 1\\Imagenes\\Misil\\M1.png"),p.image.load("Nivel 1\\Imagenes\\Misil\\M2.png"),p.image.load("Nivel 1\\Imagenes\\Misil\\M3.png"),p.image.load("Nivel 1\\Imagenes\\Misil\\M4.png"),p.image.load("Nivel 1\\Imagenes\\Misil\\M5.png"),p.image.load("Nivel 1\\Imagenes\\Misil\\M6.png"),p.image.load("Nivel 1\\Imagenes\\Misil\\M7.png"),p.image.load("Nivel 1\\Imagenes\\Misil\\M8.png")]
    countM1,countM2=0,0
    v_m=0.6
    xm1,ym1,xm2,ym2=1280/2,-100,1280/2+200,-500
    def mis(x,y,countM):
        Rotar=p.transform.rotozoom(misiles[countM//20],90,1)
        Recto=Rotar.get_rect(center=(int(x),int(y)))
        pantalla.blit(Rotar,Recto)
    #Torretas
    expbt1,expbt2=False,False
    numexbt1,numexbt2=0,0
    xbt1,ybt1,xbt2,ybt2=0,0,0,0
    disparar_torreta1,disparar_torreta2=False,False
    p_u=p.image.load("Nivel 1\\Imagenes\\P1.png")
    coord_p_u=[random.randint(300,1000),-300,random.randint(300,1000),-300,1000,1000]
    coord1=[1200,640]
    coord2=[100,640]
    def poder(a):
        angulo1=-180*m.atan((640-a[1])/(1200-a[0]))/m.pi+180
        angulo2=180*m.atan((640-a[1])/(200+a[0]))/m.pi
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
    #Colisiones
    def colisiones(x1,x2,y1,y2,r):
        colision=False
        distancia=m.sqrt((x1-x2)**2+(y1-y2)**2)
        if distancia<=r:
            colision=True
        return colision
    #Colisiones con el jefe
    def col_J(a,b):
        colision=False
        if a[0]<=b[0]<=a[0]+500 and b[1]<=a[1]+150:
            colision = True
        return colision
    #Pausa y fin
    muy_bien=["Haz  conseguido derrotar al villano, Felicitaciones.","Presiona 'esc' para continuar."]
    Pausa=False
    color=0
    cp=0
    wn=0
    ganar=[]
    for i in range(11):
        ganar.append(p.image.load("Nivel 1\\Imagenes\\Ganaste\\"+str(i+1)+".png").convert_alpha())
    def WIN(a,color,i):
        pantalla.blit(ganar[0],(0,0))
        pantalla.blit(ganar[int(i)],(0,0))
        hola=font.render(a[0],True,(color*255,color*255,color*255))
        KK=font.render(a[1],True,(color*255,color*255,color*255))
        centh=hola.get_rect(center=(int(1280/2),int(680-100)))
        centK=KK.get_rect(center=(int(1280/2),int(680)))
        pantalla.blit(hola,centh)
        pantalla.blit(KK,centK)
    #Explosiones
    xb1,yb1,xb2,yb2=0,0,0,0
    xj,yj=0,0
    expj=False
    expb1=False
    expb2=False
    numexp1,numexb1,numexb2=0,0,0
    explosion=[p.image.load("Nivel 1\\Imagenes\\Exp\\Exp1.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp2.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp3.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp4.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp5.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp6.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp7.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp8.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp9.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp10.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp11.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp12.png"),p.image.load("Nivel 1\\Imagenes\\Exp\\Exp13.png")]
    def expl(x,y,numexp):
        pantalla.blit(explosion[numexp//6],(int(x),int(y)))
    #Game over
    fin=["Haz perdido, presiona 'enter' para reintentarlo","Puntaje total: ",""]
    muerte=[]
    for i in range(11):
        muerte.append(p.image.load("Nivel 1\\Imagenes\\Muerte\\"+str(i+1)+".png").convert_alpha())
    go=0
    def G_o(a,i):
        pantalla.blit(muerte[0],(0,0))
        pantalla.blit(muerte[int(i)],(0,0))
        hola=font.render(a[0],True,(255,255,255))
        cent=hola.get_rect(center=(int(1280/2),int(700)))
        pantalla.blit(hola,cent)
    #Juego :v
    game_over=False
    Win=False
    nivel_1J=True
    while nivel_1J:
        p.mouse.set_visible(0)
        for event in p.event.get():
            if event.type== p.QUIT:
                nivel_1J=False
                return 0,False, False, False
            if event.type == p.KEYDOWN:
                if event.key == p.K_d or event.key==p.K_RIGHT:
                    vel=-1
                if event.key == p.K_a or event.key==p.K_LEFT:
                    vel=1
                if event.key==p.K_SPACE:
                    if coord_J[1]==0:
                        if i==0:
                            if B[0]=="Invisible":
                                B[0]="Visible"
                                channel2.play(sonidob)
                                a=angulo
                                coord_b[0],coord_b[1]=coord_p[0],coord_p[1]
                        elif i==1:
                            if B[1]=="Invisible":
                                B[1]="Visible"
                                channel2.play(sonidob)
                                a1=angulo
                                coord_b1[0],coord_b1[1]=coord_p[0],coord_p[1]
                if event.key==p.K_e or event.key==p.K_RETURN:
                    if t_v:
                        if not act:
                            act=True
                            t_v=False
                if event.key == p.K_ESCAPE:
                    if Pausa==False:
                        mixer.music.pause()
                        canalpausa.play(Spausa)
                        Pausa=True
            if event.type==p.KEYUP:
                if event.key == p.K_a or event.key == p.K_d or event.key==p.K_LEFT or event.key==p.K_RIGHT:
                    vel=0
        pantalla.fill((0,0,0))
        clock.tick(120)
        pantalla.blit(fondo,cfondo)
        #Movimiento de la torreta            
        if angulo<0:
            angulo=0
            vel=0
        elif angulo>180:
            angulo=180
            vel=0
        else:
            angulo+=vel
        #Torretas
        pantalla.blit(podertxt,(1010,680))
        p.draw.rect(pantalla,(int(255/2),int(255/2),int(255/2)),(990,600,140,80))
        p.draw.rect(pantalla,(0,0,0),(990,600,140,80),4)
        #Disparos torretas
        if disparar_torreta1:
            angulo1=m.atan((640-coord_J[1])/(1200-coord_J[0]))
            coord1[0]-=(vel_b)
            coord1[1]=((640-coord_J[1])/(1000-coord_J[0]))*(coord1[0]-1200)+640
            disparar(180-180*angulo1/m.pi,coord1[0],coord1[1])
        if disparar_torreta2:
            angulo2=m.atan((640-coord_J[1])/(100+coord_J[0]))
            coord2[0]+=(vel_b)
            coord2[1]=((640-coord_J[1])/(-200-coord_J[0]))*(coord2[0]-100)+640
            disparar(180*angulo2/m.pi,coord2[0],coord2[1])
        if coord1[1]<=163:
            channel1.play(exps)
            salud_j-=100
            xbt1,ybt1=coord1[0],coord1[1]-100
            colvidt1=True
            expbt1=True
            disparar_torreta1=False
            coord1[0],coord1[1]=1200,640
        if coord2[1]<=163:
            channel1.play(exps)
            colvidt2=True
            salud_j-=100
            expbt2=True
            xbt2,ybt2=coord2[0],coord2[1]-100
            disparar_torreta2=False
            coord2[0],coord2[1]=100,640
        #Torretas poderes
        if t_v:
            coord_p_u[4],coord_p_u[5]=1000,600
            pantalla.blit(p_u,(coord_p_u[4],coord_p_u[5]))
        if act:
            dt=1
            if ent_torr1[2]>=100 and ent_torr1[0]<=1200:
                poder(coord_J)
            else:
                ent_torr1[0]-=0.5
                ent_torr1[2]+=0.5
                entrada(ent_torr1)
        #Salida de torretas
        Tiempo_t+=dt
        if Tiempo_t<=2600:
            if (Tiempo_t+1)%400==0:
                channel2.play(sonidob)
                disparar_torreta1=True
                disparar_torreta2=True
        if Tiempo_t>=2600:
            if ent_torr1[2]>=-100 and ent_torr1[0]<=1400:
                act=False
                ent_torr1[0]+=0.5
                ent_torr1[2]-=0.5
                entrada(ent_torr1)
                if ent_torr1[2]==-100 and ent_torr1[0]==1400:
                    Tiempo_t=0
                    dt=0
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
        #Mov Jefe
        if -200<=coord_J[1]<0:
            coord_J[1]+=0.6
        else:
            coord_J[1]=0
            if coord_J[0]>=780:
                v_j=-v_j
            elif coord_J[0]<=0:
                v_j=-v_j
            coord_J[0]+=v_j
        #Misil
        if countM1<=8*20-2:
            countM1+=1
        else:
            countM1=0
        if ym1<=760:
            ym1+=v_m
        else:
            vida-=50
            ym1=-50
        if ym1<=163/2:
            xm1=coord_J[0]+200
        if ym1>=163/2:
            mis(xm1,ym1,countM1)
        if countM2<=8*20-2:
            countM2+=1
        else:
            countM2=0
        if ym2<=760:
            ym2+=v_m
        else:
            vida-=50
            ym2=-50
        if ym2<=163/2:
            xm2=coord_J[0]+400
        if ym2>=163/2:
            mis(xm2,ym2,countM2)
        #Colisiones Jefe
        if salud_j > 0:
            if col_J(coord_J,coord_b):
                xb1,yb1=coord_b[0],coord_b[1]-100
                expb1=True
                colvid1=True
                salud_j -=100
                B[0]="Invisible"
                coord_b=[-1000,-1000]
            if col_J(coord_J,coord_b1):
                xb2,yb2=coord_b1[0],coord_b1[1]-100
                expb2=True
                colvid2=True
                salud_j-=100
                B[1]="Invisible"
                coord_b1=[-1000,-1000]
        if coord_S[1]>690:
            coord_S[1]-=0.4
        else:
            coord_S[1]=690
        if salud_j<=5000/3:
            j=2
            v_m=1
            if abs(v_j)!=1:
                if v_j>0:
                    v_j=2
                else:
                    v_j=-2
        elif salud_j<=2*5000/3:
            j=1
            v_m=0.8
            if abs(v_j)!=1:
                if v_j>0:
                    v_j=1
                else:
                    v_j=-1
        #Colisiones
        if colisiones(xm1,coord_b[0],ym1,coord_b[1],50):
            xb1,yb1=xm1-40,ym1-40
            coord_b=[-100,-200]
            B[0]="Invisible"
            expb1=True
            i=1
            score+=punt
            if j==0:
                ym1=ym2-500
            elif j==1 or j==2:
                ym1=-100
        if colisiones(xm2,coord_b[0],ym2,coord_b[1],50):
            xb1,yb1=xm2-40,ym2-40
            coord_b=[-1000,-2000]
            expb1=True
            B[0]="Invisible"
            i=1
            score+=punt
            if j==0:
                ym2=ym1-500 
            elif j==1 or j==2:
                ym2=-100
        if colisiones(xm1,coord_b1[0],ym1,coord_b1[1],50):
            xb2,yb2=xm1-40,ym1-40
            coord_b1=[-1000,-2000]
            B[1]="Invisible"
            expb2=True
            i=0
            score+=punt
            if j==0:
                ym1=ym2-500
            elif j==1 or j==2:
                ym1=-100
        if colisiones(xm2,coord_b1[0],ym2,coord_b1[1],50):
            xb2,yb2=xm2-40,ym2-40
            coord_b1=[-1000,-2000]
            expb2=True
            B[1]="Invisible"
            i=0
            score+=punt
            if j==0:
                ym2=ym1-500
            elif j==1 or j==2:
                ym2=-100
        if colisiones(xm2,coord_p[0],ym2,coord_p[1],50):
            if j==0:
                ym2=ym1-500
            elif j==1 or j==2:
                ym2=-100
            colp=True
            vida-=50
        if colisiones(xm1,coord_p[0],ym1,coord_p[1],50):
            if j==0:
                ym1=ym2-500
            elif j==1 or j==2:
                ym1=-100
            colp=True
            vida-=50
        mov_Jefe(coord_J,j)
        name(Titulo)  
        torret(angulo,coord_p[0],coord_p[1])
        salud_jefe(coord_S[1],x,j)
        #Explosiones
        if expb1:
            if numexb1<=10:
                channel1.play(exps)
            if numexb1<=6*13-2:
                numexb1+=1
            else:
                numexb1=0
                expb1=False
            expl(xb1,yb1,numexb1)
        if expb2:
            if numexb2<=10:
                channel1.play(exps)
            if numexb2<=6*13-2:
                numexb2+=1
            else:
                numexb2=0
                expb2=False
            expl(xb2,yb2,numexb2)
        if expbt2:
            if numexbt2<=6*13-2:
                numexbt2+=1
            else:
                numexbt2=0
                expbt2=False
            expl(xbt2,ybt2,numexbt2)
        if expbt1:
            if numexbt1<=6*13-2:
                numexbt1+=1
            else:
                numexbt1=0
                expbt1=False
            expl(xbt1,ybt1,numexbt2)
        if colvid1:
            if numcol<=7:
                numcol+=1
                pantalla.blit(col[j],ccol)
                pantalla.blit(colJ[j],(int(coord_J[0]),int(coord_J[1])))
                pantalla.blit(col[j],ccol)
                pantalla.blit(Nombre,cnombre)
            else:
                numcol=0
                colvid1=False
        if colvid2:
            if numcol2<=7:
                numcol2+=1
                pantalla.blit(col[j],ccol)
                pantalla.blit(colJ[j],(int(coord_J[0]),int(coord_J[1])))
                pantalla.blit(Nombre,cnombre)
            else:
                numcol2=0
                colvid2=False
        if colvidt2:
            if numcolt2<=7:
                numcolt2+=1
                pantalla.blit(col[j],ccol)
                pantalla.blit(colJ[j],(int(coord_J[0]),int(coord_J[1])))
                pantalla.blit(Nombre,cnombre)
            else:
                numcolt2=0
                colvidt2=False
        if colvidt1:
            if numcolt1<=7:
                numcolt1+=1
                pantalla.blit(col[j],ccol)
                pantalla.blit(colJ[j],(int(coord_J[0]),int(coord_J[1])))
                pantalla.blit(Nombre,cnombre)
            else:
                numcolt1=0
                colvidt1=False
        if colp:
            if numcolp<=7:
                pantalla.blit(live[-1],(1000,25))
                numcolp+=1
            else:
                numcolp=0
                colp=False
        puntos(score,vida)
        if salud_j==0:
            j=3
            expj=True
            xj,yj=coord_J[0],coord_J[1]+50
            v_j=0
            while expj:
                if numexp1<=7:
                    channel1.play(exps)
                if numexp1 <=13*6-4:
                    numexp1+=2
                else:
                    xj+=40
                    numexp1=0
                pantalla.blit(fondo,cfondo)
                mov_Jefe(coord_J,j)
                name(Titulo)  
                puntos(score,vida)
                torret(angulo,coord_p[0],coord_p[1])
                salud_jefe(coord_S[1],x,j)
                expl(xj,yj,numexp1)
                if xj>=coord_J[0]+400:
                    Win=True
                    expj=False
                p.display.update()
        if vida<=0:
            game_over=True
            canallose.play(lose)
        while game_over:
            mixer.music.pause()
            G_o(fin,go)
            if go<10:
                go+=0.3
            for event in p.event.get():
                if event.type== p.QUIT:
                    game_over=False
                    nivel_1J=False
                    return 0,False, False, False
                if event.type == p.KEYDOWN:
                    if event.key == p.K_RETURN:
                        if game_over==True:
                            mixer.music.unpause()
                            game_over=False
                        t_v=False
                        nivel_1J=False
                        return 1,True, False, False
            p.display.update()
        while Pausa:
            menu=Cinematica_1_1.pause()
            Pausa=False
            canalpausa.pause()
            mixer.music.unpause()
            if menu:
                return 1,True,False,True
                mixer.music.pause()
            p.display.update()
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
                    nivel_1J=False
                if event.type == p.KEYDOWN:
                    if event.key == p.K_ESCAPE:
                        Save=open("Guardado.txt","r")
                        text=int(Save.readline())
                        Save.close()
                        Save=open(str(text)+".txt","w")
                        Save.close()
                        Save=open(str(text)+".txt","a")
                        Save.write(nombre+"\n")
                        Save.write(str(score+vida)+"\n")
                        Save.write("1"+"\n")
                        Save.write(str(scorei))
                        Save.close()
                        if Win==True:
                            Win=False
                            nivel_1J=False
                            return 0,False,True,False
            p.display.update()
        p.display.update()