from math import *
import sympy as sp
from sympy.plotting import plot

def PolTaylor(a,n):
    x = sp.symbols('x')
    f = sp.exp(x)
    T = f.subs(x, a)
    for k in range(1, n+1):
       dfk = sp.diff(f, x)
       T = T+dfk.subs(x,a)*((x-a)**k)/factorial(k)
       f=dfk

    print(sp.expand(T))
    g = plot(f, T, (x, a-5, a+5), title='polinomio de taylor', show=)
    g[0].line_color = 'blue'
    g[1].line_color = 'red'
    g.show()

a = float(input('Digite alrededor de cual punto desea un polinomio'))
n = int(input('Digite el orden del polinomio'))
PolTaylor(a,n)