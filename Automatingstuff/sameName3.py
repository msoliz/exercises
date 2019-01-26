# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 10:58:43 2016

@author: Mark
"""

def spam():
    global eggs
    eggs = 'spam'           #this is he global
def bacon():
    eggs = 'bacon'          #this is a local
def ham():
    print(eggs)             #this is the global

eggs = 42           #this is the global
spam()
print(eggs)
