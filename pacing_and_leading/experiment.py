from . import display
from . import geometry

class _World:

    def __init__(self):

        self.cursor = None
        self.soft_target = None
        self.hard_target = None
        self.similarity = None
        self.vertical_targets = []
        self.arrows = []
        
class Experiment:

    def __init__(self,
                 frequency,
                 width,
                 height,
                 background,
                 similarity,
                 soft_target,
                 mediator,
                 hard_target,
                 cursor,
                 vertical_targets,
                 arrows,
                 data_file):

        # frequency of display update
        self.frequency = frequency
        
        # attributes of the main window
        self.width = width
        self.height = height
        self.background = background

        # how much is the user motion (i.e. motion of the cursor)
        # similar to the hard target motion ?
        # should return a score between 0 (dissimilar) and 1 (identical)
        self._similarity = similarity
        
        # Circle is simply an holder for position,size(radius) and color
        # + an update function
        self._soft_target = display.Circle("soft_target",soft_target)
        self._hard_target = display.Circle("hard_target",hard_target)
        self._mediator = display.Circle("mediator",mediator)
        self._cursor = display.Circle("cursor",cursor)
        
        # All circles that needs management
        self._circles = [self._hard_target,
                         self._soft_target,
                         self._mediator,
                         self._cursor]
        
        # if target bars are to be used, adding them.
        # All parameters currently hard coded here
        if vertical_targets:
            self._vertical_target_left = display.VerticalLine("vertical_target_left",
                                                              vertical_targets[0])

            self._vertical_target_right = display.VerticalLine("vertical_target_right",
                                                              vertical_targets[1])
            self._vertical_bars = [self._vertical_target_left,
                                   self._vertical_target_right]

        else :
            self._vertical_bars = []

        if arrows:

            self._arrows = [ display.Arrow("arrow_"+str(index),
                                           arrow.length,
                                           arrow.width,
                                           arrow.tip_size,
                                           arrow)
                             for index,arrow in enumerate(arrows) ]

        else :

            self._arrows = []
        
        # for logging on exit
        self._similarities = []
        self._distances = []
        self._data_file = data_file
        
        
    def update(self,cursor):

        # computes the attributes of all circles
        # for an iteration

        # world is the (read only) shared memory
        # providing all info required for the update
        # of each circle and each vertical target (if any)
        world  = _World()
        world.cursor = cursor
        world.soft_target = self._soft_target.get_position()
        world.hard_target = self._hard_target.get_position()
        world.similarity = self._similarity(world.cursor,
                                            world.hard_target)
        world.vertical_targets = [vb.get_source()
                                 for vb in self._vertical_bars]
        
        # for plotting on exit
        self._similarities.append(world.similarity)
        if world.cursor is not None and world.hard_target is not None:
            self._distances.append(geometry.distance(world.cursor,
                                                     world.hard_target))
        
        # each circle calls its own update function, to
        # update position,size and color
        list ( map(lambda c: c.update(world), self._circles) )

        # each vertical target calls its own update function
        # as well
        list ( map(lambda vb: vb.update(world), self._vertical_bars) )

        # same for arrows
        list ( map(lambda a: a.update(world), self._arrows) )
        
        # returning for each circle/vertical bar an instance with attributes
        # position, size and color
        return [ circle.get()
                 for circle
                 in self._circles ], [vb.get()
                                      for vb
                                      in self._vertical_bars] , [a.get()
                                                                 for a
                                                                 in self._arrows]


    
    def save(self):

        print("saving results in",self._data_file)
        
        similarities = [s for s in self._similarities
                        if s is not None]

        with open(self._data_file,"w+") as f:
            f.write(repr(similarities))
            f.write('\n')
            f.write(repr(self._distances))
            
    @classmethod
    def plot_results(self,data_file):

        with open(data_file,"r") as f:
            data = f.read()

        similarities,distances = data.split('\n')
            
        similarities = eval(similarities)
        distances = eval(distances)

        import matplotlib.pyplot as plt

        x = range(len(similarities))
        y = similarities

        plt.scatter(x,y)
        plt.title("similarities")
        plt.show()

        x = range(len(distances))
        y = distances

        plt.scatter(x,y)
        plt.title("distances")
        plt.show()

        
