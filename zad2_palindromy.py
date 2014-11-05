'''
Created on 5 lis 2014

@author: Ewcia
'''

def odwrocony(tekst):
    return tekst[::-1]

def palindrom(tekst):
    return tekst == odwrocony(tekst)
 
napis = raw_input('Wprowadz napis: ')
if palindrom(napis):
    print "True"
else:
    print "False"
