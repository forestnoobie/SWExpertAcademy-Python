## Anwser
def cycle():
    global num_list
    copied_list = [x for x in num_list]

    flag = 0

    while flag != 1:
        copied_list = [x for x in num_list]
        for idx, num in enumerate(num_list):
            copied_list.remove(num)

            if num - idx - 1 > 0:
                copied_list.append(num - idx - 1)
            else:
                copied_list.append(0)
                flag = 1
                break

            if idx == 4: break

        num_list = copied_list

        if flag:
            break


for _ in range(10):
    TT = int(input())
    num_list = list(map(int, input().split()))
    cycle()
    print("#{} ".format(TT), end="")
    for x in num_list:
        print(x, end=" ")
    print()

## Test
num_list = [2419, 2418, 2423, 2415, 2422, 2419, 2420, 2415]
#num_list = [9550, 9556, 9550, 9553, 9558, 9551, 9551, 9551,]

## 한 사이클 다섯 번
def cycle():

    global  num_list
    copied_list = [x for x in num_list]

    flag = 0

    while flag != 1 :
        copied_list = [x for x in num_list]
        for idx, num in enumerate(num_list):
            copied_list.remove(num)

            if num  -idx - 1 >0:
                copied_list.append(num - idx - 1)
            else :
                copied_list.append(0)
                flag = 1
                break

            if idx ==  4 : break

        num_list = copied_list

        if flag:
            break

    print(num_list)

cycle()
