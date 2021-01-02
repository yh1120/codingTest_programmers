def solution(numbers):
    tmp = list()
    k = 0
    for i in numbers:
        k += 1
        for j in numbers[k:]:
            tmp.append(i + j)
    return (sorted(list(set(tmp))))

numbers = [2,1,3,4,1]
answer = solution(numbers)
print(answer)
