#include "lists.h"

/**
 * check_cycle - Function to check if there is cycle in list
 * @list: linked list to check
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *up;
	listint_t *down;

	if (!list)
		return (0);
	up= list;
	down = list;

	while (down != NULL && down->next != NULL)
	{
		up = up->next;
		down = down->next->next;

		if (up == down)
			return (1);
	}
	return (0);
}
