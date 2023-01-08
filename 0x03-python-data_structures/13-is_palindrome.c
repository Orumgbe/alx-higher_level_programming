#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - Check if a linked list is a palindrome
 * @head: double pointer to head node
 * Return: 1 if it's a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast && fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	slow = reverse_list(&slow);
	fast = *head;
	while (slow && fast)
	{
		if (slow->n != fast->n)
			return (0);
		slow = slow->next;
		fast = fast->next;
	}
	return (1);
}

/**
 * reverse_list - reverses a linked list
 * @head: head node
 * Return: Pointer to the new head
 */
listint_t *reverse_list(listint_t **head)
{
        listint_t *prev = NULL;
        listint_t *next = NULL;

        while (*head)
        {
                next = (*head)->next;
                (*head)->next = prev;
                prev = *head;
                *head = next;
        }
        *head = prev;
        return (*head);
}
