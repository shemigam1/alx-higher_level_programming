#include "lists.h"

/**
 * insert_node - inserts a new node to a linked list
 * @head: double ptr to head
 * @number int
 * Return: adddress of new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new_node = NULL;

	if (*head == NULL)
		return NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return NULL;
	new_node->n = number;

	while (current->next != NULL)
	{
		if (number >= current->n && number < current->next->n)
		{
			listint_t *temp;

			temp = current->next;
			current->next = new_node;
			new_node->next = temp;
			return (new_node);
		}
		current = current->next;
	}
	if (current->next == NULL)
	{
		current->next = new_node;
		return (new_node);
	}
	return NULL;
}
