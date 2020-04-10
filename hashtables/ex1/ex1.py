#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for i in range(0, len(weights)):
        hash_table_insert(ht, weights[i], i)

    startIter = len(weights) - 1
    while startIter > -1:
        if hash_table_retrieve(ht, limit - weights[startIter]) is not None:
            secondNumber = weights[hash_table_retrieve(ht, limit - weights[startIter])]
            return [startIter, weights.index(secondNumber)]
        startIter -= 1
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
