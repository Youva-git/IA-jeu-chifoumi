#coding:utf-8
import pipes
import random
import numpy as np
import matplotlib.pyplot as plt


t = pipes.Template()
f = t.open('pipefile','w')

#retourne une list de color aleatoir de taille n et associe
#      a chaque color une strategie aleatoire dans la list_strg
alone = input("laisser la machine generer ses propres enchainement de coups [o/n]:")
alone = alone.lower()

def f_dict_color_strg(n, list_strg):
    if n > len(list_strg):
      print("ERR : le nombre de couleur et plus grand que le nombre de strategie !")
      exit()
    dict_color_strg = {}
    while len(dict_color_strg.keys()) < n:
      color = "#"+''.join([random.choice('0123456789ABCDEF') 
          for j in range(6)])
      if color not in dict_color_strg.keys():
        strg = random.choice(list_strg)
        if strg not in dict_color_strg.values():
          dict_color_strg[color] = strg
    return dict_color_strg


if(alone == "o"):
  #retourn une liste de strg aleatoir de taille n
  def f_list_strg(n):
      list_strg = []
      while len(list_strg) < n:
        strg = [''.join([random.choice('PFC') 
              for j in range(1)]) for i in range(random.randint(1, 6))]
        if strg not in list_strg :
          list_strg.append(strg)
      return list_strg

  nb_strategie = 33
  dictt = f_dict_color_strg(nb_strategie,f_list_strg(nb_strategie))
  fig = plt.figure(figsize=(12,8))
  ax = plt.subplot()
  ax.set_axis_off()

  # Set titles for the figure and the subplot respectively
  fig.suptitle('Toutes les stratégies generées', fontsize=14, fontweight='bold')

  ax.xaxis.set_visible(False)
  ax.yaxis.set_visible(False)
  fontdict = {'size': 15}

  x_offset = 0.0
  y_offset = 0.04
  for index, (cle, valeur) in enumerate(dictt.items()):
      i = index % 11
      j = index // 11
      x = x_offset + 0.4 * j
      y = y_offset + 0.09 * i
      ax.text(x , y, valeur, fontdict=fontdict, style='italic', bbox={'facecolor': cle, 'alpha': 0.7, 'pad':0.7})   
           
  plt.savefig("automatique_graphe")
  f.write(str(dictt))
  f.close
  print("les données sont bien transmise au traitement")
  print("Vous pouvez visualiser l'image des stratégie générées dans le répértoire courant")
elif(alone == 'n'):
  filin = open('mes_strategies.txt','r')
  strategies = filin.readline()
  for i in range (len(strategies)-1):
    if(strategies[i] != ' ' and strategies[i] != 'P' and strategies[i] != 'F' and strategies[i] != 'C' and strategies[i] != ','):
      exit("Erreur format!")
  lst = strategies.split(",")
  lst_strategies = []
  for i in range(len(lst)):
    lst_strategies.append(lst[i].split(" "))
  print(lst_strategies)
  dictt = f_dict_color_strg(len(lst_strategies),lst_strategies)
  fig = plt.figure()
  ax = plt.subplot()
  fig.subplots_adjust(top=0.85)

  # Set titles for the figure and the subplot respectively
  fig.suptitle('Toutes les stratégies generées', fontsize=14, fontweight='bold')
  ax.set_title('axes title')


  fontdict = {'size': 10}

  x_offset = 0.05
  y_offset = 0.03
  for index, (cle, valeur) in enumerate(dictt.items()):
      i = index % 11
      j = index // 11
      x = x_offset + 0.4 * j
      y = y_offset + 0.09 * i
      ax.text(x , y, valeur, fontdict=fontdict, style='italic', bbox={'facecolor': cle, 'alpha': 0.7, 'pad':0.7})   
         
  
  plt.savefig("notre_graphe")
  f.write(str(dictt))
  f.close
  print("les données sont bien transmise au traitement")
  print("Vous pouvez visualiser l'image des stratégie générées dans le répértoire courant")
else:
  print("Erreur!: réassayer")
  alone = input("laisser la machine generer ses propres enchainement de coups [o/n]:")
  alone = alone.lower()

