# 미니맥스 알고리즘으로 평가

goal = [0b111000000, 0b000111000, 0b000000111, 0b100100100, 
        0b010010010, 0b001001001, 0b100010001, 0b001010100]

# o나 x 3개가 나열되었는지 판정
def check(player):
    for mask in goal:
        if player & mask == mask:
            return True
    return False

# 미니맥스 알고리즘
def minmax(p1, p2, turn):
    if check(p2):
        if turn: # 자신의 턴일 경우에는 승리
            return 1
        else: # 상대의 턴일 경우에는 패배
            return -1
    
    board = p1 | p2
    if board == 0b111111111: # 칸이 다 찼다면 무승부
        return 0
    
    w = [i for i in range(9) if (board & (1 << i)) == 0]
    if turn: # 자신의 턴일 경우에는 최소값을 선택
        return min([minmax(p2, p1 | (1 << i), not turn) for i in w])
    else: # 상대의 턴일 경우에는 최대값을 선택
        return max([minmax(p2, p1 | (1 << i), not turn) for i in w])

# 번갈아두기
def play(p1, p2, turn):
    # o나 x 3개가 나열되었으면 출력해서 종료
    if check(p2):
        print([bin(p1), bin(p2)])
        print('o나 x 3개가 나열되었습니다.')
        return
    
    board = p1 | p2
    # 모든 칸에 o나 x를 다 놓으면 무승부로 종료
    if board == 0b111111111:
        print([bin(p1), bin(p2)])
        print('무승부입니다.')
        return
    
    # 둘 칸 찾기
    w = [i for i in range(9) if (board & (1 << i)) == 0]
    # 각 위치에 두었을 때의 평가값 확인
    r = [minmax(p2, p1 | (1 << i), True) for i in w]
    # 평가값이 가장 높은 곳을 얻음
    j = w[r.index(max(r))]
    play(p2, p1 | (1 << j), not turn)

play(0, 0, True)