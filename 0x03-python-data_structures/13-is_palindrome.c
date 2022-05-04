#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
* is_palindrome - is plaidrome
*
* @head: global
*
* return: if else
*/
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	unsigned int size = 0, i = 0, data[2048];

	if (head == NULL)
		return(0);

	if (*head == NULL)
		return(1);

	while (current != NULL)
	{
		current = current->next;
		size += 1;
	}
	if (size == 1)
		return(1);

	current = *head;

	while (current != NULL)
	{
		data[i++] = current->n;
		current = current->next;
	}

	for (i = 0; i <= (size / 2); i++)
	{
		if (data[i] != data[size - i - 1])
			return(0);
	}
	return(1);
}
