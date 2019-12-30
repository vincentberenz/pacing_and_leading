import time,math
from ..pacing_and_leading import geometry
from ..pacing_and_leading import control
    

""" The soft target is an intermediate position between the user cursor
    and the hard target. It is likely to be the virtual point the 
    mediator goes toward. 

    This module contains a collection of soft targets that can be selected
    for an experiment.

    @copyright Copyright (c) 2020 Max Planck Gesellschaft
    @author Vincent Berenz

"""


class TimeDriftingSoftTarget:

    """ Moves from the user cursor to the 
        hard target over a fixed duration
    """
    
    def __init__(self,duration,
                 size=None,color=None):

        self._duration = duration
        self._time_start = None
        self._color = color
        self._size = size

    def __call__(self,world):

        t = time.time()
        if self._time_start is None:
            self._time_start = t

        delta_t = t-self._time_start

        cursor = world.cursor
        hard_target = world.hard_target

        if delta_t > self._duration :
            return hard_target

        v = [ht-c for ht,c in
             zip(hard_target,cursor)]
        norm_v = geometry.norm(v)
        
        ratio = delta_t / self._duration
        total_d = geometry.distance(cursor,hard_target)
        d = ratio * total_d
        
        self._position = [d*v_/norm_v for v_ in v] 

        return self._position,self._size,self._color
