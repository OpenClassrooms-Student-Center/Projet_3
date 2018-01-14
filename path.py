class Path:

#    @property
#    def is_target_area_valid(self):
#        pass
        # if path near/target player =! 1, movable, else can't move there

    @property
    def guardian(self):
        '''guardian is a path (9) because he is not moving and a win condition
        could also be an item which kills you if you don't have a full list '''
        if list.player_items == [1,2,3]:
            # something like that
            pass
            # win condition
        else:
            pass
            # game over 