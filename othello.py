#!/usr/bin/env python3.6
# _*_ coding: utf-8 _*_
#par alflo
from tkinter import*
air=Tk()
#cote damier
cote_case=40
nb_case=17
marge=2
cote=marge*(nb_case+1)+cote_case*nb_case
pas=(cote-marge)/nb_case
r_pion=19
pion_blanc=0
pion_noir=0
#cote gros pion
xx=100
yy=100
g_pion=20
teinte="black"
#creation damier
damier=Canvas(air,height=cote,width=cote,bg="gray")
damier.pack(side=LEFT)
#creation droite ecran
titre=Canvas(air,width=650,height=100,bg="gray")
txt=titre.create_text(300,50,text="OTHELLO",font="Arial 30 italic")
titre.pack(side=TOP)
regle_jeu=Canvas(air,height=200,width=650,bg="gray" )
txt=regle_jeu.create_text(300,100,text="bienvenue,\nle but est d'encadrer la couleur adverse\npar sa couleur \nsur une ligne et ou colonne et ou diagonale.\nafin de convertir à sa couleur les pions adverses\nattention rien n'est acquit",font="Arial 16 italic")
regle_jeu.pack()
"""listeOption=("noir","blanc","rouge","bronze","doré","argenté","bleu")
v=StringVar()
v.set(listeOption[0])
om=OptionMenu(root,v,*listeOption)"""
#barre menu
def c_c():
	v=StringVar()
	#choix_couleur=["black","white","red","brown","gold","gray","blue"]
	menubar=Menu(air)
	menu1=Menu(menubar,tearoff=0)
	menu1.add_command(label="noir",command=1)
	menu1.add_command(label="blanc",command=2)
	menu1.add_command(label="rouge",command=3)
	menu1.add_command(label="bronze",command=4)
	menu1.add_command(label="doré",command=5)
	menu1.add_command(label="argenté",command=6)
	menu1.add_command(label="bleue",command=7)
	menubar.add_cascade(label="couleur joueur 1",menu=menu1)

	
	menu2=Menu(menubar,tearoff=0)
	menu2.add_command(label="noir")
	menu2.add_command(label="blanc")
	menu2.add_command(label="rouge")
	menu2.add_command(label="bronze")
	menu2.add_command(label="doré")
	menu2.add_command(label="argenté")
	menu2.add_command(label="bleue")
	menubar.add_cascade(label="couleur joueur 2",menu=menu2)
	
	menu3=Menu(menubar,tearoff=0)
	menu3.add_command(label="noir")
	menu3.add_command(label="blanc")
	menu3.add_command(label="rouge")
	menu3.add_command(label="bronze")
	menu3.add_command(label="doré")
	menu3.add_command(label="argenté")
	menu3.add_command(label="bleue")
	menubar.add_cascade(label="couleur plateau",menu=menu3)
	
	air.config(menu=menubar)
	#print(v)
#choix couleur
"""teinte=Listbox(air)
teinte=StringVar()
teinte.insert(1,"noir/blanc")
teinte.insert(2,"rouge/bleue")
teinte.insert(3,"bronze/doré")
teinte.insert(4,"vert/jaune")
teinte.pack(side=TOP)
print(teinte)"""
#gros pion
qui_joue=Canvas(air,width=200,height=200,bg="gray")
txt1=qui_joue.create_text(100,20,text="LES",font="arial 16 italic")
txt2=qui_joue.create_text(100,180,text="JOUENT",font="arial 16 italic")
qui_joue.pack(side=LEFT)
#tableau score
tab_score=Canvas(air,width=440,height=200,bg="gray")
txt3=tab_score.create_text(225,20,text="TABLEAU DES SCORES",font="arial 16 italic")
tab_score.create_oval(110-r_pion,155-r_pion,110+r_pion,155+r_pion,fill="black",outline="gold")
tab_score.create_oval(110-r_pion,65-r_pion,110+r_pion,65+r_pion,fill="white",outline="gold")
txt4=tab_score.create_text(150,155,text="0",font="Arial 30 italic")
txt5=tab_score.create_text(150,65,text="0",font="Arial 30 italic")
tab_score.pack(side=RIGHT)

def colonne(cote,nb_case,pas,marge):
	i=1
	y=0
	while i<=nb_case+1:
		damier.create_line(i*pas-pas+1,y,i*pas-pas+1,cote,fill='black',width=marge)
		i+=1
def ligne(cote,nb_case,pas,marge):
	i=1
	x=0
	while i<=nb_case+1:
		damier.create_line(x,i*pas-pas+1,cote,i*pas-pas+1,fill='black',width=marge)
		i+=1

