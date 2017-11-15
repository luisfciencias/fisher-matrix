# tools for the Fisher matrix implementation
from scipy.misc import derivative


# function to extract the partial derivative of a function in a point
def partial_derivative(func, var=0, point=[]):
    '''
    calculate the partial derivative of the function `func' with
    respect to the variable number `var' in the point given by 
    the list of values `point'
    example: if f(x,y) = x**2 + y
    df/dx[1,1] = partial_derivative(f, 0, [1,1]) = 2.0 (modulo round error)
    df/dy[1,1] = partial_derivative(f, 1, [1,1]) = 1.0 (modulo round error)
    '''
    args = point[:]
    def wraps(x):
        args[var] = x
        return func(*args)
    return derivative(wraps, point[var], dx = 1e-6)
