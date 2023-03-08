#include "lists.h"
/**
  * check_cycle - checks for linked cycle
  * @list: pointer to liked list
  * Return: 1 if yes 0 if no
  */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	fast = slow = list;
	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (fast == slow)
			return (1);
	}
	return (0);
}
