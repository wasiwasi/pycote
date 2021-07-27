# 문자열 압축
def solution(s):
    answer = len(s)
    half_length = len(s) // 2
    array = [0] * (half_length + 1)
    
    for scale in range(1, half_length + 1):
        length = len(s)
        index = scale
        criteria = s[0:scale]
        overlap = 1
        
        while index <= len(s):
            if s[index:index + scale] == criteria:
                length -= scale
                index += scale
                # 중복이면 숫자한칸추가
                overlap += 1
            else:
                criteria = s[index:index + scale]
                index += scale
                if overlap > 1:
                    length += len(str(overlap))
                    overlap = 1
        if length < answer:
            answer = length
        
    
    return answer