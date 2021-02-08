#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <sys/wait.h>

/**
 * infinite_while - Infinite while loop.
 * Return: 0.
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
 * main - Create 5 zombie process and do an infinite loop
 * Return: Sucess
 */

int main(void)
{
	pid_t pid;
	int zomb = 0;

	while (zomb < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			zomb++;
		}
		else
			exit(0);
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
