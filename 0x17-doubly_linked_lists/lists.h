#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * struct node - Structure for doubly linked list
 * @n: data
 * @next: Pointer to the next node
 * @prev: Pointer to previous node
 *
 * Description: Doubly linked list node structure
 */
typedef struct node
{
	int n;
	struct node *next;
	struct node *prev;
} dlistint_t;

size_t print_dlistint(const dlistint_t *h);


#endif /* LISTS_H */
