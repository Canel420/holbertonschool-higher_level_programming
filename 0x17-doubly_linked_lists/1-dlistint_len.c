#include "lists.h"

/**
 * dlistint_len - Count doubly linked list nodes
 *
 * @h: Pointer reference to head node.
 *
 * Description: Traverse a doubly linked list and count each of
 * its nodes.
 *
 * Return: Amount of nodes.
 */

size_t dlistint_len(const dlistint_t *h)
{
	unsigned int i = 0;
	const dlistint_t *tmp = h;

	if (h == NULL)
		return (0);
	while (tmp != NULL)
	{
		i++;
		tmp = tmp->next;
	}
	return (i);
}
