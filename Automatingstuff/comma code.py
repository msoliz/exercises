# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 11:03:00 2016

@author: Mark
"""

def oxfordComma(spamy):
    spamy.append('and')
    #oxfordComma.insert(-1, 'and ')
    
print('Enter list value: ')
value = input()  
spam = ['apples', 'bannanas', 'tofu', 'cats']
oxfordComma(spam)

