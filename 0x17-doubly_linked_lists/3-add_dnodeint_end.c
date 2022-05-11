#include "lists.h"

/**
 * add_dnodeint_end - Function to add a node at the end of a list.
 *
 * @head: Pointer to pointer to head node of list.
 * @n: Integer data for the new node.
 *
 * Description: Adds a node at the end of a doubly linked list.
 *
 * Return: Address to the new node.
 *
 */

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	/* alocate new node space */
	dlistint_t *new_node = (dlistint_t *)malloc(sizeof(dlistint_t));
	dlistint_t *last = *head; /* this is needed for a step ahead */

	if (new_node == NULL)
		return (NULL);
	/* put data into new node */
	new_node->n = n;

	/* This new node is going to be the last node */
	new_node->next = NULL;

	/* if the list is empty , then make the new node as head */
	if (*head == NULL)
	{
		new_node->prev = NULL;
		*head = new_node;
		return (new_node);
	}

	/* Else, traverse the list till the last current node */
	while (last->next != NULL)
		last = last->next;

	/* Change the next of the last node */
	last->next = new_node;

	/* Make last node as previous of new node */
	new_node->prev = last;

	return (new_node);
}
