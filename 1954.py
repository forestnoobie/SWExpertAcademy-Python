TT = int(input())

for _ in range(1, TT + 1):
    N = int(input())
    numbers = [i for i in range(1, N * N + 1)]
    board = [[0 for i in range(N)] for j in range(N)]

    ## Recursive 인듯
    # index 에러 날 때까지 가다가 시계 반대 방향으로 바꾸기
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    ## 방향을 바꿀 때 인덱스 에러이거나 0이 아닐 때

    start_idx = [0, 0]
    turn = 0
    count = 0
    current_direction = directions[turn % 4]

    idx = start_idx

    for i in range(N * N):
        # print('Current idx',idx)
        ## Change Current Value
        board[idx[0]][idx[1]] = numbers[count]

        ## Next index
        next_idx = [idx[0] + current_direction[0], idx[1] + current_direction[1]]

        ## Check index , if its value != 0 , not out of index
        ## if its out of index change direction

        if next_idx[0] > N - 1 or next_idx[1] > N - 1:
            # print('Idx our of range, Changing directions')
            turn += 1
            current_direction = directions[turn % 4]
            next_idx = [idx[0] + current_direction[0], idx[1] + current_direction[1]]
        else:
            if board[next_idx[0]][next_idx[1]] != 0:
                #  print('Value != 0')
                turn += 1
                current_direction = directions[turn % 4]
                next_idx = [idx[0] + current_direction[0], idx[1] + current_direction[1]]

        idx = next_idx
        count += 1
        # print("Change idx",idx)

    print('#{}'.format(_))
    for row in board:
        for value in row:
            print(value, end=' ')
        print()
