import math

def area(r):
    '''
    Calculates the area of a circle with a given radius.
        Parameters:
            r - Radius of a circle
        Return value:
            Area of a circle with radius 'r'
        Raises:
            ValueError - if radius is not positive
    '''
    if r <= 0: raise ValueError("Radius is not positive")
    return math.pi * r * r

def perimeter(r):
    '''
    Calculates the circumference of a circle with a given radius.
        Parameters:
            r - Radius of a circle
        Return value:
            Circumference of a circle with radius 'r'
        Raises:
            ValueError - if radius is not positive
    '''
    if r <= 0: raise ValueError("Radius is not positive")
    return 2 * math.pi * r
