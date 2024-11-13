def area(a, h): 
    '''
    Calculates the area of a triangle with a given height and base.
        Parameters:
            a - Length of the base
            h - Length of the height
        Return value:
            Area of a triangle with base 'a' and height 'h'
    '''
    if a <= 0: raise ValueError("Base is not positive")
    if h <= 0: raise ValueError("Height is not positive")
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Calculates the perimeter of a triangle with given sides.
        Parameters:
            a - Length of the first side
            b - Length of the second side
            c - Length of the third side
        Return value:
            Perimeter of a triangle with sides 'a', 'b' and 'c'
    '''
    if a <= 0: raise ValueError("Side 'a' is not positive")
    if b <= 0: raise ValueError("Side 'b' is not positive")
    if c <= 0: raise ValueError("Side 'c' is not positive")
    return a + b + c 
