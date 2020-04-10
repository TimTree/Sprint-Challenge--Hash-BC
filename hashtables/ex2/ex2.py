#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)

    """
    YOUR CODE HERE
    """
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    route_number = 0
    while route_number < len(route):
        if route_number == 0:
            route[route_number] = hash_table_retrieve(hashtable, 'NONE')
        else:
            route[route_number] = hash_table_retrieve(hashtable, route[route_number - 1])
        route_number += 1

    return route
