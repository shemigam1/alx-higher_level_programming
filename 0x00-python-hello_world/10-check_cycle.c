#include "lists.h"

/**
 * check_cycle - check if a singly linked list is circular
 * @list: ptr to list
 * Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL)
		return 0;
	slow = list;
	fast = list-> next;
	while (fast != NULL)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
