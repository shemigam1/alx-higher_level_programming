#include "lists.h"

/**
 * check_cycle - check if a singly linked list is circular
 * @list: ptr to list
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *head = list;

	if (list == NULL)
		return (1);
	fast = head->next;
	while (fast != NULL && fast != head)
	{
		fast = fast->next;
	}
	return (fast == head)
}
