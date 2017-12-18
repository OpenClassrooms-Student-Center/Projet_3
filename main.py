import json

class map:

    MAP = []
    X_MIN = 0
    X_TOP = 15
    Y_MIN  = 0
    Y_TOP = 15
    # define current position
    pass

class start_point:
    pass
    # set to id 2
    # position X = 11
    #          Y = 1

class path:

    @property
    def is_target_area_valid(self):
        pass
        #if path near/target player =! 1, movable, else can't move there

    @property
    def guardian(self):
        ''' guardian is a path (9) because he is not moving and a win condition
        could also be an item which kills you if you don't have a full list '''
        if list.player_items == [1,2,3]:
            # something like that
            pass
            # win condition
        else:
            pass
            # game over 

class list_of_valid_path:
    VALID_PATH = []
    # tulpe?
    # set with X and Y coordinates
    # ou invalid path? Wall = item not pickable, not path

class items:
    pass
    # add 1st item at random on area that is set to "0"
    # add 2nd item at random on area that is set to "0", not on 1st item
    # add 3rd item at random on area that id set to "0", not on 1st or 2nd item

    # place randomly 3 items, ID 3, 4 & 5
    # player should be an item? Special item?
    # item as subpart of path?

class player_moves:
    pass
    # if pressed key == "left arrow" or "q"
    #    try move left using "def is_target_area_valid"
    #        self.position X -1, Y +0
    #    else invalid move
    # if pressed key == "right arrow" or "d"
    #    try move right using "def is_target_area_valid"
    #        self.position X +1, Y +0
    #    else invalid move
    # if pressed key == "up arrow" or "z"
    #    try move up using "def is_target_area_valid"
    #        self.position X +0, Y +1
    #    else invalid move
    # if pressed key == "down arrow" or "s"
    #    try move down using "def is_target_area_valid"
    #        self.position X +0, Y -1
    #    else invalid move 

def main():
    for labyrinth in json.load(open("labyrinth.json")):
        pass

main()