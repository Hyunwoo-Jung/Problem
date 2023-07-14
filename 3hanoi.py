# 3. 하노이의 탑
# 규칙 1) 크기가 다른 여러 원반이 있으며, 작은 원반 위에 큰 원반은 쌓을 수 없음
# 규칙 2) 원반을 놓을 수 있는 장소는 3군데이며, 처음에는 한 곳에 모두 쌓여 있음
# 규칙 3) 원반을 한 번에 하나씩 이동하녀 모든 원반을 다른 위치로 옮길 때의 횟수 조사

def hanoi(n, src,dist, via): # src : 현재 위치, dist : 이동 위치, via: 경유 장소
    if n > 1:
        hanoi(n - 1, src, via, dist) # n-1장을 현재 위치에서 경유 장소로 옮김
        print(src + ' -> ' + dist)
        hanoi(n - 1, via, dist, src) # n-1장을 경유 장소에서 이동 위치로 옮김
    else:
        print(src + ' -> ' + dist)

n = int(input())
hanoi(n, 'a', 'b', 'c')