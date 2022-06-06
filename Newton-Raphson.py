import numpy as np
import matplotlib.pyplot as plt

def f(x, t1, t2, t3, c1, c2, c3):
  return t1* x ** c1 + t2 * x **c2 + t3 * x ** c3

def df(x, et1, et2, et3, ec1, ec2, ec3):
  return et1* x ** ec1 + et2 * x **ec2 + et3 * x ** ec3

def newtonrap(f,df,limite=50):
  print ("Ingrese los terminos solicitados.\nPara el término independiente escriba 0 en el exponente")
  t1 = float (input ("Primer término de la funcion: "))
  t2 = float (input ("Segundo término de la funcion: "))
  t3 = float (input ("Tercer término de la funcion: "))
  c1 = float (input ("Primer exponente de la funcion: "))
  c2 = float (input ("Segundo exponente de la funcion: "))
  c3 = float (input ("Tercer exponente de la funcion: "))

  et1 = float (input ("Primer término de la funcion derivada: "))
  et2 = float (input ("Segundo término de la funcion derivada: "))
  et3 = float (input ("Tercer término de la funcion derivada: "))
  ec1 = float (input ("Primer exponente de la funcion derivada: "))
  ec2 = float (input ("Segundo exponente de la funcion derivada: "))
  ec3 = float (input ("Tercer exponente de la funcion derivada: "))

  x = np.linspace(-20,20,1000)
  plt.plot(x, f(x, t1, t2, t3, c1, c2, c3))
  plt.axhline(0, color="pink")
  plt.axvline(0, color="pink")
  plt.ylim(-20, 20)
  plt.grid()
  plt.show()
  
  x0 = float(input("Ingrese valor inicial: "))
  emax=float(input("Ingrese error tolerado: "))
  
  print("{:^5} {:^15} {:^15} {:^15} {:^15} {:^15} ".format("Iteracion", "x0", "xsolucion", "Error", "f(x0)", "f'(x0)"))
  
  for k in range(limite):
    x1=x0-f(x0, t1, t2, t3, c1, c2, c3)/df(x0, et1, et2, et3, ec1, ec2, ec3)
    error=abs((x1-x0)/x1)
    print("{:^4d} {:^20.6f} {:^15.6f} {:^15.6f} {:^15.6f} {:^15.6f}".format(k, x0, x1, error, f(x0, t1, t2, t3, c1, c2, c3), df(x0, et1, et2, et3, ec1, ec2, ec3)))
    if error<emax:
      break
    x0=x1
  print("La raiz solucion es: " ,x1)
  x = np.linspace(-20,20,100)
  plt.plot(x, f(x, t1, t2, t3, c1, c2, c3))
  plt.plot(x0, f(x0, t1, t2, t3, c1, c2, c3), 'or')
  plt.axhline(0, color="pink")
  plt.axvline(0, color="pink")
  plt.ylim(-20, 20)
  plt.grid()
  plt.show()


newtonrap(f, df)



#VERSION SIN PEDIR LA FORMULA O LA DERIVADA
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return x**3-2*x-5

def df(x):
  return 3*(x**2)+2

def newtonrap(f,x0,df,limite=50):
  emax=float(input("Ingrese error tolerado: "))
  print("{:^5} {:^15} {:^15} {:^15} {:^15} {:^15} ".format("Iteracion", "x0", "xsolucion", "Error", "f(x0)", "f'(x0)"))
  for k in range(limite):
    x1=x0-f(x0)/df(x0)
    error=abs((x1-x0)/x1)
    print("{:^4d} {:^20.6f} {:^15.6f} {:^15.6f} {:^15.6f} {:^15.6f}".format(k, x0, x1, error, f(x0), df(x0)))
    if error<emax:
      break
    x0=x1
  print("La raiz solucion es: " ,x1)
  print("Estudiantes: Castillo Felipe, Cortez Rocio")
  x = np.linspace(-20,20,100)
  plt.plot(x, f(x))
  plt.plot(x0, f(x0), 'or')
  plt.axhline(0, color="pink")
  plt.axvline(0, color="pink")
  plt.ylim(-20, 20)
  plt.grid()
  plt.show()

x = np.linspace(-20,20,1000)
plt.plot(x, f(x))
plt.axhline(0, color="pink")
plt.axvline(0, color="pink")
plt.ylim(-20, 20)
plt.grid()
plt.show()

vi = float(input("Ingrese valor inicial: "))
newtonrap(f, vi, df)"""
