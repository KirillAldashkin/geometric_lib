def area(a, b): 
    '''
    Calculates the area of a rectangle with given sides.
        Parameters:
            a - Length of the first side
            b - Length of the second side
        Return value:
            Area of a rectangle with sides 'a' and 'b'
    '''
    if a <= 0: raise ValueError("Side 'a' is not positive")
    if b <= 0: raise ValueError("Side 'b' is not positive")
    return a * b 

def perimeter(a, b): 
    '''
    Calculates the perimeter of a rectangle with given sides.
        Parameters:
            a - Length of the first side
            b - Length of the second side
        Return value:
            Perimeter of a rectangle with sides 'a' and 'b'
    '''
    if a <= 0: raise ValueError("Side 'a' is not positive")
    if b <= 0: raise ValueError("Side 'b' is not positive")
    return 2 * (a + b)
