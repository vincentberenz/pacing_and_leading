import time,math
import .geometry as geometry
import .control as control


""" The hard target is the (typically) invisible circle representing the 
    desired motion of the user, i.e. during a successful experiment the 
    user would move to keep the cursor on top of the hard target

    This module contains a collection of different hard targets that can be selected
    for an experiment.

    @copyright Copyright (c) 2020 Max Planck Gesellschaft
    @author Vincent Berenz

"""

class WaypointsHardTarget :

    """ this hard target moves from one waypoint to the other,
        at constant speed

        Args: 
           kp : list of waypoints
           velocity : in pixels per second
           size : in pixels
           color : color (None if invisible)
    """

    
    def __init__(self,
                 waypoints,
                 velocity,
                 size=None,
                 color=None):

        self._velocity = velocity
        self._waypoints = waypoints
        self._position = self._waypoints[0]
        self._previous_waypoints = self._waypoints[0]
        self._previous_time = None
        self._index = 1
        self._size = size
        self._color = color

    def __call__(self,world):

        t = time.time()
        if self._previous_time is None:
            self._previous_time = t
        delta_t = t - self._previous_time
        self._previous_time = t
        
        waypoint = self._waypoints[self._index]
        total_d = geometry.distance(waypoint,self._previous_waypoint)
        performed_d = self._velocity * delta_t
        
        if performed_d > total_d:
            self._previous_waypoint = self._waypoints[self._index]
            self._index += 1
            if self._index >= len(self._waypoints):
                self._index = 0
            self._previous_time = None
            return self(world)

        total_v = [w-pw
                   for w,pw in zip(waypoint,self._previous_waypoint)]
        norm_v = math.sqrt(sum([v**2 for v in total_v]))

        self._position = [performed_d*v/norm_v for v in total_v]

        return self._position,self._size,self._color
