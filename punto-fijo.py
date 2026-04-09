from math import *

def g(x):
    return cos(x)
def punto_fijo(x0, tol, n):
    for k in range(n):
        x1 =g(x0)
        if(abs(x1-x0)<tol):
            print('x', k+1, '=', x1, 'es un punto fijo')
            return 
        x0 = x1
        print('x', k+1, '=', x1)


punto_fijo(pi, 0.0000001, 10)