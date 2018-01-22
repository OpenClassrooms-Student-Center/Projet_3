import json

dictionaire = {1:"█",0:" ",2:"m",9:"g",3:"A",4:"T",5:"E"} 
    #A = aiguille, T = tube et E = ether
    # alt 219 makes a perfect wall for terminal use

class Layout:
    def __init__(self, configfile = 'labyrinth.json'):
        with open(configfile) as f:
            maze = json.load(f)
            self.structure = maze['labyrinth']

            # for each position valide (cf liste vide remplie):
                # item = 3
                # for x in range(0, 3):
                    # replace a 0 by item += 1
                    # comme ça  les 3 item ont une ID différente
                    # 

    def pprint(self):
        for line in self.structure:
            for char in line:
                print(dictionaire[char], end = "")
            print()#AG return to line for each completed lines
    #def get_paths(self): #QQ pourquoi ne marche-il pas avec cette ligne?
        paths = []
        self.valid_paths = paths
        for i, line in enumerate(self.structure):
            for j, char in enumerate(line):
                if char == 0: 
                #QQ est-ce que "m" et "g" doivent être dans le paths valide?
                    paths.append((i, j))
                    #print((i, j))
        print(paths)
    

    def random_items():
        for path in self.valid_paths:
            for self.valid_paths in range(0,3):
                

        #charger les paths valides
        #lire liste
        #creer copie de liste -- check avec self.valid_paths?
        #in range (0,3)
            #x=3
            #si items dans liste_copié:
                #pop toute les entrées qui ont le même i ou j
                #set random location to x
                #x =+ 1 #QQ estce qu'on peux utiliser enumerate pour partir de plus que 0?
        pass

Layout().pprint() 
    #choix des position, nombre N => renvoi un certain nombre d'element             /!\

#############################################

    #debug
#for maze in json.load(open("labyrinth.json")):
#    a = len(maze)
#    print(a)
#    print(maze)