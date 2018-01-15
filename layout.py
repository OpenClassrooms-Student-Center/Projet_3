import json

class Layout:
    def __init__(self):
        with open('labyrinth.json') as f:
        #with open(configfile) as f: #(configfile being launcher.py) --- pas réussi à faire marcher avec le 2e arg (self, configfile)
            maze = json.load(f)
            self.structure = maze['labyrinth']
            # je ne sais pas comment acceder a l'intérieur de la liste de liste pour X
            y = len(maze['labyrinth'])
            print(self.structure, y)
            
            # pour print les 0
            # for each 0 in maze['labyrinth']:
                # print position [x,y] in liste vide

            # for each position valide (cf liste vide remplie):
                # item = 3
                # for x in range(0, 3):
                    # replace a 0 by item += 1
                    # comme ça  les 3 item ont une ID différente
                    # 
Layout()

    #X_MIN = 0
    #X_TOP = 14
    #Y_MIN  = 0
    #Y_TOP = 14
#utiliser instance de Position pour les positions

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