#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *temp;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow = temp;
	}

	if (fast)
		slow = slow->next;

	while (slow)
	{
		if (prev->n != slow->n)
			is_palindrome = 1;
		temp = prev->next;
		prev->next = slow;
		slow = slow->next;
		prev->next->next = temp;
	}

	return (is_palindrome);
}
