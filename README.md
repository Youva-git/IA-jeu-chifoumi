1. simulteur du jeu Chifoumi (Pierre-feuille-ciseaux). avec trois manières différentes qui sont, le raisonnement aléatoire, le raisonnement humain et une confrontation de différentes suites de coups dans le but d’obtenir la suite la plus avantageuse.  
2. Interface utilisateur pour jouer contre le programme en laissant le choix du raisonnement (humain, aléatoire, traitement) à l’utilisateur.  
  
## Démo:  
  
<img src="https://github.com/Youva-git/demos/blob/master/IA.gif">  
  
## Manuel d'utilisation:  
  
1. Installer les Requirements.  
* Python==3.6.9  
* cycler==0.10.0  
* decorator==4.4.2  
* engineering-notation==0.6.0  
* kiwisolver==1.3.1  
* matplotlib==3.3.4  
* networkx==2.5.1  
* numpy==1.19.5  
* pandas==1.1.5  
* Pillow==8.2.0  
* pkg-resources==0.0.0  
* pyparsing==2.4.7  
* python-dateutil==2.8.1  
* pytz==2021.1  
* six==1.16.0  
* tk-tools==0.14.0  
  
2. Exécuter la commande : python3 server.py  
Suite a cela il vous sera demandé sois de choisir de laisser la machine générer les stratégies qui seront utilisé
dans le traitement ou bien d’introduire vos propres stratégies.  

* Cas ou vous avez choisez de laisser la machine générer ses propres suites de coups: dans ce cas,
la machine génère des suites de coups et associe a chaque suite une couleur unique, et ces données
seront transmise au programme de traitement.  
* Cas ou vous avez choisez d’introduire vous même les suites de coups: dans ce cas vous devez
alors remplir en amant le fichier texte «mes_strategies.txt» en respectant le format suivant:  
  * les coups sont séparer par des espaces  
  * les listes de coup par des virgules  
  
3. Exécuter la commande : python3 traitement.py.  
  
4. Exécuter la commande : python3 jeu.py  
  
