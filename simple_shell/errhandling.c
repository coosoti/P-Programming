#include "main.h"
#include <unistd.h>

/**
 * malloc_checkptr - check if return is NULL and exit if condition is met
 * @s: check null string
 */

void malloc_checkptr(char *s)
{
	if (s == NULL)
		exit(EXIT_FAILURE);
}

/**
 * malloc_checkdptr - check if return is NULL and exit if condition is met
 * @s: check null 2d string
 */

void malloc_checkdptr(char **s)
{
	if (s == NULL)
		exit(EXIT_FAILURE);
}

/**
 * getret - check for getline return value and EOF condition
 * @glob: struct of global variables
 * @ret: return of getline function
 */

void getret(ssize_t ret, myglob_t *glob)
{
	int i = 0, tracker = 0;

	if (ret < 0 || glob->lineptr == NULL)
	{
		free_alloced_mem_on_exit(glob);
		write(STDOUT_FILENO, "\n", 1);
		fflush(stdout);
		exit(glob->es);
	}
	else if (!isatty(STDIN_FILENO))
	{
		if (glob->lineptr[0] < 32)
		{
			free_alloced_mem_on_exit(glob);
			exit(glob->es);
		}
		while (glob->lineptr[i])
		{
			if (glob->lineptr[i] != 32 && glob->lineptr[i] != '\0' &&
			glob->lineptr[i] != '\n')
				tracker = 1;
			i++;
		}
			if (tracker == 0)
			{
				free_alloced_mem_on_exit(glob);
				exit(glob->es);
			}
	}
	else if (glob->lineptr[0] == '\0' && !isatty(STDIN_FILENO))
	{
		free_alloced_mem_on_exit(glob);
		exit(glob->es);
	}
}

/**
 * write_cmd_err - writes error output for commands not found in path
 * @glob: struct of global variables
 */


void write_cmd_err(myglob_t *glob)
{
	char *str = malloc(sizeof(char) * (count_digits(glob->ln) + 1));

	malloc_checkptr(str);
	to_string(glob->ln, str);

	write(STDERR_FILENO, glob->av, _strlen(glob->av));
	write(STDERR_FILENO, ": ", 2);
	write(STDERR_FILENO, str, _strlen(str));
	write(STDERR_FILENO, ": ", 2);
	write(STDERR_FILENO, glob->tokens[0], _strlen(glob->tokens[0]));
	write(STDERR_FILENO, ": not found", 11);
	write(STDERR_FILENO, "\n", 1);
	fflush(stderr);
	free(str);
}

/**
 * write_exec_err - writes error when execve fails.
 * @glob: struct of global variablesr
 */

void write_exec_err(myglob_t *glob)
{
	char *str = malloc(sizeof(char) * (count_digits(glob->ln) + 1));

	malloc_checkptr(str);
	to_string(glob->ln, str);

	write(STDERR_FILENO, glob->av, _strlen(glob->av));
	write(STDERR_FILENO, ": ", 2);
	write(STDERR_FILENO, str, _strlen(str));
	write(STDERR_FILENO, ": ", 2);
	fflush(stderr);
	free(str);
}
