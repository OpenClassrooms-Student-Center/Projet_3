import json
import random

dictionairy = {0:" ",1:"█",2:"m",3:"g",4:"N",5:"B",6:"E"} 
    #AG N = needle, B = barrel et E = ether
    #AG alt 219 makes a perfect wall for terminal use

class Layout:
    def __init__(self, configfile = 'labyrinth.json'):
        with open(configfile) as f:
            maze = json.load(f)
            self.structure = maze['labyrinth']

    def pprint(self):
        for line in self.structure:
            for char in line:
                print(dictionairy[char], end = "")
            print()#AG return to line for each completed lines

    def get_paths(self):
        paths = []
        self.valid_paths = paths
        for i, line in enumerate(self.structure):
            for j, char in enumerate(line):
                if char == 0 or char == 2: 
                #QQ est-ce que "m" doit être ajouté? /!\
                    paths.append((i, j))
                    #print((i, j))
        return paths
    
    def random_items(self):
        item_location = []
        offset = 3 #first item being number 4 in the layout 
        items = random.sample(self.valid_paths, 3)
        for i in enumerate(items):
            item_location.append(i)#QQ +offset error with tulpe
        return item_locationt
        #for each items:
            #for i = valeur x:
                #for j = valeur y:
                    #remplacer 0 par enumerate+offset
                

layout = Layout()
layout.pprint()
layout.get_paths() #print(layout.get_paths())
print(layout.random_items())
layout.pprint()
    #choix des position, nombre N => renvoi un certain nombre d'element             /!\
#############################################

    #debug
#for maze in json.load(open("labyrinth.json")):
#    a = len(maze)
#    print(a)
#    print(maze)