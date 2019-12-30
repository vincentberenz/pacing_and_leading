


class _World:

    def __init__(self):

        self.cursor = None
        self.soft_target = None
        self.hard_target = None
        


class Experiment:

    def __init__(self,
                 frequency,
                 width,
                 height,
                 background,
                 soft_target,
                 mediator,
                 hard_target,
                 cursor):

        # frequency of display update
        self.frequency = frequency
        
        # attributes of the main window
        self.width = width
        self.height = height
        self.background = background
        
        # Circle is simply an holder for position,size(radius) and color
        # + an update function
        self._soft_target = display.Circle(soft_target)
        self._hard_target = display.Circle(hard_target)
        self._mediator = display.Circle(mediator)
        self._cursor = display.Circle(cursor)

        # All circles that needs management
        self._circles = [self._soft_target,
                         self._hard_target,
                         self._mediator,
                         self._cursor]
        
    def update(self,cursor):

        # computes the attributes of all circles
        # for an iteration

        # world is the (read only) shared memory
        # providing all info required for the update
        # of each circle
        world  = _World()
        world.cursor = cursor
        world.soft_target = self._soft_target.get_position()
        world.hard_target = self._hard_target.get_position()

        # each circle calls its own update function, to
        # update position,size and color
        for circle in self._circles():
            circle.update(world)

        # returning for each circle an instance with attributes
        # position, size and color
        return [ circle.get()
                 for circle in self._circles ]
