#include "lists.h"

/**
 * check_cycle - check if a singly linked list is circular
 * @list: ptr to list
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (list == NULL)
		return (0);
	do {
		if (fast == NULL || fast->next == NULL)
		{
			return (0);
		}
		slow = slow->next;
		fast = fast->next->next;
	} while (slow != fast);
	return (1);
}
