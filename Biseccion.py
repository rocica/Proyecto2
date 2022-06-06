import numpy as np
from matplotlib import pyplot as pyp

input ("Ingrese los terminos solicitados.\nPara el término independiente escriba 0 en el exponente")
t1 = float (input ("Primer término: "))
t2 = float (input ("Segundo término: "))
t3 = float (input ("Tercer término: "))
c1 = float (input ("Primer exponente: "))
c2 = float (input ("Segundo exponente: "))
c3 = float (input ("Tercer exponente: "))
emax = float (input("Ingrese el error tolerable: "))

def f(t1, t2, t3, c1, c2, c3, x) :
    return t1* x ** c1 + t2 * x ** c2 + t3 * x ** c3 

def bisec(t1, t2, t3, c1, c2, c3, f, a, b, emax, N=100) :
    x = (a + b)/2
    for k in range(N) :
        x = (a + b) /2
        # derecho-›cambio de signo
        if f (t1, t2, t3, c1, c2, c3, x) * f(t1, t2, t3, c1, c2, c3,b) <0:
            a=x
        #izquierdo-›cambio de signo
        elif f(t1, t2, t3, c1, c2, c3, x) * f(t1, t2, t3, c1, c2, c3, a) <0:
            b=x
        else:
            break
        xold = x
        x = (a + b)/2
        e=abs((x - xold) / x)
        if e < emax:
            break
        print (k, x, f(t1, t2, t3, c1, c2, c3, x), '{:%}'.format(e))

x = range(-10,10)
pyp.plot(x, [f(t1, t2, t3, c1, c2, c3, i) for i in x])
pyp.axhline(0, color="red")
pyp.axvline(0, color="black")
pyp.show()

r1 = float (input ("Ingrese el punto A: "))
r2 = float (input ("Ingrese el punto B: "))

bisec (t1, t2, t3, c1, c2, c3, f, r1, r2, emax)