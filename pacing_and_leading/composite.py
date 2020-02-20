from ..pacing_and_leading import geometry

class Composite:

    def __init__(self,instances):

        self._instances = instances
        self._total_weights = float(sum([i[0] for i in instances]))

        
    def __call__(self,arg1,arg2=None):

        def _none_safe(v):
            if v is None:
                return 0
            return v
        
        if arg2 is None:
            # for positions (vectors)
            r = self._instances[0][1](arg1)
            _,size,color = r
            weighted_vectors = [[i[0],i[1](arg1)[0]] for i in self._instances]
            value =  geometry.linear_combination(weighted_vectors)
            return [v/self._total_weights for v in value],size,color
        else :
            # for similarity (scalar)

            value = sum([i[0]*_none_safe(i[1](arg1,arg2)) for i in self._instances])
            return value/self._total_weights

                
