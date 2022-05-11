#include "lists.h"

/**
 * free_dlistint - Free a doubly link list.
 *
 * @head: Pointer to the head node of list.
 *
 * Description: Frees a doubly link list.
 *
 */

void free_dlistint(dlistint_t *head)
{
	if (head == NULL)
		return;

	while (head)
	{
		dlistint_t *next = head->next;
		free(head);
		head = next;
	}
	return;
}
