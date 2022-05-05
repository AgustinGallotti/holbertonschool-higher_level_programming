#include "lists.h"
/**
* free-dlistint - free all nodes
* @header: head
*/
void free_dlistint(dlistint_t *head)
{
	dlistint_t *current, *nextnode;
	current = head;
	while (current != NULL)
	{
		nextnode = current->next;
		free(current);
		current = nextnode;
	}
}
