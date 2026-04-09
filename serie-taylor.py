from math import *

import sympy as sp

from sympy.plotting import plot

def PolTaylor(a,n):
    x = sp.symbols('x')
    f = sp.log(x)
    T = f.subs(x, a)
    for k in range(1, n+1):
        dfk = sp.diff(f, x)
        T = T+dfk.subs(x,a)*((x-a)**k)/factorial(k)
        f = dfk
    print(sp.expand(T))
    g=plot(f,T,(x, a-3, a+3), title='Polinomio de taylor',show=False)
    g[0].line_color='blue'
    g[1].line_color='red'
    g.show()
a = float(input('Digite alrededor de cual punto desea la serie de polinomios  '))
n = int(input('Digite el orden del polinomio de taylor  '))
PolTaylor(a,n)