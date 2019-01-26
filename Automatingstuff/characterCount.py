# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 11:04:32 2016

@author: Mark
"""

message = 'It was a bright cold day in April, and the clocks were stricking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
    
print(count)