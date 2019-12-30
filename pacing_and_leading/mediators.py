import time,math
import .geometry as geometry
import .control as control
    

""" The mediator is the (visible) circle that tries to influence the user's behavior

    This module contains a collection of different mediators that can be selected
    for an experiment.

    @copyright Copyright (c) 2020 Max Planck Gesellschaft
    @author Vincent Berenz

"""

class LinearMediator :

    """ This mediator moves toward the soft target 
        using a linear controller with constant kp,
        size and color

        Args: 
           kp : linear gain to compute the current velocity
           size : size in pixels
           color : color (None if invisible)
           position : starting position
    """
    
    def __init__(self,kp,size,color,position=(0,0)):
        
        self._kp = kp
        self._position = position
        self._size = size
        self._color = color
        self._previous_time = None

    # assumes world as a soft target attribute
    def __call__(self,world):

        soft_target = world.soft_target
        self._previous_time,self._position = control.linear_controller( self._previous_time,
                                                                        self._position,
                                                                        soft_target,
                                                                        self._kp)
        return self._position,self._size,self._color





    
                   
        
                
