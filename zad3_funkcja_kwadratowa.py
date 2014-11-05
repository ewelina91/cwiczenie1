'''
Created on 5 lis 2014

@author: Ewcia
'''

def funkcjakwadratowa(a,b,c,x):
    y=a*x**2+b*x+c
    return y
a=input("Podaj a:")
b=input("Podaj b:")
c=input("Podaj c:")
x=input("Podaj x:")
y=funkcjakwadratowa(a,b,c,x)
print ("Wartosc funkcji kwadratowej:"), y

from math import sqrt
delta = (b**2) - (4*a*c)
if delta < 0:
    print "Brak miejsc zerowych funkcji"
else:
    pdelta = sqrt(delta)
    print "Pierwiastek z delty wynosi:", pdelta
 
if delta < 0:
    print "Brak rozwiazan"
elif delta == 0:
    x = - b / 2 * a
    print "x rowna sie: ", x
else:
    x1 = (- b - sqrt (delta)) / 2 * a
    x2 = (- b + sqrt (delta)) / 2 * a
    print "x1 rowna sie:", x1, "x2 rowna sie:", x2
    
for i in xrange (-10,10):
    print str(i) + ": " + str(funkcjakwadratowa(1,1,-1,i))