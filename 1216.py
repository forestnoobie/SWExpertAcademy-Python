## Anwser
def check_horizontal(x, y):
    global count

    max_length = 100 - x
    global max_pal

    for length in range(2, max_length + 1):
        odd = length % 2
        stack = board[y][x:x + length // 2]
        start_idx = x + length // 2
        is_pal = True

        if odd:
            start_idx += 1

        assert len(board[y][start_idx: x + length]) == len(stack)

        for value in board[y][start_idx: x + length]:
            if value != stack.pop():
                is_pal = False
                break

        if is_pal:
            #   print("Found")
            #   print(board[y][x:x + length])

            if length > max_pal:
                max_pal = length
                # print(board[y][x:x + length])

        # print("Found",y,x)

    return True


## 세로 확인
def check_vertical(x, y):
    global count

    max_length = 100 - y
    global max_pal

    for length in range(2, max_length + 1):
        is_pal = True

        odd = length % 2

        stack = []

        for idx in range(y, y + length // 2):
            # print("index",idx)
            stack.append(board[idx][x])

        start_idx = y + length // 2

        if odd:
            start_idx += 1

        for idx in range(start_idx, y + length):
            value = board[idx][x]
            if value != stack.pop():
                is_pal = False

        if is_pal:
            if length > max_pal:
                max_pal = length
                # print([board[idx][x] for idx in range(y, y + length)])

            # print("Found", y, x)
    return True


for _ in range(1, 11):

    t = int(input())
    board = []

    for i in range(100):
        row = str(input())
        board.append([x for x in row])

    max_pal = 0
    for y in range(100):
        for x in range(100):
            check_horizontal(y, x)
            # print("Checking Vertically")
            check_vertical(y, x)

    print("#{} {}".format(_, max_pal))

## Test

f = open("C:/Users/Nakyilkim/Downloads/inputs.txt",'r')
lines = f.readlines()

T = lines[0]

board = []

for i in range(100):
    board.append([x for x in lines[i+i][:-1]])
f.close()


'''
board = []


tmp = "BCBBCACA BCAAACAC ABACBCCB AACBCBCA ACACBAAA ACCACCCB AACAAABA CACCABCB"

for row in tmp.split(" "):
    board.append([x for x in row])

board_length = 8

count = 0
'''

## 가로로 확인
def check_horizontal(x, y):
    global count

    max_length = 100 - x
    global max_pal

    for length in range(2, max_length + 1):
        odd = length % 2
        stack = board[y][x:x + length // 2]
        start_idx = x + length // 2
        is_pal = True

        if odd:
            start_idx += 1

        assert len(board[y][start_idx: x + length]) == len(stack)

        for value in board[y][start_idx: x + length]:
            if value != stack.pop():
                is_pal = False
                break


        if is_pal:
         #   print("Found")
         #   print(board[y][x:x + length])

            if length > max_pal:
                max_pal = length
                print(board[y][x:x + length])

        # print("Found",y,x)

    return True


## 세로 확인
def check_vertical(x, y):
    global count

    max_length = 100 - y
    global max_pal


    for length in range(2, max_length + 1):
        is_pal = True

        odd = length % 2

        stack = []

        for idx in range(y, y + length // 2):
            # print("index",idx)
            stack.append(board[idx][x])

        start_idx = y + length // 2

        if odd:
            start_idx += 1

        for idx in range(start_idx, y + length):
            value = board[idx][x]
            if value != stack.pop():
                is_pal = False

        if is_pal:
            if length > max_pal:
                max_pal = length
                print([board[idx][x] for idx in range(y, y + length)])


            # print("Found", y, x)
    return True


max_pal = 0

for y in range(100):
    for x in range(100):

        check_horizontal(y,x)
        #print("Checking Vertically")
        check_vertical(y,x)

if length == 1:
    count = count//2



