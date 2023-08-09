#ifndef LISTS_H
#define LISTS_H

#include <stddef.h>

/**
 * struct listint_s - singly linked list
 * @n: integer value
 * @next: points to the next node
 *
 * Description: Structure for a singly linked list node.
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/**
 * print_listint - Prints all elements of a listint_t list.
 * @h: Pointer to the head of the list.
 * Return: Number of nodes in the list.
 */
size_t print_listint(const listint_t *h);

/**
 * add_nodeint - Adds a new node at the beginning of a listint_t list.
 * @head: Pointer to a pointer to the head of the list.
 * @n: Integer value to store in the new node.
 * Return: Address of the new element, or NULL on failure.
 */
listint_t *add_nodeint(listint_t **head, const int n);

/**
 * free_listint - Frees a listint_t list.
 * @head: Pointer to the head of the list to be freed.
 */
void free_listint(listint_t *head);

/**
 * check_cycle - Checks if a loop exists in a listint_t linked list.
 * @list: Pointer to the head of the list to be checked.
 * Return: 0 if no cycle, 1 if a cycle is present.
 */
int check_cycle(listint_t *list);

#endif /* LISTS_H */

