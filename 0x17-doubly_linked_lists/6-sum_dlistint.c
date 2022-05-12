#include "lists.h"

int sum_dlistint(dlistint_t *head)
{
	dlistint_t *node = head;
	dlistint_t *next;
	int sum = 0;

	if (head == NULL)
		return (0);

	while (node != NULL)
	{
		next = node->next;
		sum += node->n;
		node = next;
	}
	return (sum);
}
