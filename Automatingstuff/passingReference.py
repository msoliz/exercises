# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 10:54:42 2016

@author: Mark
"""

def eggs(someParameter):
    someParameter.append('Hello')
    
spam = [1, 2, 3]
eggs(spam)
print(spam)