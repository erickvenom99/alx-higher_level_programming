#include "lists.h"
/**
 * append_nodes - Appends a new node with the given value
* @head: Pointer to the head of the linked list
* @val: Value to be stored in the new node
*
* Return: None
*/
void append_nodes(listint_t **head, int val)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *last = *head;

	if (new_node == NULL)
	{
		return;
	}

	new_node->n = val;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return;
	}

	while (last->next != NULL)
	{
		last = last->next;
	}

	last->next = new_node;
}

/**
 * rev_list - Reverses a linked list
 * @head: Pointer to the head of the linked list
 *
 * Return: Pointer to the new head of the reversed linked list
 */
listint_t *rev_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * _palindrome - Checks if a linked list is a palindrome
 * @head: Pointer to the head of the linked list
 *
 * Return: 1 if the linked list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *reverse = rev_list(*head);
	listint_t *current = *head;

	while (current != NULL && reverse != NULL)
	{
		if (current->n != reverse->n)
		{
			return (0);
		}
		current = current->next;
		reverse = reverse->next;
	}

	return (1);
}
