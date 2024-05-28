#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if there is a loop in a linked list
 * @list: a ptr to the head of the linked list
 * Return: 0 if there is not a loop, 1 if there is a loop
 */
int check_cycle(listint_t *list)
{
listint_t *head;
listint_t *temp;

head = list;
temp = list;

while (temp != NULL && head->next != NULL && head->next->next != NULL)
{
head = head->next->next;
temp = temp->next;

if (head == temp)
return (1);
}
return (0);
}
