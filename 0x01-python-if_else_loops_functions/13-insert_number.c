#include "lists.h"
#include <stdlib.h>
/**
  * insert_node - inserts node
  * @head: pointer to a linked list
  * @number: value in linked list
  * Return: address of new node
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return NULL;

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= new_node->n)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		listint_t *current = *head;
		while (current->next != NULL && current->next->n < new_node->n)
			current = current->next;
		new_node->next = current->next;
		current->next = new_node;
	}
	return new_node;
}