choix_couleur=["black","white","red","brown","gold","gray","blue"]
liste=[[" "]*(int(nb_case+1)) for loop in range(int(nb_case+1))]
liste[int((nb_case-1)/2)][int((nb_case-1)/2)]="n"
liste[int((nb_case-1)/2)][int((nb_case-1)/2+1)]="b"	
liste[int((nb_case-1)/2+1)][int((nb_case-1)/2)]="b"	
liste[int((nb_case-1)/2+1)][int((nb_case-1)/2+1)]="n"
tour=[]
pas=42
marge=2
r_pion=19
def centrage_pion (event):
	x=event.x
	y=event.y
	print("x=",x)
	print("y=",y)
	pas=42
	marge=2
	if pas/2<x%pas:
		x=(x//pas)*pas+pas+marge
		lon=int(x//pas)
	else:
		x=(x//pas)*pas+marge
		lon=int(x//pas)
	if pas/2<y%pas:
		y=(y//pas)*pas+pas+marge
		lat=int(y//pas)
	else:
		y=(y//pas)*pas+marge
		lat=int(y//pas)		
	
	
	global tour
	
	print("1:",lat)
	print("1:",lon)
	if 1<=lat<nb_case and 1<=lon<nb_case:
		if liste[lat][lon]==" ":
			alpha_lat=[-1,-1,0,1,1,1,0,-1]
			alpha_lon=[0,1,1,1,0,-1,-1,-1]
			i=0
			for direction in range (8):									
				if liste [lat+alpha_lat[direction]][lon+alpha_lon[direction]]!=" ":
					i+=1
					

					
	if i!=0 and tour.count("b")==tour.count("n"):
		liste [lat][lon]="b"
		couleur(liste,nb_case,r_pion)
		tour+=["b"]
		color="b"
		enemi="n"
		retourne_pion(liste,color,enemi,lat,lon)
		aqui_le_tour(tour,xx,yy,g_pion)
	elif i!=0 and tour.count("b")!=tour.count("n"):
		liste [lat][lon]="n"
		couleur(liste,nb_case,r_pion)
		tour+=["n"]
		color="n"
		enemi="b"
		retourne_pion(liste,color,enemi,lat,lon)
		aqui_le_tour(tour,xx,yy,g_pion)
	else:
		damier.bind("<Button-1>",centrage_pion)

	for elt in liste:
		print("".join(elt))	
def couleur(liste,nb_case,r_pion):		
	
	for lat in range(nb_case):
		for lon in range(nb_case):
			if liste[lat][lon]=="n":
				y=lat*pas+marge
				x=lon*pas+marge
				damier.create_oval(x-r_pion,y-r_pion,x+r_pion,y+r_pion,fill="black",outline="gold")
				 
			if liste[lat][lon]=="b":
				y=lat*pas+marge
				x=lon*pas+marge
				damier.create_oval(x-r_pion,y-r_pion,x+r_pion,y+r_pion,fill="white",outline="gold")
				
				
			
				

def retourne_pion(liste,color,enemi,lat,lon):
	
	print("2:",lat)
	print("2:",lon)
	print("2:",color)
	alpha_lat=[-1,-1,0,1,1,1,0,-1]
	alpha_lon=[0,1,1,1,0,-1,-1,-1]
	
	for direction in range (8):
		change=[]
		a=lat
		o=lon
		while enemi:
			
			a+=alpha_lat[direction]
			o+=alpha_lon[direction]
			if liste[a][o]==" ":
				change=[]
				break
			if liste[a][o]==color and len(change)==0:
				break
			if liste[a][o]==enemi:
				change+=[(a,o)]	
				continue
			if liste[a][o]==color and len(change)>0:
				print("change: ",change,alpha_lat[direction],alpha_lon[direction],a,o,color)
				conversion(change,color)
				break
def conversion(change,color):
	for (a,o) in change:
		liste[a][o]=color
		couleur(liste,nb_case,r_pion)
		score(liste,nb_case)
def aqui_le_tour(tour,xx,yy,g_pion):
	if len(tour)%2==0:
		qui_joue.create_oval(xx-g_pion,yy-g_pion,xx+g_pion,yy+g_pion,fill="white",outline="gold")
	elif len(tour)%2!=0:
		qui_joue.create_oval(xx-g_pion,yy-g_pion,xx+g_pion,yy+g_pion,fill="black",outline="gold")	
def score(liste,nb_case):
	tab_score.delete(ALL)
	score_noir=0
	score_blanc=0
	for ligne in range(nb_case+1):
		score_noir+=liste[ligne].count("n")
		score_blanc+=liste[ligne].count("b")
	print(score_noir)
	print(score_blanc)
	txt3=tab_score.create_text(225,20,text="TABLEAU DES SCORES",font="arial 16 italic")
	tab_score.create_oval(110-r_pion,155-r_pion,110+r_pion,155+r_pion,fill="black",outline="gold")
	tab_score.create_oval(110-r_pion,65-r_pion,110+r_pion,65+r_pion,fill="white",outline="gold")
	txt4=tab_score.create_text(200,155,text=score_noir,font="Arial 30 italic")
	txt5=tab_score.create_text(200,65,text=score_blanc,font="Arial 30 italic")
			
colonne(cote,nb_case,pas,marge)
ligne(cote,nb_case,pas,marge)

couleur(liste,nb_case,r_pion)
aqui_le_tour(tour,xx,yy,g_pion)
damier.bind("<Button-1>",centrage_pion)
	



air.mainloop()	
