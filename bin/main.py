from ..pacing_and_leading.gui import PacingAndLeading
from ..pacing_and_leading.mediators import *
from ..pacing_and_leading.hard_targets import *
from ..pacing_and_leading.soft_targets import *
from ..pacing_and_leading.cursors import *
from ..pacing_and_leading.similarities import *
from ..pacing_and_leading.experiment import Experiment


if __name__ == "__main__":

    # ---------- window and experiment config ---------- #

    # to be used in future for logging
    USER_ID = 0

    # frequency of main program iteration
    frequency = 300

    # config of the window
    width = 800
    height = 800
    background = (1,1,1)
    dpi=100

    # logging file. Currently only logging the
    # similarity (cf below)
    data_file = "/tmp/pacing_and_leading"
    
    # ---------- similarity computation ---------- #

    # see similarities.py for code
    
    # compute the similarity between the cursor motion and
    # the hard target motion (see below). Score between 0 (dissimilar)
    # and 1 (similar)

    # the (secret) goal of the program is to increase the
    # similarity over time, i.e. "tricking" the user into
    # moving the cursor in a manner similar the hard target
    # moves.

    # you can choose between:
    
    # 1 --- WeightedVelocitySimilarity is a weighted score between
    # difference in norm and direction of the velocity
    
    #weight_norm=0.5
    #weight_direction=0.0
    #similarity=WeightedVelocitySimilarity(weight_direction=weight_direction,
    #                                      weight_norm=weight_norm)

    # 2 --- ProductVelocitySimilarity is the product between
    # similarity of the velocities norm and similarity
    # in direction of velocities
    
    similarity=ProductVelocitySimilarity()

    
    # ---------- hard target motion ---------- #

    # the hard target is the circle which motion
    # defines the desired motion of the user, i.e if
    # the experiment is a success, the cursor motion becomes the
    # same (according to the similarity function defined above)
    # as the hard target

    # set hard_target_display to True to see it. In normal
    # experiment, the hard target is secret to the user, and
    # hard_targe_display is False

    # see hard_targets.py for code

    # You can choose between:
    
    # 1 --- WaypointsHardTarget has the target moving at
    # constant speed between predefined waypoints
    
    waypoints = [ [200,200] , [600,200] ]
    velocity = 100.0
    size = 40
    color = (1,0,0)
    hard_target_display=False
    hard_target = WaypointsHardTarget(waypoints,
                                      velocity,
                                      size=size,
                                      color=color)


    # ---------- soft target motion ---------- #

    # The soft target is some intermediate between
    # the cursor and the hard target.
    # Idea is: if the soft target is the cursor, then
    # the mediator motion (see below) is purely reactive,
    # if the soft target is the hard target, then
    # the mediator motion is feed forward (ignores user motion)
    # "Intermediate" soft target motions are between
    # reactive and feed forward

    # set soft_target_display=True to see the soft target.
    # In experiment, expected value is False 

    # see soft_targets.py for code
    
    size = 40
    color = (0,1,0)
    soft_target_display=False

    # You can choose between:
    
    # 1 --- TimeDriftingSoftTarget : motion of the soft target
    # is first purely reactive, then becomes feed forward
    # as time goes by. change "duration" to make this transition
    # slower or faster
    
    #duration = 180
    #soft_target = TimeDriftingSoftTarget(duration,
    #                                     size=size,
    #                                     color=color)

    # 2 --- SimilaritySoftTarget : motion of the soft target
    # is more feedforward if the motion of the cursor is similar
    # to the one of the hard target, and more reactive if dissimilar.

    # Optionally, not the current similarity score is used, but a
    # value averaging the similarity over x seconds (similarity_average_period,
    # which can be set to None for no averaging)

    similarity_average_period=5
    soft_target = SimilaritySoftTarget(similarity_average_period,
                                       size=size,
                                       color=color)

    

    # ---------- mediator ---------- #

    # The mediator is the circle visible to the user.
    # The software is trying to influence the motion of the user
    # via the motion of the mediator.
    # In the Apollo experiment, the mediator is the hand of the robot.
    # The motion of the mediator is strongly related to the soft target
    # (see above). In practice, the mediator "follows" the soft target,
    # with some delay.

    # see mediators.py for code
    
    size = 40
    color = (0,0,1)
    mediator_display=True

    # you can choose between:
    
    # 1 --- LinearMediator
    # The mediator goes toward the soft target using a
    # proportional controller over the speed.
    # The higher the gain (kp), the faster the motion.
    
    #kp = 0.7
    #mediator = LinearMediator(kp,size,color)

    # 2 --- SimilarityMediator
    # The mediator goes toward the soft target using a
    # proportional controller over the speed.
    # The gain changes with the similarity between the
    # cursor and the hard target motions.
    # The more similar, the higher the gain (and the faster
    # the mediator motion).

    # Optionally, not the current similarity score is used, but a
    # value averaging the similarity over x seconds (similarity_average_period,
    # which can be set to None for no averaging)
    
    kp_min = 0.4
    kp_max = 2.0
    similarity_average_period=None
    mediator = SimilarityMediator(similarity_average_period,
                                  kp_min,kp_max,
                                  size,color)

    
    # ---------- cursor ---------- #

    # What the user moves on the screen with
    # the mouse

    # see cursors.py for code
    
    size = 40
    
    # 1 --- BasicCursor
    # A simple circle 
    
    #color = (0,1,1)
    #cursor = BasicCursor(size,color)

    # 2 --- VelocityCursor
    # A circle which color changes depending on the velocity
    # of the cursor. Idea is to encourage at least some motion
    # from the user.

    velocity_threshold=10
    color_slow = (0.9,1,0.9)
    color_fast = (0,1,0)
    cursor = VelocityCursor(size,color_slow,color_fast,
                            velocity_threshold)

    
    # ---------- experiment code, do not touch ---------- #
    
    experiment = Experiment(frequency,
                            width,
                            height,
                            background,
                            similarity,
                            soft_target,
                            mediator,
                            hard_target,
                            cursor,
                            data_file)

    gui = PacingAndLeading(experiment,dpi,
                           hard_target_display=hard_target_display,
                           soft_target_display=soft_target_display,
                           mediator_display=mediator_display)
    gui.run()

    experiment.save()

    Experiment.plot_results(data_file)

