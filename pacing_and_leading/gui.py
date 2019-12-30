import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


class PacingAndLeading:

    def __init__(self,
                 experiment,
                 dpi,
                 hard_target_display=False,
                 soft_target_display=False,
                 mediator_display=True):

        # creating the main figure
        self._figure = plt.figure()
        self._figure.set_dpi(dpi)
        self._figure.set_size(experiment.width,
                              experiment.height)

        # setting the cursor motion callback
        self._figure.canvas.mpl_connect('cursor_motion',
                                        self.mouse_move)
        
        self._axis = plt.axes(xlim=(0,width),
                              ylim=(0,height))
        
        # middle of main figure
        self._center = [width/2,height/2]

        # will return for each iteration the
        # position of each circle to draw
        self._experiment = experiment

        # initial cursor position
        self._cursor_position = self._center

        # creating the matplotlib circles to draw.
        # if display is False, no circle is drawn
        def _gen_circle(display):
            if display:
                circle = plt.Circle(self._center,0,fc="white")
                self._axis.add_patch(circle)
                return circle
            else :
                return None
        
        self._hard_target = _gen_circle(hard_target_display)
        self._soft_target = _gen_circle(soft_target_display)
        self._mediator = _gen_circle(mediator_display)
        self._cursor = _gen_circle(True)

        # not that the order is the same as of
        # Experiment._circles
        self._draw_circles = [self._hard_target,
                              self._soft_target,
                              self._mediator,
                              self._cursor]

        # management of the animation by matplotlib
        self._animation = animation.FuncAnimation(self._figure,
                                                  self.animate,
                                                  interval=1000.0/experiment.frequency,
                                                  blit=True)
        
    def mouse_move(self,event):

        self._cursor_position = [event.xdata,
                        event.ydata]
        
        
    def animate(self,None):

        circles = self._experiment.update(self._cursor_position)

        def draw(circle,draw_circle):
            if draw_circle is None:
                return
            draw_circle.center = circle.position
            draw_circle.set_radius(circle.size)
            draw_circle.fill=True
            draw_circle.set_color(circle.color)
            return

        for circle,draw_circle in zip(circles,self._draw_circles):
            draw(circle,draw_circle)

            
        
        

