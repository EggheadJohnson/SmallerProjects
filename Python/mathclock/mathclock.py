#For Christmas I received a clock from my mother-in-law.  This clock, instead of having numbers,
#had equations.  Naturally, I had to verify each of the equations.  They all checked out.
#Paul Johnson
#Christmas 2013

from math import *

def integral(lam, stepSize=0.001, start=0, end=10000):
    tot = 0
    counter = start
    while counter < end:
        tot += lam(counter)*stepSize
        counter += stepSize
    return tot

def two(stepSize=0.001, end=10000):
    gam = 0.5772156649
    eq = lambda x: (exp(-x**2)-exp(-x))/x
    integ = integral(eq, stepSize, stepSize)
    return gam/integ

def three():
    a = atan(1/7.)
    a = 5/2*a
    a = pi/8 - a
    a = tan(a)
    a = 79*a
    return a

def four(stepSize=1, end=10000):
    eq = lambda k: pow(-1, k)/(2*k+1)
    sm = integral(eq,1)
    return pi/sm

def five():
    a = 1/4.*atan(1/238.)
    a += pi/16.
    a = tan(a)
    return 1/a

def six():
    eq = lambda x: log(x)/(x-1)
    integ = integral(eq,0.00001,0.00001,1)
    return pow(pi,2)/integ

def seven():
    a = 2*atan(1/3.)
    a = pi/4 - a
    a = tan(a)
    return 1/a

def eight(stepSize = 1):
    eq = lambda k: 1/(pow((2*k+1),2))
    sm = integral(eq,stepSize)
    return pow(pi,2)/sm

def nine():
    t1 = tan(pi/9)
    t2 = tan(2*pi/9)
    t3 = tan(4*pi/9)
    ta = t1*t2*t3
    return pow(ta,4)

def ten():
    phi = 1.6180339
    p = 1/(2*phi)
    return pi/asin(p)

def eleven():
    eq = lambda k: pow(1/sin(k*pi/1000), 4)
    sm = integral(eq,1,1,1000)
    return pow(10,12)+pow(10,7)-45*sm

def twelve():
    eq = lambda x: x/(sinh(sqrt(3)*x))
    integ = integral(eq,0.0001,0.0001,100)
    return pow(pi,2)/integ

#print two()
#print three()
#print four()
#print five()
#print six()
#print seven()
#print eight()
#print nine()
#print ten()
#print eleven()
#print twelve()


