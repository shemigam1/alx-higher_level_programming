#include "lists.h"

/**
 * check_cycle - check if a singly linked list is circular
 * @list: ptr to list
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list;

	if (head->next != NULL)
	{
		head = head->next;
	}
	else
	{
		return (0);
	}
	while (head != list)
	{
		if (head->next == NULL)
		{
			return (0);
		}
		head = head->next;
	}
	return (1);
}
