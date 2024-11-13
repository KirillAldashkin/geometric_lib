def area(a):
    '''
    Calculates the area of a square with a given side.
        Parameters:
            a - Length of the side
        Return value:
            Area of a square with side 'a'
    '''
    if a <= 0: raise ValueError("Side is not positive")
    return a * a

def perimeter(a):
    '''
    Calculates the perimeter of a square with a given side.
        Parameters:
            a - Length of the side
        Return value:
            Perimeter of a square with side 'a'
    '''
    if a <= 0: raise ValueError("Side is not positive")
    return 4 * a
