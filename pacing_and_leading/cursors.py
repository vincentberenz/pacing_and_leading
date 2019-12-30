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
