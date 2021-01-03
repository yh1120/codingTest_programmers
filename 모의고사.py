def solution(answers):
    answer = []
    num1 = 0
    num2 = 0
    num3 = 0
    for i in range(0, len(answers)):
        if (i % 5 + 1) == answers[i]:
            num1 += 1
        if i % 2 == 0 and answers[i] == 2:
            num2 += 1
        elif i % 8 == 1 and answers[i] == 1:
            num2 += 1
        elif i % 8 == 3 and answers[i] == 3:
            num2 += 1
        elif i % 8 == 5 and answers[i] == 4:
            num2 += 1
        elif i % 8 == 7 and answers[i] == 5:
            num2 += 1
        if (i % 10 == 0 or i % 10 == 1) and answers[i] == 3:
            num3 += 1
        elif (i % 10 == 2 or i % 10 == 3) and answers[i] == 1:
            num3 += 1
        elif (i % 10 == 4 or i % 10 == 5) and answers[i] == 2:
            num3 += 1
        elif (i % 10 == 6 or i % 10 == 7) and answers[i] == 4:
            num3 += 1
        elif (i % 10 == 8 or i % 10 == 9) and answers[i] == 5:
            num3 += 1
    if num1 >= num2 and num1 >= num3:
        answer.append(1)
    if num2 >= num1 and num2 >= num3:
        answer.append(2)
    if num3 >= num1 and num3 >= num2:
        answer.append(3)
    return answer

answers = [1,3,2,4,2]
ret = solution(answers)
print(ret)