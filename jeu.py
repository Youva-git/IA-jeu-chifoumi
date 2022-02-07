from random import randint
from tkinter import *
import pipes
import random
from tkinter import messagebox
from numpy.core.numeric import True_

# variables globales
a = open('pipe_strg_gagnante').read()
ton_score = 0
mon_score = 0
rang_strg = 0
mes_coups = []

def affecte_strategie(var1,var2,var3):
    if(var2.get() == 1 ) :
        return extract_coup(list(a))
    if(var3.get() == 1):
        return raisonnement_humain()
    if(var1.get() == 1):
        res = []
        coups = ['P','F','C']
        for i in range(1):
            coup = random.choice(coups)
            res.append(coup)
        return res

# extract_coup prend en parametre une liste de caracteres et renvoi 
# une liste de coup
def extract_coup(list):
    res = []
    for i in range(len(list)):
        if list[i] == 'P' or list[i] == 'F' or list[i] == 'C' :
            res.append(list[i])
    return res


def augmenter_scores(mon_coup,ton_coup):
    global mon_score, ton_score, rang_strg, etat
    rang_strg += 1
    if mon_coup == 'P' and ton_coup == 'F' or mon_coup == 'F' and ton_coup == 'C' or mon_coup == 'C' and ton_coup == 'P':
        ton_score += 1
        etat = False  
    if mon_coup == 'F' and ton_coup == 'P' or mon_coup == 'C' and ton_coup == 'F' or mon_coup == 'P' and ton_coup == 'C':
        mon_score += 1
        etat = True  

def jouer(ton_coup,strg):
    global mon_score, ton_score, score1, score2, rang_strg, etat
    if( var1.get() == 1 and var2.get() ==1 or var1.get() ==1 and var3.get() ==1 or var2.get() ==1 and var3.get() ==1):
        messagebox.showerror("Erreur","Choisir une seule strategie")
    elif (var1.get() == 0 and var2.get() == 0 and var3.get() == 0):
        messagebox.showerror("Erreur","Choisir une strategie au minimum")
    else:
        strg = affecte_strategie(var1,var2,var3)
        if(rang_strg >= len(strg)):
            rang_strg = 0
        mon_coup = strg[rang_strg]
        mes_coups.append(mon_coup)
        
        print("la stratégie utilisé par la machine => "+format(strg))
        if mon_coup=='P':
            lab3.configure(image=pierre)
        elif mon_coup=='F':
            lab3.configure(image=papier)
        else:
            lab3.configure(image=ciseaux)    
        augmenter_scores(mon_coup,ton_coup)
        score1.configure(text=str(ton_score))
        score2.configure(text=str(mon_score))
    

def jouer_pierre():
        jouer('P',strg)
        lab1.configure(image=pierre)
    
def jouer_papier():
        jouer('F',strg)
        lab1.configure(image=papier)

def jouer_ciseaux():
        jouer('C',strg)
        lab1.configure(image=ciseaux)

def reinit():
    global mon_score,ton_score,score1,score2,lab1,lab3,rang_strg
    ton_score = 0
    mon_score = 0
    rang_strg = 0
    score1.configure(text=str(ton_score))
    score2.configure(text=str(mon_score))
    lab1.configure(image=rien)
    lab3.configure(image=rien)

def raisonnement_humain():
    global strg, etat, mes_coups
    len_mes_coups = len(mes_coups)
    coups = ['P','F','C']
    if(len_mes_coups == 0):
        strg = ['P']
    else:
        if(etat == True):
            strg = [mes_coups[len_mes_coups-1]]
        else:
            c = random.choice(coups)
            while(c == mes_coups[len_mes_coups-1]):
                c =  random.choice(coups)
            strg = [c]
    return strg

# fenetre graphique
fenetre = Tk()
fenetre.title("Pierre, papier, ciseaux")

#images
rien = PhotoImage(file ='rien.gif')
versus = PhotoImage(file ='versus.gif')
pierre = PhotoImage(file ='pierre.gif')
papier = PhotoImage(file ='papier.gif')
ciseaux = PhotoImage(file ='ciseaux.gif')


# Label
texte1 = Label(fenetre, text="Humain :", font=("Helvetica", 16))
texte1.grid(row=0,column=0)

texte2 = Label(fenetre, text="Machine :", font=("Helvetica", 16))
texte2.grid(row=0,column=2)

texte3 = Label(fenetre, text="Pour jouer, cliquez sur une des icones ci-dessous.")
texte3.grid(row=3, columnspan =3, pady =5)

score1 = Label(fenetre, text="0", font=("Helvetica", 16))
score1.grid(row=1, column=0)    

score2 = Label(fenetre, text="0", font=("Helvetica", 16))        
score2.grid(row=1, column=2)      

lab1 = Label(fenetre, image=rien)
lab1.grid(row =2, column =0)

lab2 = Label(fenetre, image=versus)
lab2.grid(row =2, column =1)

lab3 = Label(fenetre, image=rien)
lab3.grid(row =2, column =2)

lab4 = Label(fenetre, text="Choisir une stratégie avant de jouer", font=("Helvetica", 14))
lab4.grid(row=6, columnspan =3, pady =5)

# boutons
bouton1 = Button(fenetre,command=jouer_pierre)
bouton1.configure(image=pierre)
bouton1.grid(row =4, column =0)

bouton2 = Button(fenetre,command=jouer_papier)
bouton2.configure(image=papier)
bouton2.grid(row =4, column =1,)

bouton3 = Button(fenetre,command=jouer_ciseaux)
bouton3.configure(image=ciseaux)
bouton3.grid(row =4, column =2)

bouton4 = Button(fenetre,text='Recommencer',command=reinit)
bouton4.grid(row =5, column =0, pady =10, sticky=E)

bouton5 = Button(fenetre,text='Quitter',command=fenetre.destroy)
bouton5.grid(row =5, column =2, pady =10, sticky=W)


#chekbox
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

var1.set(1)


alea = Checkbutton(fenetre,text = "aleatoire", variable= var1)
alea.grid(row =7, column =0, pady =10, sticky=W)

traitee = Checkbutton(fenetre,text = "traitement", variable= var2)
traitee.grid(row =7, column =1, pady =10, sticky=W)

humain = Checkbutton(fenetre,text = "humain", variable= var3)
humain.grid(row =7, column =2, pady =10, sticky=W)


strg = affecte_strategie(var1,var2,var3)
etat = True
# demarrage :
fenetre.mainloop()