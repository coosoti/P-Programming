#include "main.h"

/**
 * exct - function utilises execve() to execute standard commands in path
 * @glob: struct of global variables.
 */

void exct(myglob_t *glob)
{
	int exe_ret;
	char *cmd;
	int exct_exit = EXIT_FAILURE;

	cmd = find_path(glob->tokens[0]);
	if (cmd == NULL)
	{
		free(glob->lineptr);
		free(glob->copy);
		free_tokens(glob->tokens);
		glob->lineptr = NULL, glob->copy = NULL, glob->tokens = NULL;
		_exit(exct_exit);
	}

	exe_ret = execve(cmd, glob->tokens, environ);
	if (exe_ret == -1)
	{
		write_exec_err(glob);
		perror(glob->tokens[0]);
		fflush(stderr);
		free(glob->lineptr);
		free(glob->copy);
		free_tokens(glob->tokens);
		glob->lineptr = NULL, glob->copy = NULL, glob->tokens = NULL;

		if (errno == EACCES)
		{
			exct_exit = 126;
		}

		_exit(exct_exit);
	}
}
