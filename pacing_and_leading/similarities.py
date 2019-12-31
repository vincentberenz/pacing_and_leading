from ..pacing_and_leading import control
from ..pacing_and_leading import geometry

class WeightedVelocitySimilarity:

    def __init__(self,weight_direction=0.5,
                 weight_norm=0.5,max_velocity=200):

        self._velocity_cursor = control.Velocity()
        self._velocity_hard_target = control.Velocity()
        self._weight_direction = weight_direction
        self._weight_norm = weight_norm
        self._weights  = weight_norm + weight_direction
        self._max_velocity = max_velocity

    def __call__(self,cursor,hard_target):

        velocity_cursor = self._velocity_cursor.get(cursor)
        velocity_hard_target = self._velocity_hard_target.get(hard_target)

        if velocity_cursor is None or velocity_hard_target is None:
            return None

        norm_cursor = geometry.norm(velocity_cursor)
        norm_hard_target = geometry.norm(velocity_hard_target)

        if norm_cursor > norm_hard_target:
            norm_similarity = norm_hard_target / norm_cursor
        else :
            norm_similarity = norm_cursor / norm_hard_target

        dot = geometry.dot(velocity_cursor,
                           velocity_hard_target)

        angle_similarity = 0.5+dot/2.0

        n = self._weight_norm*norm_similarity
        a = self._weight_direction*angle_similarity
        return (a+n)/self._weights


class ProductVelocitySimilarity:

    def __init__(self,
                 max_velocity=200):

        self._velocity_cursor = control.Velocity()
        self._velocity_hard_target = control.Velocity()
        self._max_velocity = max_velocity

    def __call__(self,cursor,hard_target):

        velocity_cursor = self._velocity_cursor.get(cursor)
        velocity_hard_target = self._velocity_hard_target.get(hard_target)

        if velocity_cursor is None or velocity_hard_target is None:
            return None

        norm_cursor = geometry.norm(velocity_cursor)
        norm_hard_target = geometry.norm(velocity_hard_target)

        if norm_cursor > norm_hard_target:
            norm_similarity = norm_hard_target / norm_cursor
        else :
            norm_similarity = norm_cursor / norm_hard_target

        dot = geometry.dot(velocity_cursor,
                           velocity_hard_target)

        angle_similarity = 0.5+dot/2.0

        return angle_similarity*norm_similarity

