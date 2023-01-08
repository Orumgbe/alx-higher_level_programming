#include "lists.h"
/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: double pointer to head node
 * Return: 0, if it is not a palindrome,
 * 1, if it is a palindrome
 */
int is_palindrome(listint_t** head) {
	listint_t *right;
	int arr[1000];
	int i = 0, j = 0, k;
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	right = *head;
	while (right != NULL) {
		arr[j] = right->n;
		right = right->next;
		j++;
	}
	k = j;
	while (i <= (k/2)) {
		if (arr[i] != arr[j])
			return (0);
		i++;
		j--;
	}
	return (1);
}
