#include "main.h"
#include <stdlib.h>

/**
 * handle_sigint - signal handler function
 * @sig: signal argument
 */

void handle_sigint(int __attribute__((unused))sig)
{
	signal(sig, SIG_IGN);
	write(STDOUT_FILENO, "\n$ ", 3);
	signal(sig, handle_sigint);
	fflush(stdout);
}

/**
 * main - handles the mode of the shell
 * @argc: argument count
 * @argv: argument vector
 *
 * Return: 0 Always
 */

int main(int __attribute__((unused))argc, char *argv[])
{
	if (argv[0] == NULL)
		exit(EXIT_FAILURE);

	signal(SIGINT, handle_sigint);
	if (!isatty(STDIN_FILENO))
		non_interactive_mode(argv[0]);
	else
		my_getline(argv[0]);

	return (0);
}
