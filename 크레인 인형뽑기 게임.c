#include <stdio.h>

int		solution(int board[5][5], int *moves)
{
	int stack[1000] = {0, };
	int answer = 0;
	int k = 0;
	int move = 0;
	for (int i = 0; moves[i] != 0; i++)
		for (int j = 0; j < 5; j++)
			if (board[j][moves[i] - 1] > 0)
			{
				stack[k] = board[j][moves[i] - 1];
				board[j][moves[i] - 1] = 0;
				if (k > 0 && stack[k] == stack[k - 1])
				{
					answer++;
					stack[k] = 0;
				}
				printf("stack : %d, answer : %d\n",stack[k], answer);
				k++;
				break;
			}
	printf("\n");
	return (answer);
}

int		main(void)
{
	int board[5][5] = {
		{0,0,0,0,0},
		{0,0,1,0,3},
		{0,2,5,0,1},
		{4,2,4,4,2},
		{3,5,1,3,1}};
	int	moves[8] = {1,5,3,5,1,2,1,4};
	int answer = solution(board, moves);
	printf("%d", answer);
	return (0);
}
