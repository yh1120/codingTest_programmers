def solution(participant, completion):
    participant = sorted(participant)
    completion = sorted(completion)
    completion.append("")
    for k in range(0,len(participant)):
        if participant[k] != completion[k]:
            return participant[k]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
answer = solution(participant, completion)
print("answer is :", answer)