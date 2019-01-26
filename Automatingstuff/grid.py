# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 09:35:44 2016

@author: Mark
"""


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
        

for i in range (len(grid[0])):
    for n in range (len(grid)):
        print(grid[n][i],end='')
    
    print()

