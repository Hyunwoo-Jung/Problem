# n퀸 문제
# 체스판에 n개의 퀸을 서로 위협되지 않도록 배치하는 문제

N = 13 # N값만 바꾸면 됨

# 대각선 확인
def check(x, col):
    # 배치 완료된 행을 반대 순서로 탐색
    for i, row in enumerate(reversed(col)):
        if (x + i + 1 == row) or (x - i - 1 == row): # 왼쪽 위와 왼쪽 아래에 있는가
            return False
    return True

def search(col):
    if len(col) == N: # 전부 배치되면 출력
        print(col)
        return
    
    for i in range(N):
        if i not in col: # 동일한 행은 사용하지 않음
            if check(i, col):
                col.append(i)
                search(col)
                col.pop()

search([])