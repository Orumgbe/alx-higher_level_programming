#include "lists.h"
/**
 * check_cycle - checks for cycle in singly linked list
 * @list: head node
 * Return: 0 for no cycle, 1 for cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *double = NULL, *single = NULL;

	if (list == NULL)
		return (0);
	single = list;
	double = list->next;
	while (double && list->next->next)
	{
		if (double == single)
			return (1);
		double = double->next->next;
		single = single->next;
	}
	return (0);
} 
