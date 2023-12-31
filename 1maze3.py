# 2) 깊이 우선 탐색으로 탐색

maze = [[9,9,9,9,9,9,9,9,9,9,9,9], 
        [9,0,0,0,9,0,0,0,0,0,0,9], 
        [9,0,9,0,0,0,9,9,0,9,9,9], 
        [9,0,9,9,0,9,0,0,0,9,0,9], 
        [9,0,0,0,9,0,0,9,9,0,9,9], 
        [9,9,9,0,0,9,0,9,0,0,0,9], 
        [9,0,0,0,9,0,9,0,0,9,1,9], 
        [9,0,9,0,0,0,0,9,0,0,9,9], 
        [9,0,0,9,0,9,0,0,9,0,0,9], 
        [9,0,9,0,9,0,9,0,0,9,0,9], 
        [9,0,0,0,0,0,0,9,0,0,0,9], 
        [9,9,9,9,9,9,9,9,9,9,9,9]]

# 우수법에서의 이동 방향(하, 우, 상, 좌) 설정
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# 시작 위치(x좌표, y좌표, 이동 횟수, 방향)설정
x, y, depth, d = 1, 1, 0, 0

while maze[x][y] != 1:
    # 탐색 완료로 설정
    maze[x][y] = 2

    #우수법으로 탐색
    for i in range(len(dir)): # 이동 방향의 개수로 나눠 나머지를 구해서 다음 방향을 결정
        # 진행 방향의 오른쪽부터 순서대로 탐험
        j = (d + i - 1) % len(dir)
        if maze[x + dir[j][0]][y + dir[j][1]] < 2:
            # 방문하지 않은 경우에는 진행하여 이동 횟수를 늘림
            x += dir[j][0]
            y += dir[j][1]
            d = j
            depth += 1
            break
        elif maze[x + dir[j][0]][y + dir[j][1]] == 2:
            # 이미 방문한 경우에는 진행하여 이동 횟수를 줄임
            x += dir[j][0]
            y += dir[j][1]
            d = j
            depth -= 1
            break

print(depth)