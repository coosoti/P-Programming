#include "main.h"

/**
 * my_getline - Handles the main process for interactive mode
 * @av: vector of arguments passed to the program.
 */

void my_getline(char *av)
{
	int path_ret = 0;
	ssize_t getlin_ret = 0;
	size_t n = 0;
	myglob_t glob = {NULL, NULL, NULL, 0, 0, NULL};

	glob.av = av;

	while (1)
	{
		write(STDOUT_FILENO, "$ ", 2);
		fflush(stdout);

		getlin_ret = getline(&(glob.lineptr), &n, stdin);
		getret(getlin_ret, &glob);
		glob.ln++;

		if (glob.lineptr[0] == '\n' && glob.lineptr[1] == '\0')
			continue;
		if (glob.lineptr[getlin_ret - 1] == '\n')
			glob.lineptr[getlin_ret - 1] = '\0';
		else
			getlin_ret = getlin_ret + 1;
		glob.copy = malloc(sizeof(char) * getlin_ret);
		malloc_checkptr(glob.copy);
		str_cpy(glob.copy, glob.lineptr);
		glob.tokens = splitstr(glob.lineptr, glob.copy);
		malloc_checkdptr(glob.tokens);

		if (ch_builtin(&glob))
			continue;

		glob.es = 0;

		path_ret = check_path(glob.tokens[0]);
		forking(path_ret, &glob);

	}
}

/**
 * non_interactive_mode - Handles the main process for non-interactive mode
 * @av: vector of arguments passed to the program.
 */

void non_interactive_mode(char *av)
{
	int path_ret = 0;
	ssize_t getlin_ret = 0;
	size_t n = 0;
	myglob_t glob = {NULL, NULL, NULL, 0, 0, NULL};

	glob.av = av;

	while (1)
	{
		getlin_ret = getline(&(glob.lineptr), &n, stdin);
		if (glob.lineptr[0] == '\0')
		{
			free_alloced_mem_on_exit(&glob);
			exit(glob.es);
		}
		getret(getlin_ret, &glob);
		glob.ln++;

		if (glob.lineptr[getlin_ret - 1] == '\n')
			glob.lineptr[getlin_ret - 1] = '\0';
		else
			getlin_ret = getlin_ret + 1;

		glob.copy = malloc(sizeof(char) * getlin_ret);
		malloc_checkptr(glob.copy);
		str_cpy(glob.copy, glob.lineptr);
		glob.tokens = splitstr(glob.lineptr, glob.copy);
		malloc_checkdptr(glob.tokens);

		if (ch_builtin(&glob))
			continue;

		glob.es = 0;

		path_ret = check_path(glob.tokens[0]);
		forking(path_ret, &glob);

	}
}
