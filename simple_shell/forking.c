#include "main.h"

/**
 * forking - function initializes forking the main process in order to...
 *             execute the standard commands in the child process.
 * @glob: struct of global variables.
 * @r: return of check_path() which determines if command exists
 */

void forking(int r, myglob_t *glob)
{
	pid_t fret;
	int status;

	if (r == 0)
	{
		fret = fork();
		if (fret < 0)
		{
			perror("fork");
			fflush(stderr);
			exit(EXIT_FAILURE);
		}
		else if (fret == 0)
			exct(glob);
		else
		{
			wait(&status);
			glob->es = wexitstat(status);
			free_alloced_mem_on_exit(glob);
		}
	}
	else
	{
		write_cmd_err(glob);
		glob->es = 127;
		free_alloced_mem_on_exit(glob);
	}
}
