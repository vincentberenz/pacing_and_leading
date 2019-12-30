from ..pacing_and_leading.gui import PacingAndLeading
from ..pacing_and_leading.mediators import *
from ..pacing_and_leading.hard_targets import *
from ..pacing_and_leading.soft_targets import *
from ..pacing_and_leading.cursors import *
from ..pacing_and_leading.experiment import Experiment


if __name__ == "__main__":

    USER_ID = 0

    frequency = 300

    width = 800
    height = 800
    background = (1,1,1)
    dpi=100

    waypoints = [ [200,600] , [600,600] ]
    velocity = 1.0
    size = 40
    color = (1,0,0)
    hard_target_display=True
    hard_target = WaypointsHardTarget(waypoints,
                                      velocity,
                                      size=size,
                                      color=color)


    duration = 180
    size = 40
    color = (0,1,0)
    soft_target_display=True
    soft_target = TimeDriftingSoftTarget(duration,
                                         size=size,
                                         color=color)

    kp = 1.0
    size = 40
    color = (0,0,1)
    mediator_display=True
    mediator = LinearMediator(kp,size,color)


    size = 40
    color = (0,1,1)
    cursor = BasicCursor(size,color)

    experiment = Experiment(frequency,
                            width,
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
    gui.run()
