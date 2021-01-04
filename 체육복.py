import collections

def solution(n, lost, reserve):
    answer = list(range(1, n + 1))
    answer = collections.Counter(answer) - collections.Counter(lost) + collections.Counter(reserve)
    print(answer)
    return answer

n = 5
lost = [2, 4]
reserve = [1, 3, 5]
answer = solution(n, lost, reserve)
print(answer)