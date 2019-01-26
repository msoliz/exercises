# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 10:46:03 2016

@author: Mark
"""

myPets = ['Zophie', 'Pooka', 'nine-tail']
print('Enter a pet name: ')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')