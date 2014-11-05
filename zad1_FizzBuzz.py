'''
Created on 5 lis 2014

@author: Ewcia
'''
#Pierwsze rozwiazanie
def podzielna(n):
    for x in n:
        if not (x%15):
            print "Fizz Buzz"
        elif not (x%3):
            print "Fizz"
        elif  not (x%5):
            print "Buzz" 
        else:
            print x
zakres=range(1,100)
liczby=podzielna(zakres)

#Drugie rozwiazanie
liczba = input("Podaj n:")
for x in range(1,liczba):
    if not (x%15):
        print "Fizz Buzz"
    elif not (x%3):
        print "Fizz"
    elif not (x%5):
        print "Buzz"
    else:
        print x