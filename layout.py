import json

class Layout:
    def __init__(self):
        with open('labyrinth.json') as f:
        #with open(configfile) as f: #(configfile being launcher.py) --- pas réussi à faire marcher avec le 2e arg ,configfile
            maze = json.load(f)
            self.structure = maze['labyrinth']
            y = len(maze['labyrinth'])
            #print(self.structure, y)

    #X_MIN = 0
    #X_TOP = 14
    #Y_MIN  = 0
    #Y_TOP = 14
#utiliser instance de Position pour les positions

    #utiliser self.structure et len() pour avoir des longueurs varaibles
    #metode get_valid_path qui parcoure self.structure, a chaque 0, ajoute la pos et la renvoie
    #if chaque ligne:
    #if chaque colonne:
        #lister les 0 et retourner liste              /!\
    #choix des position, nombre N => renvoi un certain nombre d'element             /!\

#############################################

    #debug
#for maze in json.load(open("labyrinth.json")):
#    a = len(maze)
#    print(a)
#    print(maze)