# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:18:40 2016

@author: Mark
"""

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]            #list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)
    

    