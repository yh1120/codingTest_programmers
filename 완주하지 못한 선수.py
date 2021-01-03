def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    completion.append("")
    for k in range(0,len(participant)):
        if participant[k] != completion[k]:
            return participant[k]


"""
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer)
    return list(answer.keys())[0]
"""


participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
answer = solution(participant, completion)
print("answer is :", answer)