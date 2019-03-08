N=1
M=1
K=2
A=1
B=1
Ntime = [5]
Mtime = [7]
Ktime = [7, 10]

K_num = [[None,None],[None,None]]

N_occupied = [False]
M_occupied = [False]
waiting_list = []


## 시작 고객 들어오는 시간

idx = 0
start = Ktime[idx]

## 서버가 비어는 서버 찾기
## 비어 있으면 바로 넣기

## 시간확인 비어 있는 창구 찾기
## 없으면 대기

def findN(N_occupied):
    
    for idx, i in enumerate(N_occupied) :
        if i == False:
            return idx
        
    return False


def findM(M_occupied):
    
    for idx, i in enumerate(M_occupied) :
        if i == False:
            return idx
    return False





time = 0
visited_receiption = [0] * K
visited_repair = [0] * K

receiption_desk = [[-1,-1] for _ in range(N)]
repair_desk = [[-1,-1,-1] for _ in range(M)]

# receiption_desk[i][0] = time// 접수를 받고 경과 시간
# receiption_desk[i][1] = customer number
 

receiption_q = []
repair_q = []

complete = [0] * K
using_desk = [[-1,-1] for _ in range(K)]

while True :
    for i in range(len(Ktime)):
        
        ## Waiting
        if Ktime[i] < time and visited_receiption[i] == 0 :
            visited_receiption[i] == 1 
            receiption_q.append(i)
        receiption_q.sort(reverse=True)    
    
        ## 창구 처리
        for i in range(N):
            if receiption_desk[i][0] >= 0:
                receiption_desk[i][0] += 1
                if receiption_desk[i][0] == Ntime[i]:
                    visited_repair[ receiption_desk[i][1]]
                    repair_q.append([0,i,receiption_desk[i][1]])
                    receiption_desk[i]= [-1,-1]
                    
        ## 정비 창구 시간
        for i in range(repair_q):
            repair_q[i][0] -= 1
        repair_q.sort(reverse=True)
        
        ## 장비 창구 처리
        for i in range(M):
            if repair_desk[i][0] >= 0:
                repair_desk[i][0] += 1
                if repair_desk[i][0] == Mtime[i]:
                    complete[repair_desk[i][2]] = 1
                    ## 리셉션 데스크와 리페어 데스크의 번호를 넣어준다
                    using_desk[repair_desk[i][2]] =  [repair_desk[i][1]+1,i+1]
                
            if repair_desk[i][0] == -1 :
                if repair_q:
                    customer_turn = repair_q.pop()
                    repair_desk[i] = [0, customer_turn[1],customer_turn[2]]
            
        
    
    time += 1
    if min(complete) > 0 :
        break
    
ans = 0
for i in range(K):
    if using_desk[i][0] == A and using_desk[i][1] ==B :
        ans += (i+1)
if ans > 0:
    print("#{} {}".format(testcase,ans))
else :
    print("#{} {}".format(testcase, -1))
