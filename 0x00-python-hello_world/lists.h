#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - Node of a singly linked list
 * @n: integer data in the node
 * @next: points to the next node in the list
 *
 * Description: singly linked list node structure
 * Each node holds an integer value (@n) 
 * and a reference to the next node (@next).
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
