#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node in listint_t list
 * Return: 0 if not a palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *h;
	listint_t *tmp;
	listint_t *tmp2;

	if (head == NULL || *head == NULL)
		return (0);
	h = *head;
	tmp = *head;
	while (tmp->next != NULL)
		tmp = tmp->next;
	while (h != tmp)
	{
		tmp2 = h;
		if (h->n != tmp->n)
			return (0);
		while (tmp2->next != tmp)
		{
			tmp2 = tmp2->next;
			tmp = tmp2;
			if (h == tmp)
				break;
			h = h->next;
		}	
	}
	return (1);
}
