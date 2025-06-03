import sys

n, m = map(int, sys.stdin.readline().split())
board = []

for _ in range(n):
    row = list(sys.stdin.readline().strip()) 
    board.append(row)

def search(x,y,board):
    countb = 0 #시작이 B인 경우 
    countw = 0 #시작이 W인 경우

    for i in range(8):
        for j in range(8):
            if (i+j)%2 ==0: #시작점이랑 같아야함
                if board[x+i][y+j] != 'W':
                    countw +=1
                if board[x+i][y+j] != 'B':
                    countb +=1
            else: #시작점이랑 달라야함
                if board[x+i][y+j] != 'W':
                    countb+=1
                if board[x+i][y+j] != 'B':
                    countw+=1

    return min(countb,countw)



min_count = 1e9
for i in range(n-7):
    for j in range(m-7):
        min_count = min(min_count, search(i,j,board))

print(min_count)