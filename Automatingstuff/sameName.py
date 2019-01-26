# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 10:52:17 2016

@author: Mark
"""

def spam():
    eggs = 'spam local'
    print(eggs)     #prints 'spam local'
    
def bacon():
    eggs = 'bacon local'
    print(eggs)     #prints 'bacon local'
    spam()
    print(eggs)     #prints 'bacon local'

eggs = 'global'
bacon()
print(eggs)         #prints 'global'

    