#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to list
 *
 * Return: 0 if its not a palindrome, 1 if it is
 */

int is_palindrome(listint_t **head)
{
	listint_t **my_head = *head;
	listint_t *temp = *head;
	int result = 1;

	if (*head == NULL || *head->next == NULL)
		return (result);
	if (temp->n == temp->next->n && temp->next->next == NULL)
		return (result);
}
