from ..pacing_and_leading import geometry
from ..pacing_and_leading import control



class BasicCursor:

    def __init__(self,
                 size,
                 color):

        self._size = size
        self._color = color


    def __call__(self,world):

        cursor = world.cursor
        return cursor,self._size,self._color


class VelocityCursor:

    def __init__(self,
                 size,
                 color_slow,
                 color_fast,
                 velocity_threshold):

        self._size = size
        self._color_slow = color_slow
        self._color_fast = color_fast
        self._threshold = velocity_threshold
        self._velocity = control.Velocity()
        

    def __call__(self,world):

        cursor = world.cursor
        velocity = self._velocity.get(cursor)

        if velocity is None:
            return cursor,self._size,self._color_slow

        n = geometry.norm(velocity)

        if n>self._threshold:
            return cursor,self._size,self._color_fast

        return cursor,self._size,self._color_slow
