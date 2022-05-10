import math

from pygame import Vector2


def clamp_on_range(x, min_value, max_value):
    return max(min(x, max_value), min_value)


def clamp_on_rectangle(point, rectangle):
    clamp = Vector2()
    clamp.x = clamp_on_range(
        point.x,
        rectangle.x,
        rectangle.x + rectangle.width
    )
    clamp.y = clamp_on_range(
        point.y,
        rectangle.y,
        rectangle.y + rectangle.height
    )
    return clamp


def project_vector(project, onto):
    d = onto.dot(onto)
    if 0 <= d:
        dp = project.dot(onto)
        return onto * (dp/d)
    return onto


def circle_point_collide(circle, point):
    center = Vector2(circle.x, circle.y)
    distance = (center - point).magnitude()
    return distance <= circle.radius


def circle_segment_collide(circle, p1, p2):
    if circle_point_collide(circle, p1):
        return True
    if circle_point_collide(circle, p2):
        return True

    center = Vector2(circle.x, circle.y)
    d = p2 - p1
    lc = center - p1
    p = project_vector(lc, d)
    nearest = p1 + p

    return circle_point_collide(circle, nearest) and p.magnitude() <= d.magnitude() and 0 <= p.dot(d)


def circle_rectangle_collide(circle, rectangle):
    center = Vector2(circle.x, circle.y)
    clamped = clamp_on_rectangle(center, rectangle)
    return circle_point_collide(circle, clamped)
