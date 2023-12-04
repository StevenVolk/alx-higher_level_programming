#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *check = *head;
	int num_of_nodes = 0, index = 0, *array = NULL;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
		return (1);
	while (check)
	{
		++num_of_nodes;
		check = check->next;
	}
	array = malloc(sizeof(int) * num_of_nodes);
	check = *head;
	while (check)
	{
		array[index++] = check->n;
		check = check->next;
	}
	for (index = 0; index < num_of_nodes / 2; index++)
	{
		if (array[index] != array[num_of_nodes - 1 - index])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
