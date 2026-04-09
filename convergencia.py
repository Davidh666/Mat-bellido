from math import *

def fp_convergence(func, a, b, error_accept):

    def f(x):
        return eval(func)
    if f(a) * f(b) >= 0:
        print("No hay cambio de signo en el intervalo.")
        return
    c = a
    error = 1.0
    i = 0 

    print(f"{'Iteracion ':<5} | {'Raiz aprox':<12} | {'Error':<12} | ")

    print("-" * 35)

    while error > error_accept:
        c_anterior = c
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        error = abs(c-c_anterior)
        i+=1
        print(f"{i:<5} | {c:<12.6f} | {error:<12.6e} | ")

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("-" * 35)

    print(f"La raiz es: {c}")

fp_convergence("x**3 - 2*x - 5", 2, 3, 0.0001)