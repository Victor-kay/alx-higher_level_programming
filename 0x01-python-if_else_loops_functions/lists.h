#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - Structure for a singly linked list
 * @n: An integer value to store
 * @next: Pointer to the next node in the list
 *
 * Description: Defines the structure for a singly linked list node
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

/**
 * print_listint - Prints all elements of a linked list
 * @h: A pointer to the head of the linked list
 * Return: Number of nodes in the list
 */
size_t print_listint(const listint_t *h);

/**
 * add_nodeint_end - Adds a new node at the end of a linked list
 * @head: A pointer to a pointer to the head of the linked list
 * @n: An integer value to add to the new node
 * Return: Address of the new node, or NULL on failure
 */
listint_t *add_nodeint_end(listint_t **head, const int n);

/**
 * free_listint - Frees memory used by a linked list
 * @head: A pointer to the head of the linked list
 */
void free_listint(listint_t *head);

/**
 * insert_node - Inserts a new node at the correct position in a sorted list
 * @head: A pointer to a pointer to the head of the linked list
 * @number: An integer value to add to the new node
 * Return: Address of the new node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */

