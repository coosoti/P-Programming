#include "main.h"

/**
 * _getenv - searches for environment variable in path and ...
 *           returns pointer to it's value.
 * @path: environment variable to search for
 * Return: address of value string
 *         NULL if variable does not exist.
 */

char *_getenv(char *path)
{
	char **env;
	size_t path_len;

	env = environ;
	path_len = _strlen(path);

	while (*env != NULL)
	{
		if (_strncmp(*env, path, path_len) == 0 && (*env)[path_len] == '=')
		{
			return (&((*env)[path_len + 1]));
		}
		env++;
	}

	return (NULL);
}
