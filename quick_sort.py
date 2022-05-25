"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array, pivot_number=-1, head_compare=0):

    if array[pivot_number] > array[head_compare]:
        print(pivot_number)

        head_compare += 1

        return quicksort(array, pivot_number, head_compare)

    if array[pivot_number] < array[head_compare]:
        print(pivot_number)

        temp_element = array[head_compare]

        array[head_compare] = array[pivot_number - 1]
        array[pivot_number - 1] = array[pivot_number]
        array[pivot_number] = temp_element

        pivot = pivot_number - 1

        return quicksort(array, pivot, head_compare)

    if array[pivot_number] == array[head_compare]:
        print(pivot_number)
        print(array[pivot_number] == array[head_compare])

        # go smaller first
        array_smaller = array[0:pivot_number]

        if array_smaller[-1] > array_smaller[0]:
            print('array last is samller than fisrt')

            pivot = array.index((array_smaller[-1]))
            # print(pivot)

            return quicksort(array, pivot, head_compare)

        # if array_smaller[-1] == array_smaller[0]:
        #     print('array last is not samller than fisrt')
        #     # print(array[pivot_number] == array[head_compare])

    return array

    # return quicksort(array, array_smaller.index(array_smaller[-1]))

    # array_bigger = array[pivot_number + 1: -1]

    # print(array)
    # return quicksort(array, head_compare=pivot_number + 1)

    # print(array_bigger)

    # return quicksort(array_smaller)

    # else:
    #     return 'banana'


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

print(quicksort(test))
