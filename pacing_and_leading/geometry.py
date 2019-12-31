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


def normalize(v,target_norm=1):

    n = norm(v)
    return [v_*target_norm/n for
            v_ in v]


def dot(v1,v2):

    v1_ = normalize(v1)
    v2_ = normalize(v2)

    return sum([a*b
                for a,b in zip(v1_,v2_)])

def linear_combination(weight_vectors):
    s = len(weight_vectors[0][1])
    weighted = [[w*a for a in v]
                for w,v in weight_vectors]
    w = [sum([a[i] for a in weighted]) for i in range(s)]
    return w
