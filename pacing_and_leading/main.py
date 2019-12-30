from .gui import PacingAndLeading
from .mediators import *
from .hard_targets import *
from .soft_targets import *
from .cursors import *
from .experiment import Experiment


USER_ID = 0

frequency = 300

width = 800
height = 800
background = (1,1,1)
dpi=100

waypoints = [ [200,600] , [600,600] ]
velocity = 1.0
size = 5
color = (1,0,0)
hard_target_display=True
hard_target = WayPointsHardTarget(waypoints,
                                  velocity,
                                  size=size,
                                  color=color)


duration = 180
size = 5
color = (0,1,0)
soft_target_display=True
soft_target = TimeDriftingSoftTarget(duration,
                                     size=size,
                                     color=color)

kp = 1.0
size = 3.0
color = (0,0,1)
mediator_display=True
mediator = LinearMediator(kp,size,color)


size = 5
color = (1,1,0)
cursor = BasicCursor(size,color)

experiment = Experiment(width,
                        height,
                        background,
                        soft_target,
                        mediator,
                        hard_target,
                        cursor)

gui = PacingAndLeading(experiment,dpi,
                       hard_target_display=hard_target_display,
                       soft_target_display=soft_target_display,
                       mediator_display=mediator_display)
plt.show()
