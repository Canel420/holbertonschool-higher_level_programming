#include "lists.h"

/**
 * add_dnodeint - Function to add a new node in a linked list
 *
 * @head: Pointer to ponter to head node of the list.
 * @n: integer data for the new node.
 *
 * Description: Adds a new node at the beggining of a doubly
 * linked lists.
 *
 * Return: Address to the new node
 *
 */

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	/* allocate new node space */
	dlistint_t *new_node = (dlistint_t *)malloc(sizeof(dlistint_t));

	if (new_node == NULL)
		return (NULL);

	/* Put in data */
	new_node->n = n;

	/* make next of new node as head and prevoius as NULL */
	new_node->next = (*head);
	new_node->prev = NULL;

	/* change prev of head node to new node */
	if ((*head) != NULL)
		(*head)->prev = new_node;

	/* move the head to point to the new node */
	(*head) = new_node;

	return (new_node);
}
