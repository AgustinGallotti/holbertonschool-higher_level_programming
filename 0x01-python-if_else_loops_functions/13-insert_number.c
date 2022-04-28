#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
* listint_t - we list
*
* Return: a new value in the list
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *add;

	add = malloc(sizeof(listint_t));
	if (!add)
		return (NULL);
	add->n = number;
	current = *head;
	if (*head == NULL || (*head)->n) {
		add->next = *head;
		(*head) = add;
		return (*head);
	}
	else {
		current = *head;
		while (current->next != NULL && current->next->n 
			< add->n) {
			current = current->next;
		}
		add->next = current->next;
		current->next = add;
		}
	return (*head);
}
