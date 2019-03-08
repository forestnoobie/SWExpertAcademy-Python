def invest(numlist):
    
    profit = 0

#    dropidx_list = []
#    upidx_list =[]
#    for idx, i in enumerate(numlist):
#        if idx !=0:
#            if numlist[idx-1]  > numlist[idx]:
#                dropidx_list.append(idx-1)
#            else :
#                upidx_list.append(idx-1)
                
                
    start_idx =0 
        
    while start_idx < len(numlist) :
        maxvalue = max(numlist[start_idx:])
        maxindex = numlist[start_idx:].index(maxvalue)
        #print("maxindex",maxindex)
        #print("startindex",start_idx)
        for idx in range(start_idx, start_idx + maxindex+1):
            profit += maxvalue - numlist[idx]
            
        start_idx = start_idx + maxindex + 1
            
    
    return profit

TT = int(input())

for _ in range(TT):
    total_length = int(input())
    numlist = list(map(int,input().split()))
    #print(total_length,numlist)
    
    result = invest(numlist)
    print("#{} {}".format(_+1,result))
    