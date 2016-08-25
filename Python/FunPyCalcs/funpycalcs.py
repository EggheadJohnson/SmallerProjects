from random import *
from math import *
from decimal import *

def withPoints(n = 1000):
    count = 0
    for iter in range(n):
        x = random()
        y = random()
        count += sqrt(x**2+y**2)<=1
    return 4.*count/n

def withSticks(n = 1000, size = 10, linecount = 5, sticklength = 1):
    count = 0
    linedist = 1.*size/linecount
    linelist = []
    for x in range(linecount):
        linelist.append(x*linedist)
    for iter in range(n):
        x = random()
        x*=(size-sticklength)
        x+=(sticklength/2.)
        a = random()*2*pi
        x2 = x+sticklength*cos(a)
        for line in linelist:
            if (x<=line and x2>=line) or (x>=line and x2<=line): count += 1
    return 2.*sticklength*n/(linedist*count)

def gregoryLeibniz(n = 1000):
    tot = 0
    for x in range(1,n):
        if x%2:
            tot += 4./(2*x-1)
        else:
            tot -= 4./(2*x-1)
    return tot

def nilakantha(n = 1000):
    tot = 3
    for x in range(1,n):
        b = 2*x
        if x%2:
            tot += 4./(b*(b+1)*(b+2))
        else:
            tot -= 4./(b*(b+1)*(b+2))
    return tot

def chudnovsky(max = 10):
    tot = 0.0
    for k in range(max):
        tot += ((-1.)**k)*(factorial(6.*k))*(13591409+k*545140134.)/( factorial(3.*k)*((factorial(k))**3.)*640320.**(3.*k+1.5))
    tot *= 12
    tot = 1/tot
    return tot

#print withPoints()
#print withSticks()
#print gregoryLeibniz()
#print nilakantha(10000)
print chudnovsky()
print pi