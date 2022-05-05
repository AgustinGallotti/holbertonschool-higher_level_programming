#include "lists.h"
/*
* sum_dlistint - sum of lists
*
* Return: sum of the data
*/
int sum_dlistint(dlistint_t *head)
{
	dlistint_t *current;
	int data = 0;
	if (head == NULL)
		return (0);
	current = head;
	while (current != NULL)
	{
		data = data + current->n;
		current = current->next;
	}
	return (data);
}
