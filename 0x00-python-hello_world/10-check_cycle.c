#include "lists.h"

/**
 * check_cycle - checks a cycle
 * @list: list
 *
 * Returns: 0 if there's a cycle, 1 if not
 */

int check_cycle(listint_t *list)
{
	int node_number = 0;
	listint_t *first_node = list, aux = list;
	int comparisson = 0;

	while (aux != NULL)
	{
		aux = aux->next;
		node_number++;
	}
	if (*aux->next != *first_node)
		comparisson = 1;

	return (comparisson);
}
