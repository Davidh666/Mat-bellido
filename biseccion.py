from math import *

def f (x):
    return exp(-x)-x;

def biseccion (a, b, tol):
    m1=a;
    m=b;
    k=0;
    if(f(a)*f(b)>0):
        print("No cambia de signo");

    while(abs(m1-m)>tol):
        m1=m;
        m=(a+b)/2;
        if(f(a)*f(m)<0): #cambia de signo entre a y m
            b=m;
        if(f(m)*f(b)<0): #cambia de signo entre m y b
            a=m;
        print('El intervalo es [',a,',',b,']')
        k=k+1;
    print('x',k,'=',m,'  es una buena aproximación');

biseccion(0, 1, 0.0001)
