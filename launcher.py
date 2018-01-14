import json

import item
import layout
import path
import player
import position
#import list_of_valid_path --only if I can't implement it another way--

def main():
    for labyrinth in json.load(open("labyrinth.json")):
        with open('labyrinth.json') as f:
            maze = json.load(f)
            # read list = laby dans json 
# print(maze)
main()
 

#### Notes perso / Memo ####
# pour soutenance, voir les amélio possibles et comment les implémenter
# voir classes qui comuniquent ensemble
# voir modèle obj qui se raconte bien en langage de tt les jours
# poser les bonnes questions aux fct et classes
# essayer de modifier en interne
# dictionaire de traduction pour modifier le laby
# spirte size is to be defined ex:(40px)