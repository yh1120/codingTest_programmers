def solution(board, moves):
    ans = 0
    stack = list()
    k = 0
    for i in range(len(moves)):
        for j in range(len(board[0])):
            if board[j][moves[i] - 1] > 0:
                stack.append(board[j][moves[i] - 1])
                board[j][moves[i] - 1] = 0
                if (k > 0 and stack[k] == stack[k - 1]):
                    ans += 2
                    stack.pop()
                    stack.pop()
                    k -= 2
                k += 1
                break
    return ans

board = [[0,0,0,0,0,0],
         [0,0,1,0,3,0],
         [0,2,5,0,1,3],
         [4,2,4,4,2,1],
         [3,5,1,3,1,4],
         [1,1,1,1,1,1]]
moves = [1,5,6,3,5,1,6,2,1,4]
answer = 0

answer = solution(board, moves)
print(answer)
