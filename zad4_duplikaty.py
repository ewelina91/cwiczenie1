'''
Created on 5 lis 2014

@author: Ewcia
'''
#Pierwsze rozwiazanie
def duplikaty(lista):
    wyjscie=[]
    for wyraz in lista: 
        if wyraz not in wyjscie:
            wyjscie.append(wyraz)
    return wyjscie
wyrazy=['kot', 'pies', 'chomik', 'kot', 'pies', 'pies', 'wydra']
wyjscie=duplikaty(wyrazy)
print wyjscie

#Drugie rozwiazanie
nazwy = ["kot", "pies", "chomik", "kot", "pies", "pies", "wydra", "okon"]
print "Wejscie:", nazwy
nazwy = list(set(nazwy))
print "Wyjscie:", (nazwy)
