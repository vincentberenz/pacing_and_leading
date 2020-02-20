import copy


class _Circle:

    def __init__(self,name,position,size,color):
        self.name = name
        self.position = copy.deepcopy(position)
        self.size = copy.deepcopy(size)
        self.color = copy.deepcopy(color)

    def __str__(self):
        return str(self.name)+"\t"+str(self.position)
        

class _VerticalLine(_Circle):

    def __init__(self,name,position,size,color):

        _Circle.__init__(name,position,size,color)


class Circle :

    """ generic class for all moving circles in the world
        
    Args:      
    update_function : compute the position, size and color
    of the circle depending of the current state of the world,
    e.g. position of the user's cursor
    """
    
    def __init__(self,
                 name,
                 update_function,
                 init_position=[0,0]):

        self._name = name
        self._position = init_position
        self._size = None 
        self._color = None # None means transparent
        self._update_function = update_function

    def __str__(self):
        return str(self._name)+":\t"+str(self._position)
        
    def get_position(self):
        
        return copy.deepcopy(self._position)

    def get(self):

        return _Circle(self._name,
                       self._position,
                       self._size,
                       self._color)
    
    def update(self,world):

        self._position,self._size,self._color = self._update_function(world)
    

class VerticalLine(Circle) :

    """ generic class for all moving circles in the world
        
    Args:      
    update_function : compute the position, size and color
    of the circle depending of the current state of the world,
    e.g. position of the user's cursor
    """
    
    def __init__(self,
                 name,
                 vertical_target,
                 init_position=[0,0]):

        Circle.__init__(self,
                        name,
                        vertical_target,
                        vertical_target.get_position())
        self._vertical_target = vertical_target
        
    def get_source(self):
        
        return self._vertical_target
        
    def update(self,world):

        self._position,self._size,self._color = self._update_function(world)
