#include "lists.h"
#include <stdio.h>
/**
 *check_cycle - checks the cycle in the list
 *@list: pointer to a list
 *Return: returns 1 otherwise 0 in no cycle
 */

int check_cycle(listint_t *list)
{


	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}
	return (0);
}
