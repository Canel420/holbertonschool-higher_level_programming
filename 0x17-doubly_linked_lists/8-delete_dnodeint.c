#include "lists.h"

/**
 * delete_dnodeint_at_index - Delete a node in a given position
 *
 * @head: Pointer to poointer of head node.
 * @index: Node position for deletion
 *
 * Description: Deletes a doubly linked list node at a given position.
 *
 * Return: 1 is succed or -1 if not.
 *
 */

int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *delete = *head;
	unsigned int i;

	if (*head == NULL)
		return (-1);

	/* Traverse up to the node at position n */
	for (i = 0; delete != NULL && i < index; i++)
		delete = delete->next;

	/* if index is greater then the number of nodes */
	if (delete == NULL)
		return (-1);
	/* If node to delete is head change head reference to next node */
	if (*head == delete)
		*head = delete->next;
	if (delete->next != NULL)
		delete->next->prev = delete->prev;
	if (delete->prev != NULL)
		delete->prev->next = delete->next;

	free(delete);
	return (1);
}
