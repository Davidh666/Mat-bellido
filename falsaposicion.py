def fp_method(func, a, b, error_accept):


    
    # Método de la falsa posición para encontrar raíces de una función dada.
    # Parámetros:
    # func: La función de la cual se desea encontrar la raíz, dada como una cadena.
    # a: El valor inicial de la variable independiente.
    # b: El valor final de la variable independiente.
    # error_accept: El error aceptado.
    # Retorno:
      
   
    def f(x):
        return eval(func)
    
    i = 0
    c_before = 0
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))
    error = 1.0

    while error > error_accept:
        c_after = (a * f(b) - b * f(a)) / (f(b) - f(a))


        if f(a) * f(b) >= 0:
            print("No se puede aplicar el método de la falsa posición.")
            break

        elif f(a) * f(c_after) < 0:
            error = abs(c_after - b)
            b = c_after
            i = i + 1
        
        elif f(b) * f(c_after) < 0:
            error = abs(c_after - a)
            a = c_after
            i = i + 1

        else:
            print("No se puede aplicar el método de la falsa posición.")
            break

        # Reemplaza tus prints por estos:
        print(f"Iteración {i}: Error = {error:.6e}")
        print(f"Raíz aprox = {c_after:.6f}")
        print(f"Intervalo actual = [{a:.6f}, {b:.6f}]")
        print("-" * 40)


fp_method("x**3 - 2*x - 5", 2, 3, 0.0001)