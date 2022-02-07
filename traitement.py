  #coding:utf-8
import networkx as nx
import numpy as np
import random
import time
import matplotlib.pyplot as plt
from math import *
import math 
import pandas
from matplotlib.table import Table
import pipes
from tkinter import messagebox
#import seaborn.apionly as sns
import matplotlib.animation
from fonction import*

if __name__ == '__main__':
    s = input("Entrer le nombre de joueurs ")
    z = input("Entrez sur quelle forme de graphe vous voulez visuliser l'evolustion du jeu:\n   1 pour complet\n   2 pour grille\n   3 pour circulaire\n   ==>")
    myPipe = open('pipefile').read()
    nb_nodes = int(s)
    G = nx.Graph()
    nb_strg = 30
    couleur = extract_color(myPipe)
    coups = extract_coup(myPipe)
    # generer une liste de strategir aleatoire
    list_color_strg = init_str(coups,couleur)

    # generer une liste de color aleatoire et associé a chaque color 
    # une strategir de jeu

    G.add_edges_from(graph_nodes(nb_nodes))
    pos = nx.circular_layout(G)

    # associé a chaque node du graphe G une color aleatoire
    strg_nodes = color_strg_nodes_func(G, list(list_color_strg.keys()))

    # associé a chaque node du graphe G une startegie en fonction de sa couleur
    init_strg_nodes = init_strg_nodes_func(G, strg_nodes, list_color_strg)

    strategies_points = {k:0 for k in strg_nodes.values()}
    def care(nb):
      rc = math.sqrt(nb)
      rcf = math.ceil(rc)
      return rcf

    keys = list(strg_nodes.keys())
    values = list(strg_nodes.values())
    taille = care(len(keys))

    def lists_to_tuples():
      l_tuples = []
      for i in range(0,len(keys)):
        l_tuples.append((keys[i],values[i]))
      return l_tuples

    lists = lists_to_tuples()
    def liste_complition():
      for i in range(len(lists),(taille * taille)+1):
        lists.append((str(i),'white'))

    liste_complition()
    x,y=0,0
    liste_of_liste = []
    liste_of_liste0 = []
    for i in range(len(lists)):
      liste_of_liste0.append(lists[i])
      x +=1
      if(x == taille):
        liste_of_liste.append(liste_of_liste0)
        liste_of_liste0 = []
        y+=1
        x = 0
    if(x < taille  and y < taille ):
      liste_of_liste.append(liste_of_liste0)
    dict_affiche = {}
    dict_node_coords = dict_indexing(G,taille)
    for i in range(1, len(G) + 1):
      dict_affiche[strg_nodes.get(str(i))] = list_color_strg.get(strg_nodes.get(str(i)))
    
    arret = {'fin' : False}

    def update(num):
        axs[0, 0].clear()
        axs[0, 1].clear()
        axs[1, 0].clear()
        axs[1, 1].clear()
        axs[0, 1].axes.xaxis.set_visible(False)
        axs[1, 0].axes.xaxis.set_visible(False)
        axs[1, 0].axes.yaxis.set_visible(False)
        axs[1, 1].axes.xaxis.set_visible(False)
        axs[1, 1].axes.yaxis.set_visible(False)
        axs[1,0].set_axis_off()
        fin = False
        node1 = np.random.choice(G.nodes())
        node2 = np.random.choice(calc_voisins(G,node1, taille,z,dict_node_coords,strg_nodes))
        coup_node1 = etiquettes_nodes(strg_nodes, init_strg_nodes).get(node1)
        coup_node2 = etiquettes_nodes(strg_nodes, init_strg_nodes).get(node2)
        
        while strg_nodes.get(node1) == strg_nodes.get(node2):
           node1 = np.random.choice(G.nodes())
           node2 = np.random.choice(calc_voisins(G,node1, taille,z,dict_node_coords,strg_nodes))
           coup_node1 = etiquettes_nodes(strg_nodes, init_strg_nodes).get(node1)
           coup_node2 = etiquettes_nodes(strg_nodes, init_strg_nodes).get(node2)
           if all(x ==list(strg_nodes.values())[0] for x in list(strg_nodes.values())):
              fin = True
              break
        
        if fin == True:
          strg_gg = list_color_strg.get(strg_nodes.get('1'))
          t = pipes.Template()
          f = t.open('pipe_strg_gagnante','w')
          f.write(str(strg_gg))
          f.close
          axs[1,0].add_table(tb)

          if(arret.get('fin') == True):
            messagebox.showerror("fin:","La strategie gagnate est: \n" + str(strg_gg))
            _ = input("Press [enter] to exit.")
            exit()
          list_players_nodes = []
          nx.draw(G, pos, 
              edgelist = list_players_nodes,
              edge_color = 'black',
              labels = etiquettes_nodes(strg_nodes, init_strg_nodes), 
              node_color = strg_nodes.values(),
              ax=axs[0, 0]
          )
          arret.update({'fin': True})
          nb_coups = sum(strategies_points.values())
          x_offset = 0.05
          y_offset = 0.15
          for index, (cle, valeur) in enumerate(strategies_points.items()):
            i = index % 7
            j = index // 7
            x = x_offset + 0.13 * i
            y = y_offset + 0.18 * j
            pvaleur = ((valeur * 100) / nb_coups)
        else:
          list_players_nodes = [(node1, node2)]
          nx.draw(G, pos, 
              edgelist = list_players_nodes,
              edge_color = 'black',
              labels = etiquettes_nodes(strg_nodes, init_strg_nodes), 
              node_color = strg_nodes.values(),
              ax=axs[0, 0]
          )
          if coup_node1 ==  coup_node2:
              a1, b1 = init_strg_nodes.get(node1)
              if a1 < len(b1):
                  a1 += 1
              if a1  == len(b1):
                  a1 = 0
              color = strg_nodes.get(node1)
              x,y = dict_node_coords.get(node1)
              tb.add_cell(x, y, width, height,edgecolor='none', loc='center', facecolor=color)
              axs[1,0].add_table(tb)   
              init_strg_nodes.update({node1: (a1, b1)})
          
          a2, b2 = init_strg_nodes.get(node2)
          if a2  < len(b2):
              a2 += 1
          if a2  == len(b2):
              a2 = 0
          color = strg_nodes.get(node1)
          x,y = dict_node_coords.get(node1)
          tb.add_cell(x, y, width, height,edgecolor='none', loc='center', facecolor=color)
          axs[1,0].add_table(tb)   
          init_strg_nodes.update({node2: (a2, b2)})

          # si noeud 2 gagne
          if (coup_node1 == 'P' and coup_node2 == 'C') or (coup_node1 == 'C' and coup_node2 == 'F') or (coup_node1 == 'F' and coup_node2 == 'P'): 
              strategies_points[strg_nodes.get(node1)] += 1
              color = strg_nodes.get(node1)
              x,y = dict_node_coords.get(node2)
              tb.add_cell(x, y, width, height,edgecolor='none', loc='center', facecolor=color)
              axs[1,0].add_table(tb)
              strg_nodes.update({node2: strg_nodes.get(node1)})
              a, b = init_strg_nodes.get(node1)
              if a + 1 <= len(b):
                  a += 1
              if a == len(b):
                 a = 0
                 
              init_strg_nodes.update({node1: (a, b)})
              init_strg_nodes.update({node2: (0, b)})
              
          # Si noeud 1 gagne
          if (coup_node1 == 'C' and coup_node2 == 'P') or (coup_node1 == 'F' and coup_node2 == 'C') or (coup_node1 == 'P' and coup_node2 == 'F'):
              strategies_points[strg_nodes.get(node2)] += 1
              color = strg_nodes.get(node2)
              x,y = dict_node_coords.get(node1)
              tb.add_cell(x, y, width, height,edgecolor='none', loc='center', facecolor=color)
              axs[1,0].add_table(tb)  
              strg_nodes.update({node1: strg_nodes.get(node2)})
              a, b = init_strg_nodes.get(node2)
              if a + 1 <= len(b):
                  a += 1
              if a == len(b):
                  a = 0  

              init_strg_nodes.update({node2: (a, b)})
              init_strg_nodes.update({node1: (0, b)})

        barlist = axs[0, 1].bar(list(range(len(strategies_points))), strategies_points.values())
        for i, color in enumerate(strategies_points.keys()):
            barlist[i].set_color(color)
        
        fontdict = {'size': 10}

        x_offset = 0.05
        y_offset = 0.03
        for index, (cle, valeur) in enumerate(dict_affiche.items()):
          i = index % 11
          j = index // 11
          x = x_offset + 0.4 * j
          y = y_offset + 0.09 * i
          axs[1, 1].text(x , y, valeur, fontdict=fontdict, style='italic', bbox={'facecolor': cle, 'alpha': 0.7, 'pad':0.7})   
         
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(12,8))
    
    tb = Table(axs[1,0])
    data = pandas.DataFrame(liste_of_liste)
   

    nrows, ncols = data.shape
    width, height = 1.0 / ncols, 1.0 / nrows
    for(i,j), val in np.ndenumerate(data):
        c = liste_of_liste[i][j]
        n,cc = c
        tb.add_cell(i, j, width, height,edgecolor='none', loc='center', facecolor=cc)
     
    axs[1,0].add_table(tb)
    ani = matplotlib.animation.FuncAnimation(fig, update, frames=6, interval=5, repeat=True)
    plt.show() 
    