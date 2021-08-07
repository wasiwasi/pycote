# 가사 검색
from bisect import bisect_left, bisect_right

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

answer = []
array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

# 각 글자 수에 맞는 인덱스에 단어입력
for word in words:
    array[len(word)].append(word)
    reversed_array[len(word)].append(word[::-1])
for i in range(10001):
    array[i].sort()
    reversed_array[i].sort()

for querie in queries:
    length = len(querie)
    count = 0
    # 전부 와일드카드라면 temp의 갯수를 answer 배열에 추가
    if querie.count('?') == length:
        answer.append(len(array[length]))
    # 와일드카드가 접두라면
    elif querie[0] == '?':
        left_index = bisect_left(reversed_array[length],  querie[::-1].replace('?', 'a'))
        right_index = bisect_right(reversed_array[length], querie[::-1].replace('?', 'z'))
        answer.append(right_index - left_index)
    # 와일드카드가 접미라면
    elif querie[-1] == '?':
        left_index = bisect_left(array[length], querie.replace('?', 'a'))
        right_index = bisect_right(array[length], querie.replace('?', 'z'))
        answer.append(right_index - left_index)
print(answer)

# 효율성 1, 2, 3실패
# def bisearch_right(array, start, end):
#     # 접두가 와일드카드일 때 ?가 아닌 문자가 아닌 곳의 인덱스를 반환
#     mid = (start + end) // 2
#     if start > end:
#         return None
#     if array[mid] == '?':
#         if array[mid + 1] != '?':
#             return mid + 1
#         else:
#             return bisearch_right(array, mid + 1, end)
#     else:
#         return bisearch_right(array, start, mid - 1)
#     return -1

# def bisearch_left(array, start, end):
#     # 접미가 와일드카드일 때 가장 왼쪽의 ?의 인덱스를 반환함
#     mid = (start + end) // 2
#     if start > end:
#         return None
#     if array[mid] == '?':
#         if array[mid - 1] != '?':
#             return mid
#         else:
#             return bisearch_left(array, start, mid - 1)
#     else:
#         return bisearch_left(array, mid + 1, end)
#     return -1

# def solution(words, queries):
#     answer = []

#     for querie in queries:
#         temp = []
#         length = len(querie)
#         count = 0
#         # querie의 글자 수와 같은 길이의 단어만 넣은 temp배열 생성
#         for word in words:
#             if len(word) == length:
#                 temp.append(word)
#         # 전부 와일드카드라면 temp의 갯수를 answer 배열에 추가
#         if querie.count('?') == length:
#             answer.append(len(temp))
#         # 와일드카드가 접두라면
#         elif querie[0] == '?':
#             index = bisearch_right(querie, 0, length)
#             for word in temp:
#                 if querie[index:] == word[index:]:
#                     count += 1
#             answer.append(count)
#         # 와일드카드가 접미라면
#         elif querie[-1] == '?':
#             index = bisearch_left(querie, 0, length)
#             for word in temp:
#                 if querie[:index] == word[:index]:
#                     count += 1
#             answer.append(count)
#     return answer