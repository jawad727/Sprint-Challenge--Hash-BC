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
    route = ["NONE"] * length

    # Looping through each ticket, adding it to route if it has a source of "NONE"
    # If not add it to the hash table
    for t in tickets:
        if t.source == "NONE":
            route[0] = t.destination
        else:
            hash_table_insert(hashtable, t.source, t.destination)

    # looping through route to populate
    for i in range(1, len(tickets)):
        # next available route will equal the destination from the previous one
        route[i] = hash_table_retrieve(hashtable, route[i-1])

    return route