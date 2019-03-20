## Anwser

for t in range(1, 11):

    length = int(input())

    board = []

    for _ in range(8):
        row = str(input())
        board.append([x for x in row])
        # board([x for x in row])

    board_length = 8

    count = 0

    ## 가로로 확인
    def check_horizontal(x, y):
        global count

        max_length =

        ## X가 범위 안에 있어야 없으면 return
        if x > board_length - length or y > board_length - 1:
            return False

        odd = length % 2
        stack = board[y][x:x + length // 2]
        start_idx = x + length // 2

        if odd:
            start_idx += 1

        for value in board[y][start_idx: x + length]:
            if value != stack.pop():
                return False
        # print("Found",y,x)
        # print(board[y][x:x+length])

        count += 1

        return True


    ## 세로 확인
    def check_vertical(x, y):
        global count

        ## X가 범위 안에 있어야 없으면 return
        if y > board_length - length or x > board_length - 1:
            return False

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
                return False
        count += 1
        # print("Found", y, x)
        # print([board[idx][x] for idx in range(y, y+length) ])
        return True


    for y in range(8):
        for x in range(8):
            check_horizontal(y, x)
            # print("Checking Vertically")
            check_vertical(y, x)

    if length == 1:
        count = count // 2

    print("#{} {}".format(t, count))

## Test
length =1

board = []

tmp ='CBBCBAAB CCCBABCB CAAAACAB BACCCCAC AABCBBAC ACAACABC BCCBAABC ABBBCCAA'

tmp = "BCBBCACA BCAAACAC ABACBCCB AACBCBCA ACACBAAA ACCACCCB AACAAABA CACCABCB"

for row in tmp.split(" "):
    board.append([x for x in row])

board_length = 8

count = 0

## 가로로 확인
def check_horizontal(x,y):
    global count

    ## X가 범위 안에 있어야 없으면 return
    if x > board_length - length or y > board_length -1  :
        return False

    odd = length%2
    stack = board[y][x:x+length//2]
    start_idx = x + length // 2

    if odd :
        start_idx += 1

    for value in board[y][start_idx: x + length]:
        if value != stack.pop():
            return False
    print("Found",y,x)
    print(board[y][x:x+length])

    count += 1

    return True

## 세로 확인
def check_vertical(x,y):
    global count

    ## X가 범위 안에 있어야 없으면 return
    if y > board_length - length or x > board_length - 1:
        return False

    odd = length % 2

    stack = []

    for idx in range(y, y + length//2):
        #print("index",idx)
        stack.append(board[idx][x])

    start_idx = y + length // 2

    if odd:
        start_idx += 1

    for idx in range(start_idx,y+length):
        value = board[idx][x]
        if value != stack.pop():
            return False
    count += 1
    print("Found", y, x)
    print([board[idx][x] for idx in range(y, y+length) ])
    return True


for y in range(8):
    for x in range(8):

        check_horizontal(y,x)
        #print("Checking Vertically")
        check_vertical(y,x)

if length == 1:
    count = count//2



