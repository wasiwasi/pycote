#기둥과 보
def is_ok(answer):
    for x, y, structure in answer:
        if structure == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False
        elif structure == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        x, y, structure, op = frame
        if op == 0:
            answer.remove([x, y, structure])
            if not is_ok(answer):
                answer.append([x, y, structure])
        elif op == 1:
            answer.append([x, y, structure])
            if not is_ok(answer):
                answer.remove([x, y, structure])
    return sorted(answer)