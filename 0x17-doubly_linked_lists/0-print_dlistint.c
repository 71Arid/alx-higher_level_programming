#include "lists.h"
/**
 * print_dlistint - prints dlist
 * @h: pointer to head node
 * Return: number of nodes
 */ 
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *new = h;
	int i = 0;

	while (new != NULL)
	{
		i++;
		new = new->next;
	}
	return i;
}
