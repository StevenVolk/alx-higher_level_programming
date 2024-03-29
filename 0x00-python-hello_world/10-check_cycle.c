#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: a singly linked list to be checked
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (list && slow && fast && slow->next && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (!fast || !slow)
			return (0);
		if (fast->next == slow)
			return (1);
	}
	return (0);
}
