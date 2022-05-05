#include "lists.h"
/*
* get_dnodeint_at_index - find n'th
*
* Return: new node at idx
*/
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *current;
	unsigned int count = 0;
	
	current = head;

	if (current == NULL)
		return (NULL);
	while (current != NULL)
	{
		if (count == index)
		{
			return (current);
		}
		count++;
		current = current->next;
	}
	return (current);
}
