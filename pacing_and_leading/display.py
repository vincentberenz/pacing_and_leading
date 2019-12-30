import copy


class _Circle:

    def __init__(self,position,size,color):
        self.position = copy.deepcopy(position)
        self.size = copy.deepcopy(size)
        self.color = copy.deepcopy(color)


class Circle :

    """ generic class for all moving circles in the world
        
    Args:      
    update_function : compute the position, size and color
    of the circle depending of the current state of the world,
    e.g. position of the user's cursor
    """
    
    def __init__(self,update_function):

        self._position = None
        self._size = None 
        self._color = None # None means transparent
        self._update_function = update_function

    def get_position(self):
        
        return copy.deepcopy(self._position)

    def get(self):

        return _Circle(self._position,
                       self._size,
                       self._color)
    
    def update(self,world):

        self._position,self._size,self._color = self._update_function(world)
    


