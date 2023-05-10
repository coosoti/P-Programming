#include "main.h"

/**
 * splitstr - function splits string in tokens.
 * @line: line pointer to command line string
 * @linecopy: pointer to copy of line ptr
 *
 * Return: 2d array of tokens
 */

char **splitstr(char *line, char *linecopy)
{
	char *token;
	char *delim = " \n";
	char **tokenarray;
	unsigned int tokencount = 0;
	int i = 0;

	if (line == NULL || linecopy == NULL)
		return (NULL);
	token = strtok(line, delim);
	tokencount++;

	while (token != NULL)
	{
		token = strtok(NULL, delim);
		tokencount++;
	}
	tokenarray = malloc(sizeof(char *) * tokencount);
	if (tokenarray == NULL)
		return (NULL);

	token = strtok(linecopy, delim);
	for (i = 0; token != NULL; i++)
	{
		tokenarray[i] = malloc(sizeof(char) * (_strlen(token) + 1));
		if (tokenarray[i] == NULL)
		{
			free_tokens(tokenarray);
			return (NULL);
		}

		str_cpy(tokenarray[i], token);
		token = strtok(NULL, delim);
	}
	tokenarray[i] = NULL;

	return (tokenarray);
}

