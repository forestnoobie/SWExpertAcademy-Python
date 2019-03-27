## Anwser

TT = int(input())


def search(now, picked=[]):
    global min_tower, num_list

    heights = [num_list[x] for x in picked]
    ## Base
    if sum(heights) >= B:
        if sum(heights) < min_tower:
            min_tower = sum(heights)
        # print(heights)
        return
    if len(picked) == N:
        return

    if len(picked) == 0:
        smallest = -1
    else:
        smallest = picked[-1]

    # print("Startinc",picked)

    # Search
    for idx, v in enumerate(num_list):
        if idx > smallest:
            picked.append(idx)
            search(idx, picked)
            picked.pop()


for _ in range(TT):
    N, B = map(int, input().split())
    num_list = list(map(int, input().split()))
    min_tower = float('inf')
    search(0)
    print("#{} {}".format(_ + 1, min_tower - B))

### Test
## Min Max
N = 5
B = 16
num_list = [1,3,3,5,6]

## 완탐을 한다 하지만 16이상이거나 숫자가 없으면 종료

min_tower = float('inf')

def search(now,picked=[]):

    global min_tower, num_list


    heights = [num_list[x] for x in picked]
    ## Base
    if sum(heights) >=16 :
        if sum(heights) < min_tower:
            min_tower = sum(heights)
        #print(heights)
        return
    if len(picked) == N:
        return

    if len(picked) == 0 :
        smallest = -1
    else :
        smallest = picked[-1]

    #print("Startinc",picked)

    # Search
    for idx, v in enumerate(num_list):
        if idx > smallest :
            picked.append(idx)
            search(idx,picked)
            picked.pop()

search(0)
print(min_tower-B)