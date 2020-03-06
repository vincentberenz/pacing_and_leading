import time,math
from ..pacing_and_leading import geometry

class Arrow:

    def __init__(self,
                 position,
                 length,
                 color):

        self._length = length
        self._position = position
        self._color = color

    def get(self):

        return self._position,self._length,self._color
        
    def __call__(self,world):

        soft_target = world.soft_target

        if not soft_target:
            return self._position,[0,0],self._color

        v = [st-p
             for st,p in zip(soft_target,
                             self._position)]

        v = geometry.normalize(v,target_norm=self._length)

        return self._position,v,self._color
        
