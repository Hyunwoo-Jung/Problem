# 5. 틱택토
# 3X3칸에 O와 X를 번갈아 쓰며, 가로/세로 혹은 대각선상에 같은 모양 3개를 늘여놓으면 이기는 게임
import random

goal = [0b111000000, 0b000111000, 0b000000111, 0b100100100, 
        0b010010010, 0b001001001, 0b100010001, 0b001010100]

# o나 x 3개가 나열되었는지 판정
def check(player):
    for mask in goal:
        if player & mask == mask:
            return True
    return False

# 번갈아두기
def play(p1, p2):
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

    # 무작위로 두기
    r = random.choice(w)
    play(p2, p1 | (1 << r))

play(0, 0)