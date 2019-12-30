import math



def linear_controller( previous_time,
                       current_position,
                       target_position,
                       kp ):

    """
    Linear controller over velocity
    Returns:
        updated previous time, next position 
    """
    
    t = time.time()
    if previous_time is None:
        return t,current_position
    delta_t = t - previous_time
    previous_time = t
    return previous_time, [ kp*(cp-tp)*delta_t for cp,tp
                            in zip(current_position,target_position) ]
