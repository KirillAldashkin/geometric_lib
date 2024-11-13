import math

def area(r):
    '''
    Calculates the area of a circle with a given radius.
        Parameters:
            r - Radius of a circle
        Return value:
            Area of a circle with radius 'r'
    '''
    return math.pi * r * r

def perimeter(r):
    '''
    Calculates the circumference of a circle with a given radius.
        Parameters:
            r - Radius of a circle
        Return value:
            Circumference of a circle with radius 'r'
    '''
    return 2 * math.pi * r
