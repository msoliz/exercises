# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:34:42 2016

@author: Mark
"""
def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result
        
print('Enter a number')

try: 
    n = int(input())    
except ValueError:
    print('Error: Please enter an integer')      
while n != 1:           # would 'while n != True: '  still work??
    n = collatz(int(n))
    
      
      









