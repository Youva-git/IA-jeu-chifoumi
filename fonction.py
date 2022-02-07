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

#import seaborn.apionly as sns
import matplotlib.animation

#return la liste de toutes les aretes du graphe
def graph_nodes(nb_nodes):
    list_nodes_graph = []
    for i in range(1, nb_nodes):
        list_nodes_graph.append((str(i),str(i + 1)))
    list_nodes_graph.append((str(nb_nodes),str(1))) 
    return list_nodes_graph 

#return un dictionnair qui affect comme valeur 
#       une couleur aleatoir pour chaque noeud
def color_strg_nodes_func(G, list_strg):
    strg_node = {}
    for i in range(1, len(G)  + 1):
        strg_node[str(i)] = random.choice(list_strg)
    return strg_node     

# return un dictionnair qui affect comme valeur une stratégie 
#       pour chaque noeud en fonction de sa couleur 
def init_strg_nodes_func(G, node_color_strg, list_color_strg):
    etiquettes_nodes = {}
    for i in range(1, len(G) + 1):
      etiquettes_nodes[str(i)] = (0, list_color_strg.get(node_color_strg.get(str(i))))
    return etiquettes_nodes

#return un dictionnair qui affect comme valeur le coup a joué
#       pour chaque noeud  
def etiquettes_nodes(G, init_strg_nodes):
    etiquettes_nodes = {}
    for i in range(1, len(G) + 1):
      a, b = init_strg_nodes.get(str(i))
      etiquette = b[a]
      etiquettes_nodes[str(i)] = etiquette
    return etiquettes_nodes
    
#return une list de color aleatoir de taille n et associe
#      a chaque color une strategie aleatoire dans la list_strg
def f_dict_color_strg(list_strg):
    dict_color_strg = {}
    while  len(dict_color_strg.keys()) < len(list_strg):
      color = "#"+''.join([random.choice('0123456789ABCDEF') 
          for j in range(6)])
      if color not in dict_color_strg.keys():
        strg = random.choice(list_strg)
        if strg not in dict_color_strg.values():
          dict_color_strg[color] = strg
          
    return dict_color_strg

#return une list de strg aleatoir de taille n
def f_list_strg(n):
    list_strg = []
    while len(list_strg) < n:
     strg = [''.join([random.choice('PFC') 
          for j in range(1)]) for i in range(random.randint(1, 6))]
     if strg not in list_strg :
      list_strg.append(strg)
    return list_strg
    
# return la list des voisins du node qui sont dans le Graphe
def voisins_nodes(G, node):
    voisins_nodes = []
    for v in G[node]:
      voisins_nodes.append(v)
    return voisins_nodes 


def calc(taille,nb):
      x,y =0,0  
      for i in range(1,nb):
        x +=1
        if(x == taille):
          y+=1
          x = 0
      return y,x

def dict_indexing(G,taille):
  node_coords = {} 
  for i in range(1,len(G) + 1):
    x,y = calc(taille,i)
    node_coords[str(i)] = (x,y)
  return node_coords

#extract_coup(chaine) : RENVOI LA LISTE DES STRATEGIE
def extract_coup(chaine):
    res = []
    aux = []
    for i in range(len(chaine)):
        if(chaine[i] == '['):
            while(chaine[i] != ']'):
                if(chaine[i] == 'P' or chaine[i] == 'F' or chaine[i] == 'C' ):
                    aux.append(chaine[i])
                i = i +1 
        if(aux != []):
            res.append(aux)
        aux = []
    return res

#extract_string_color(chaine) : extrait les couleur a partir de la chaine de caractere et les stock dans une liste
def extract_color(chaine):
    res = []
    aux = ''
    for i in range(len(chaine)):
        if(chaine[i] == '#'):
             while(chaine[i] != '\''):
                aux = aux + chaine[i]
                i = i +1 
        if(aux != ''):
            res.append(str(aux))
        aux = ''
    return res
    
def init_str(list, list1):
    dec = {}
    for i in range(len(list1)):
        dec[str(list1[i])] = list[i]
    return dec


def calc_voisins(G,node,taille,form,dict_node_coords,strg_nodes):
  if form == '1':
    return [np.random.choice(G.nodes())]
  elif form == '2':
    list_coord_voisins = []
    list_node_voisins = []
    a,b = dict_node_coords.get(str(len(strg_nodes)))
    x,y = dict_node_coords.get(str(node)) 
    x1,y1 = x-1, y-1
    list_coord_voisins.append((x1,y1))
    x2,y2 = x, y-1
    list_coord_voisins.append((x2,y2))
    x3,y3 = x+1, y-1
    list_coord_voisins.append((x3,y3))
    x4,y4 = x-1, y
    list_coord_voisins.append((x4,y4))
    x5,y5 = x+1, y
    list_coord_voisins.append((x5,y5))
    x6,y6 = x-1, y+1
    list_coord_voisins.append((x6,y6))
    x7,y7 = x, y+1
    list_coord_voisins.append((x7,y7))
    x8,y8 = x+1,y+1
    list_coord_voisins.append((x8,y8))
    for i in range(0,len(list_coord_voisins)):
      x,y = list_coord_voisins[i]
      if x < 0 or x >= taille or y < 0 or y >= taille or x > a or y > b :
        pass
      else:
        list_node_voisins.append(list(dict_node_coords.keys())[(list(dict_node_coords.values())).index((x,y))])
    return list_node_voisins
  elif form == '3':
    if int(node) - 1 < 1:
      return [str(int(node) +1)]
    elif int(node) + 1 > len(dict_node_coords):
      return [str(int(node)-1)]
    else:  
      return [str(int(node)-1),str(int(node)+1)]
