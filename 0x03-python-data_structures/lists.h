#ifndef LISTS_H
#define LISTS_H
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

void append_nodes(listint_t **head, const int val);
listint_t *rev_list(listint_t *head);
int is_palindrome(listint_t **head);
void free_listint(listint_t *head);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
#endif /* LIST_H */
