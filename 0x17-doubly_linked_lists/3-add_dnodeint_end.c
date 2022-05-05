#include "lists.h"
/**
* add_dnodeint_end - node in the tail
*
* 
* Return: new node at the tail
*/
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
    dlistint_t *new, *temp = *head;
	new = malloc(sizeof(dlistint_t));
    new->n = n;
	new->next = NULL;

	if (*head == NULL)
	{
		new->prev = NULL;
		*head = new;
		return (new);
	}
    while (temp->next != NULL)
	{
        temp = temp->next;
	}
	temp->next = new; /*las node of the linked list is temp*/
	new->prev = temp; /*assign new node to temp of head*/
    return (new);
}
