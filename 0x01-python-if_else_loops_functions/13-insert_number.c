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
	int flag = 0;

	add = malloc(sizeof(listint_t));
	if (!add)
		return (NULL);
	add->n = number;
	current = *head;
	/*adding*/
	if (*head == NULL || (*head)->n) {
		add->next = *head;
		(*head) = add;
		return (*head);
	}
	else {
		current = *head;
		while (current->next != NULL)
		{
			if (number < (*head)->n)
			{
				flag = 1;
				break;
			}
			else if (current->next->n < number)
				break;
			current = current->next;
		}
		add->next = current->next;
		if (flag == 1) {
			(*head) = add;
			add->next = current->next;
		}
		else
			current->next = add;
	return (*head);
	}
}
