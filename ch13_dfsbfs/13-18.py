# 괄호 변환

def is_correct(p):
    temp = []
    for letter in p:
        if letter == '(':
            temp.append(letter)
        else:
            if temp:
                temp.pop()
            else:
                return False
    return True

def sort_braket(w):
    left_b = 0
    right_b = 0
    if is_correct(w):
        return w
    for i, letter in enumerate(w):
        if letter == '(':
            left_b += 1
        else:
            right_b += 1
        if left_b == right_b:
            u = w[:i + 1]
            v = w[i + 1:]
            break
    if is_correct(u):
        return u + sort_braket(v)
    else:
        new_str = '(' + sort_braket(v) + ')'
        tail = ''
        for u_letter in u[1:-1]:
            if u_letter == '(':
                tail += ')'
            else:
                tail += '('
        new_str += tail
    return new_str
                

def solution(p):
    answer = ''
    answer = sort_braket(p)
    return answer