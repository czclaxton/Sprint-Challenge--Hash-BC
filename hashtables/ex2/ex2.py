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
    route = [None] * length

    for ticket in tickets:
        source = ticket.source
        destination = ticket.destination
        hash_table_insert(hashtable, source, destination)

    first = hash_table_retrieve(hashtable, "NONE")
    route[0] = first

    for i in range(1, length):
        last = hash_table_retrieve(hashtable, first)
        route[i] = last
        first = last

    return route
