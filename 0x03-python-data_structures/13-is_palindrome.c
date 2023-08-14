#include <stddef.h>

typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/**
 * is_palindrome - Check if a singly linked list is a palindrome.
 * @head: Pointer to the head of the linked list.
 * Return: 0 if not a palindrome, 1 if a palindrome.
 */
int is_palindrome(listint_t **head) {
    listint_t *slow = *head, *fast = *head;
    listint_t *prev_slow = NULL, *second_half = NULL;
    listint_t *mid_node = NULL;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return 1;

    // Find the middle of the linked list
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    // Handle odd length linked list
    if (fast != NULL) {
        mid_node = slow;
        slow = slow->next;
    }

    // Reverse the second half of the linked list
    second_half = slow;
    prev_slow->next = NULL;
    while (second_half != NULL) {
        listint_t *next_node = second_half->next;
        second_half->next = slow;
        slow = second_half;
        second_half = next_node;
    }

    // Compare the reversed second half with the first half
    while (slow != NULL) {
        if ((*head)->n != slow->n) {
            is_palindrome = 0;
            break;
        }
        (*head) = (*head)->next;
        slow = slow->next;
    }

    // Restore the original linked list
    prev_slow->next = mid_node;
    second_half = slow;
    slow = NULL;
    while (second_half != NULL) {
        listint_t *next_node = second_half->next;
        second_half->next = slow;
        slow = second_half;
        second_half = next_node;
    }
    return is_palindrome;
}
