#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)




def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # Adding all weights to hash table
    for index in range(0, length):
        hash_table_insert(ht, weights[index], index)

    # Check if limit - weights[index] is True, if so we found the solution
    for index in range(0, length):
        if hash_table_retrieve(ht, limit - weights[index]):
            # If one index is greater then the other put it first in the tuple
            if index > hash_table_retrieve(ht, limit - weights[index]):
                return (index, hash_table_retrieve(ht, limit - weights[index]))
            else:
                return (hash_table_retrieve(ht, limit - weights[index]), index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
