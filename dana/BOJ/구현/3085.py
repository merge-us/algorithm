import sys
n = int(sys.stdin.readline())
board = []
for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))

# 색이 다른 인접한 두 칸 교환
# 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분 찾음
# 그 사탕의 수 최대 개수 갱신

dx = [-1,1,0,0]
dy = [0,0,-1,1]

max_cnt = 0

# 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분 찾음 
def search(board):

    global max_cnt

    #세로중에서 같은 색 몇개인지
    for i in range(n):
        count=1
        for j in range(1,n):
            if board[i][j]==board[i][j-1]:
                count+=1
            else:
                max_cnt=max(max_cnt,count)
                count=1
        max_cnt=max(max_cnt,count)
            

    #가로중에서 같은 색 몇개인지
    for j in range(n):
        count=1
        for i in range(1,n):
            if board[i][j]==board[i-1][j]:
                count+=1
            else:
                max_cnt=max(max_cnt,count)
                count=1
        max_cnt=max(max_cnt,count)


#모든 좌표에 대해서 오른쪽, 아래 좌표랑 비교해서 색이 다르면 교환
for x in range(n):
    for y in range(n):
        for d in (0,3):
            nx,ny = x+dx[d],y+dy[d]
            if 0<=nx<n and 0<=ny<n:
                if board[x][y] != board[nx][ny]:
                    #교환하고
                    board[x][y],board[nx][ny]=board[nx][ny],board[x][y]
                    #가장 긴 연속 부분 찾고
                    search(board)
                    #원상복구
                    board[x][y],board[nx][ny]=board[nx][ny],board[x][y]

            
print(max_cnt)