### Anwser
# original code : https://2heedu.tistory.com/62

class magnetic():

    def __init__(self, length, board):
        self.len = length
        self.board = board
        self.count = 0

    def make_empty_board(self):
        tmp_board = [[0 for i in range(self.len)] for j in range(self.len)]
        return tmp_board

    def move(self):

        board = self.board
        count = self.count

        for col in range(self.len):
            for row in range(self.len):
                if board[row][col] == 2:
                    board[row][col] = 0
                elif board[row][col] == 1:
                    break
            for row in reversed(range(self.len)):
                if board[row][col] == 1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    break

        for col in range(self.len):

            flag = 0

            for row in range(self.len):
                if board[row][col] == 1:
                    if flag == 0: flag = 1

                elif board[row][col] == 2:
                    if flag == 1:
                        flag = 0
                        count += 1
        self.board = board
        self.count = count


for _ in range(1, 11):
    length = int(input())

    board = [[0 for i in range(length)] for j in range(length)]

    for i in range(length):
        board[i] = list(map(int, input().split()))

    mag = magnetic(length, board)

    mag.move()

    print('#{} {}'.format(_, mag.count))

### Test
length = 7
board = [[1, 0, 2, 0, 1, 0, 1],
         [0, 2, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 1, 0],
         [0, 0, 0, 0, 1, 2, 2],
         [0, 0, 0, 0, 0, 1, 0],
         [0, 0, 2, 1, 0, 2, 1],
         [0, 0, 1, 2, 2, 0, 2]]


class magnetic():

    def __init__(self,length,board):
        self.len = length
        self.board = board
        self.count = 0

        red_list = []
        blue_list = []
        stuck_dict = {}
        #
        # for i in range(length):
        #     board[i] = list(map(int, input().split()))
        #     for idx, value in enumerate(board[i]):
        #         if value == 1:
        #             red_list.append([i, idx])
        #         elif value == 2:
        #             blue_list.append([i, idx])

        for i in range(length):
            for idx, value in enumerate(board[i]):
                if value == 1:
                    red_list.append([i, idx])
                elif value == 2:
                    blue_list.append([i, idx])
        self.red_list = red_list
        self.blue_list = blue_list
        self.stuck_dict = stuck_dict

    def make_empty_board(self):
        tmp_board = [[0 for i in range(self.len)] for j in range(self.len)]
        return tmp_board

    def move(self):

        board = self.board
        count = self.count

        for col in range(self.len):
            for row in range(self.len):
                if board[row][col] == 2: board[row][col] = 0
                elif board[row][col] == 1 : break
            for row in reversed(range(self.len)):
                if board[row][col] == 1 : board[row][col] = 0
                elif board[row][col] == 2: break

        for col in range(self.len):

            flag = 0

            for row in range(self.len):
                if board[row][col] == 1:
                    if flag == 0 : flag = 1

                elif board[row][col] ==2 :
                    if flag == 1 :
                        flag = 0
                        count +=1
        self.board = board
        self.count = count


    def print_board(self):
        for row in self.board:
            print(row)
        print('Count',self.count)


