# 자물쇠와 열쇠
def rotate_array(array):
    length = len(array)
    new_array = [([0] * length) for _ in range(length)]
    
    for i in range(length):
        for j in range(length):
            new_array[j][length - i - 1] = array[i][j]
    return new_array

def is_fit(key, lock, start, end, board_size, x, y):
    # 보드판 초기화
    board = [[0] * board_size for _ in range(board_size)]
    
    for i in range(len(key)):
        for j in range(len(key)):
            board[x + i][y + j] = key[i][j]
            
    for i in range(start, end):
        for j in range(start, end):
            board[i][j] += lock[i - start][j - start]
            if board[i][j] != 1:
                return False
            
    return True                    

def solution(key, lock):
    answer = False
    m = len(key)
    n = len(lock)
    start = m - 1
    end = start + n
    board_size = 2 * start + n
    
    for _ in range(4):
        for i in range(end):
            for j in range(end):
                if is_fit(key, lock, start, end, board_size, i, j):
                    return True
                # 총 4번까지 회전시키며 체크
        key = rotate_array(key)
        
    
    return answer