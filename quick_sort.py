"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    lenght = len(array)

    if lenght <= 1:
        return array

    pivot = array.pop()
    items_lower = []
    items_greater = []

    for item in array:
        if item > pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quicksort(items_lower) + [pivot] + quicksort(items_greater)


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
# test = [25, 20, 21, 21]
# test = [6, 4, 1, 3, 9]

print(quicksort(test))
