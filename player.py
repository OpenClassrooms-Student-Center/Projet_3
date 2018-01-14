class Player:
    pass
    #attribut self.pos => position
    #methode move pour le déplacer
    #mouvement par texte move("r"),move("l")...


    # /!\ def is_wall(x,y) => is true, nothing/false do

        # if keypress == "left arrow" or "q"
        #    try move left using "def is_target_area_valid"
        #        self.position X -1, Y +0
        #    else invalid move
        # if keypress == "right arrow" or "d"
        #    try move right using "def is_target_area_valid"
        #        self.position X +1, Y +0
        #    else invalid move
        # if keypress == "up arrow" or "z"
        #    try move up using "def is_target_area_valid"
        #        self.position X +0, Y +1
        #    else invalid move
        # if keypress == "down arrow" or "s"
        #    try move down using "def is_target_area_valid"
        #        self.position X +0, Y -1
        #    else invalid move 