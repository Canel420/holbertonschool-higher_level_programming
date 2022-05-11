#include "lists.h"

/**
 * print_dlistint - Print doubly linked list nodes
 *
 * @h: Pointer reference to head node.
 *
 * Description: Traverse a doubly linked list and prints each of
 * its nodes.
 *
 * Return: Amount of nodes.
 */

size_t print_dlistint(const dlistint_t *h)
{
	unsigned int i = 0;
	const dlistint_t *tmp = h;

	if (h == NULL)
		return (0);
	while (tmp != NULL)
	{
		printf("%d\n", tmp->n);
		i++;
		tmp = tmp->next;
	}
	return (i);
}
