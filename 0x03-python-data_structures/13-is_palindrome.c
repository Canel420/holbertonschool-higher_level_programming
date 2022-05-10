#include "lists.h"

/**
 * check_Pal - Recursive function to check if the linked list is a palindrome
 *
 * @left: Start node of the list
 * @right: End node of the list
 *
 * Description: Reaches the end of the linked list and compares if the
 * last node has the same value as the first node and so on.
 *
 * Return: Return 1 if palindrome
 *
 */

int check_Pal(listint_t **left, listint_t *right)
{
	int res;

	if (right == NULL)
		return (1);

	res = check_Pal(left, right->next) && ((*left)->n == right->n);
	(*left) = (*left)->next;

	return (res);
}

/**
 * is_palindrome - Function to check if the linked list is a palindrome
 *
 * @head: Reference to head node of list
 *
 * Description: Calls recursive function to check if palindrome
 *
 * Return: The call to the recursive function.
 */

int is_palindrome(listint_t **head)
{
	return (check_Pal(head, *head));
}
