
# https://www.swexpertacademy.com/main/talk/solvingClub/boardCommuView.do?solveclubId=AV6kld8aisgDFASb&commuId=AV8UO_oqDEsDFAU0

TT = int(input())


def dfs(month, cost):
    global min_cost, cost_list
    global use_list

    # print(month,cost)

    ## Base Case
    if month > 11:
        if min_cost > cost:
            # print("min_cost",min_cost)
            min_cost = cost
        return

    ## 현재 이용 계획이 없으면 다음 달로 이동
    if use_list[month] == 0:
        dfs(month + 1, cost)
        return

    # 1일 이용권
    dfs(month + 1, cost + cost_list[0] * use_list[month])
    # 1달 이용권
    dfs(month + 1, cost + cost_list[1])
    # 3달 이용권
    dfs(month + 3, cost + cost_list[2])
    # 1년
    dfs(month + 12, cost + cost_list[3])


for _ in range(1, TT + 1):
    cost_list = list(map(int, input().split()))
    use_list = list(map(int, input().split()))
    min_cost = float('inf')
    dfs(0, 0)

    print("#{} {}".format(_, min_cost))

########## Test



cost_list = [10, 40, 100, 300]
use_list = [0, 0, 2, 9 ,1 ,5, 0, 0, 0, 0, 0, 0]

min_cost = float('inf')

## DFS
# 현재 구매할 달, 현재까지 비용

def dfs(month,cost):
    global min_cost

    print(month,cost)

    ## Base Case
    if month > 11 :
        if min_cost > cost :
            min_cost = cost
        return


    ## 현재 이용 계획이 없으면 다음 달로 이동
    if use_list[month] == 0 :
        dfs(month+1, cost)
        return

    # 1일 이용권
    dfs(month + 1 , cost + cost_list[0] * use_list[month])
    # 1달 이용권
    dfs(month + 1 , cost + cost_list[1])
    # 3달 이용권
    dfs(month + 3 , cost + cost_list[2])
    # 1년
    dfs(month + 12 , cost + cost_list[3])

