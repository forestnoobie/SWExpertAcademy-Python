# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:51:51 2019

@author: Nakyilkim
"""

## Recursive

result_dict = {}
result_path = []

def solve(start, left=4, combine=[]):
    
    path = combine
    print("start , left, path",start, left,path)
    ## Base Case
    if left == 0 and start != 0:
        print("Failed")
        return 
    if start ==0 :
        
        print("Sucess")

        tmp_path = str(sorted(path, reverse = True))
        
        if tmp_path not in result_dict.keys():
            result_dict[tmp_path] = 1
        return 
    
    square_list = []

    for i in reversed(range(int(start**(0.5))+1)):
        square_list.append(i**2)
    
    for square in square_list[:-1]:
        #print("square",square)
        jump = start - square
        #print(jump)
        path.append(square)
        result = solve(jump, left-1, combine=path)
        
        if result :
            tmp_key = str(sorted(result, reverse = True))
            
            if tmp_key not in result_dict.keys():
                result_dict[tmp_key] = 1
        
        path.pop()
                
        
        
