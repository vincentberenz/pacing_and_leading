import time,math


def distance(p1,p2):
    
    """
    returns the euclidian distance between p1 and p2
    """
    
    return math.sqrt(sum([(a-b)**2
                          for a,b in zip(p1,p2)]))

def norm(v):

    """
    returns norm of vector v
    """
    
    return math.sqrt(sum([a**2 for a in v]))
