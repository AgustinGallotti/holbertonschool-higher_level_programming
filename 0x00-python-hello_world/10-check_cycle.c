#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* test - test for check the node
* @nextnode: node next
* @nextnext: second next
* Return: yes or not
*/
int check_cycle(listint_t *list)
{
listint_t *nextnode = list, *nextnext = list;
	while (list != NULL && nextnode != NULL && nextnext != NULL)
	{
		nextnode = nextnode->next;
		nextnext = nextnext->next->next;
		if (nextnode == nextnext)
			return (1);
	}
	return(0);
}
