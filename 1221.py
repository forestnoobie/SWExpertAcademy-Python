## Anwser

TT = int(input())

for _ in range(1, TT + 1):

    N = int(input().split()[1])

    wor_list = list(map(str, input().split()))

    wor2num = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5,
               "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

    num2wor = {0: "ZRO", 1: "ONE", 2: "TWO", 3: "THR", 4: "FOR", 5: "FIV", 6:
        "SIX", 7: "SVN", 8: "EGT", 9: "NIN"}

    num_list = [wor2num[x] for x in wor_list]

    num_list = sorted(num_list)

    sorted_wor = [num2wor[x] for x in num_list]

    print("#{}".format(_), end=' ')
    for value in sorted_wor:
        print(value, end=' ')

## Test

f = open("C:/Users/Nakyilkim/Downloads/GNS_test_input.txt",'r')
lines = f.readlines()

T = lines[2]

board = []

f.close()

wor_list = [x for x in T[:-2].split(" ")]

wor2num = {"ZRO" : 0 , "ONE" : 1, "TWO" : 2, "THR":3, "FOR":4 ,"FIV" : 5,
           "SIX" : 6, "SVN": 7 , "EGT":8, "NIN":9}

num2wor = {0 : "ZRO" , 1:  "ONE" , 2 : "TWO", 3 : "THR", 4 : "FOR" , 5 :"FIV" , 6 :
           "SIX" , 7 : "SVN", 8: "EGT", 9 :  "NIN"}

num_list = [wor2num[x] for x in wor_list]

num_list = sorted(num_list)

sorted_wor = [num2wor[x] for x in num_list]

for value in sorted_wor:
    print(value, end=' ')