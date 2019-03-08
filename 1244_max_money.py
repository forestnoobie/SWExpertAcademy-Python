# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:58:42 2019

@author: Nakyilkim
"""

### 재귀 + 완전 탐색으로 풀이

# 숫자 교환 조건
# 1. 숫자 교환하여 도달할 수 있는 최종 목표는
# list를 내림차순 정렬한 모양일 것으로 추정 (안 될 수도 있으나 비슷하게 가기는 함)
# 2. 원래 리스트의 가장 앞 자리수가 교환의 후보가 된다
# 3. 단 그 앞자리수가 정렬 리스트에 같은 자리수 숫자와 같으면 다음 자리로 이동
# 4. 교환 후보를 선정하면 원래 리스트에 가장 숫자가 큰 값의 인덱스를 찾는ㄷ
# 5. (여기서 중요) 가장 큰 값을 가지는 인덱스들과 교환을 하면서 재귀적으로 1을 반복한다


def listtonum(numlist):
    totalsum = 0
    for idx, i in enumerate(reversed(numlist)):
        totalsum +=  i * (10**idx)
     
     
    return totalsum
     
 
def Change_full(numList, TradeNum, realTrade=0):
     
    #print("Starting TradeNum",TradeNum)
    ## Base
    if TradeNum ==0:
 
        return listtonum(numList)
       
    sorted_list = sorted(numList, reverse=True)
#    indices = [i for i, x in enumerate(numList) if x == smallestidx]
 
    cand_idx = 0
     
    if sorted_list == numList:
      #  print("aligning Finished",numList)
         
        for num in numList:
            if numList.count(num) > 2:
        #        print("repeating number exist")    
                return listtonum(numList)
                break
             
        #print("No repeating number")
         
        if TradeNum%2:
            temp = numList[-2]
            numList[-2] = numList[-1]
            numList[-1] = temp
        return listtonum(numList)
     
    while sorted_list[cand_idx] == numList[cand_idx]:
         
       # print("sorted {}, num {}".format(sorted_list,numList))
        #print("Next cand",cand_idx)
        cand_idx += 1
         
 
     
    ## 가장 마지막 index랑 바꿔야 이 부분에 Max 필요
     
    temp = numList[cand_idx]
    swap_idx_list = [idx for idx, x in enumerate(numList) if x == sorted_list[cand_idx]]
     
    result =[]
    for swap_idx in swap_idx_list:
             
        #swap_idx = numList.index(sorted_list[cand_idx])
        numList[cand_idx]=sorted_list[cand_idx]
        numList[swap_idx]=temp
         
        result.append(Change_full(numList, TradeNum-1, realTrade=realTrade+1))
 
        numList[cand_idx]=temp
        numList[swap_idx]=sorted_list[cand_idx]        
         
         
    return max(result)
TT = int(input())
 
for _ in range(TT):
    numbers , tradingnum = map(int,input().split())
    numberlist = [int(x) for x in str(numbers)]
     
    result = Change_full(numberlist,tradingnum)
 
    print('#{} {}'.format(_+1,result))