#include "lists.h"
#include <stddef.h>
/**
 * is_palindrome - checks for palindrome
 * @head: head of list
 * Return: 1 if palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *temp;
	int pali = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		temp = slow->next;
		slow->next = prev;
		prev = slow;
		slow= temp;
	}

	if (fast)
		slow = slow->next;

	while (slow)
	{
		if (prev->n != slow->n)
			pali = 0;
		temp = prev->next;
		prev->next = slow;
		slow = slow->next;
		prev->next->next = temp;
	}
	return (pali);
} 
