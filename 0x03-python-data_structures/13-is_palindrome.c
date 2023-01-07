#include "lists.h"
/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: double pointer to head node
 * Return: 0, if it is not a palindrome,
 * 1, if it is a palindrome
 */
int is_palindrome(listint_t** head) {
	listint_t *left, *right, *temp;
	if (*head == NULL || (*head)->next)
		return (1);
	right = left = temp = *head;
	while (right->next != NULL)
		right = right->next;
	while (left != right || left->next != right) {
		if (left->n != right->n)
			return (0);
		while (temp->next != right)
			temp = temp->next;
		right = temp;
		left = left->next;
		temp = left;
	}
	return (1);
}
