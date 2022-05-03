#include "lists.h"

/**
 * check_cycle - Finds a cycle in a singly linked list
 *
 * @list: Reference to head node of the list.
 *
 * Description: Compares the next pointer of a node with the next
 * pointer of the next node, if equal proves cycle existence.
 *
 * Return: 1 if cycle exists or 0 if it does not.
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
