#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
/**
 * infinite_while - Creates an infinite loop
 * Return: Always returns 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - the entry point.
 * Return: always return 0 on sucess.
 */
int main(void)
{
	pid_t child_pid;
	char count = 0;

	while (count < 5)
	{
		child_pid = fork();
		if (child_pid < 0)
		{
			perror("Fork error");
			exit(EXIT_FAILURE);
		}
		else if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			count++;
		}
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
