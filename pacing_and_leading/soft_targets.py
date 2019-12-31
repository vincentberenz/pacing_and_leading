import time,math
from collections import deque
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
        
        self._position = [c+d*v_/norm_v
                          for c,v_ in zip(cursor,v)] 

        return self._position,self._size,self._color


# if similar : toward hard target,
# else, toward cursor
    
class SimilaritySoftTarget:

    def __init__(self,
                 similarity_average_period,
                 size=None,
                 color=None):

        if similarity_average_period is not None:
            self._similarities = control.Averager(similarity_average_period)
        else :
            self._similarities = None
        self._color = color
        self._size = size
        
    def __call__(self,world):

        cursor = world.cursor
        hard_target = world.hard_target
        similarity = world.similarity

        if similarity is None:
            return cursor,self._size,self._color

        if self._similarities is not None:
            similarity = self._similarities.get(similarity)
        
        v = [ht-c for ht,c in
             zip(hard_target,cursor)]
        norm_v = geometry.norm(v)
        total_d = geometry.distance(cursor,hard_target)
        d = similarity * total_d
        
        position = [c+d*v_/norm_v
                    for c,v_ in zip(cursor,v)] 
        
        return position,self._size,self._color
    
