#include "lists.h"
/**
 * check_cycle - checks for cycle in singly linked list
 * @list: head node
 * Return: 0 for no cycle, 1 for cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = NULL, *slow = NULL;

	if (list == NULL)
		return (0);
	slow = list;
	fast = list;
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
	}
	return (0);
} 
