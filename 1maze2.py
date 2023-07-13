# 1) 너비 우선 탐색으로 탐색

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

# 시작 위치(x좌표, y좌표, 이동 횟수)를 설정
pos = [[1,1,0]]

while len(pos) > 0:
    x, y, depth = pos.pop(0) # 리스트에서 탐색할 위치를 얻음

    # 목표에 도달하면 멈춤
    if maze[x][y] == 1:
        print(depth)
        break

    # 탐색 완료로 설정
    maze[x][y] == 2

    # 상하좌우 탐색
    if maze[x - 1][y] < 2:
        pos.append([x - 1, y, depth + 1]) # 이동 횟수를 늘려 왼쪽을 리스트에 추가
    if maze[x + 1][y] < 2:
        pos.append([x + 1, y, depth + 1]) # 이동 횟수를 늘려 오른쪽을 리스트에 추가
    if maze[x][y - 1] < 2:
        pos.append([x, y - 1, depth + 1]) # 이동 횟수를 늘려 위쪽을 리스트에 추가
    if maze[x][y + 1] < 2:
        pos.append([x, y + 1, depth + 1]) # 이동 횟수를 늘려 아래쪽을 리스트에 추가