#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts node into sorted list
 * @head: double pointer to head
 * @number: data number to be inserted
 * Return: on success, new node of address
 * on failure, NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *front, *back, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL || !number)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL) {
		*head = new;
		return (new);
	}
	back = *head;
	while (back->next != NULL) {
		front = back->next;
		if (back->n > new->n) {
			new->next = back;
			*head = new;
			return (new);
		}
		if (front->n < new->n) {
			front = front->next;
		}
		else {
			new->next = front;
			back->next = new;
			return (new);
		}
		back = back->next;
	}
	back->next = new;
	new->next = NULL;
	return (new);
}
