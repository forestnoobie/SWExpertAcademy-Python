# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 15:05:35 2019

@author: Nakyilkim
"""

N = 4

board = [[9,8,9,8],
         [4,6,9,4],
         [8,7,7,8],
         [4,5,3,5]]

def check_duplicate(current_position, delta, path=[], right_down=0 , left_down=0 ,left_up=0, right_up=0):
    
    print("checking Duplicates")
    print("path",path)
    
    if right_down :
        for move in range(1,delta+1):
            num = board[current_position[0]+move][current_position[1]+move]
            if num in path:
                print('Duplication Found',num)
                return False
            path.append(num)
            
    elif left_down:
        for move in range(1,delta+1):
            
            num = board[current_position[0]+move][current_position[1]-move]
            
            if num in path:
                print('Duplication Found',num)
                return False
            if current_position[1]-move <0 :
                print("Out of Board")
                return False
            path.append(num)
    
    
    elif left_up : 
    	for move in range(1,delta+1):
            num = board[current_position[0]-move][current_position[1]-move]
            if num in path:
                print('Duplication Found',num)
                return False  
            if current_position[0]-move < 0 or current_position[1]-move < 0:
                print("Out of Board",num)
                return False
            path.append(num)
    elif right_up : 
    	for move in range(1,delta):
            num = board[current_position[0]-move][current_position[1]+move] 
            if num in path:
                return False  
            if current_position[0]-move < 0 :
                print("Out of Board")
                return False
            path.append(num)
    
    return path


#
#for i in range(N):
#    row = list(map(int,input().split()))
#    board[i] = row
#    
##


result = []


##for i in range(N):
#    for j in range(N):
#        if i == 0 and j ==0

for i in range(0,N-1):
    for j in range(1,N-1):
        
        print('='*10,i,j)

            ## Move right
        right_delta = min(N-j, N-i-1)
        right_cand = [i for i in range(1, right_delta)]
        print('right_cand',right_cand)
        
        path = []
        path.append(board[i][j])
        
        ## Move !
        for right in right_cand :
            print("Start Right",right)
            
            start = [i,j]
            new_path = []
            new_path.append(board[start[0]][start[1]])
            ## Check Dupilcate
            check =  check_duplicate(start,right, path = new_path, right_down=1)
            if check == False :
                continue
            elif check != False : 
                print("Else")
                new_path = check
            
            move_i = 0
            move_i = i + right
            
            move_j = 0
            move_j = j + right
            
            print("Moved Position 1",move_i,move_j)
            
            left_delta = min(move_j, N-move_i)
            left_cand =[i for i in range(1,left_delta)]
            
            print("left_cand",left_cand)
            
            for left in left_cand:
                new_path2 = []
                new_path2 = [x for x in new_path]
                
                print("Left",left,new_path2)
                
                check = check_duplicate([move_i,move_j],left, new_path2, left_down=1)
                
                if check == False :
                    continue
                elif check != False : 
                    new_path2 = check
                    
                move_i2 = 0
                move_i2 = move_i + left
                
                move_j2 = 0
                move_j2 = move_j - left
                
                print("Moved Position 2",move_i2,move_j2)
                
                check = check_duplicate([move_i2,move_j2], right, new_path2, left_up=1) 
            
                if check == False:
                    continue
                else : 
                    new_path2 = check
                    
                move_i3 = 0
                move_j3 = 0
                
                move_i3 = move_i2 - right
                move_j3 = move_j2 - right
                print("Moved Position 3",move_i3,move_j3)
                
                check = check_duplicate([move_i3,move_j3], left, new_path2, right_up=1) 
                if check == False:
                    continue
                else : 
                    new_path2 = check        
                    
                print("Path found",new_path2)
                print("Length", (right+left)*2)
                print("Length")
                result.append((right+left)*2)
              
        

if len(result) == 0 :
    print("",-1)
else :
    print("", max(result))
        

        
        ## 직사각형 완성
        
        
        ## 직사각형 완성
        ## 반대편도 check 해서 이상 없으면 총 길이 반환
        
    