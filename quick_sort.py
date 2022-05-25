"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array, pivot_number=-1, head_compare=0):

    if array[pivot_number] > array[head_compare]:
        # print(pivot_number, head_compare)

        if head_compare + 1 < len(array):
            head_compare += 1
            return quicksort(array, pivot_number, head_compare)

    if array[pivot_number] < array[head_compare]:

        temp_element = array[head_compare]

        array[head_compare] = array[pivot_number - 1]
        array[pivot_number - 1] = array[pivot_number]
        array[pivot_number] = temp_element

        pivot = pivot_number - 1

        return quicksort(array, pivot, head_compare)

    if array[pivot_number] == array[head_compare]:
        print('case 4', abs(pivot_number), abs(head_compare))

        #

        if abs(pivot_number) == abs(head_compare):
            print('case 4 first if')

            print(array)

            return quicksort(array, -1, array.index(array[head_compare + 1]))

        if abs(pivot_number) != abs(head_compare):
            print('case 4 second if')
            print(array)

            # if pivot_number - 1 < len(array):
            return quicksort(array, pivot_number - 1, head_compare)

    # if head_compare + 1 < len(array):
    #     return quicksort(array, -1, head_compare)

    # else:
    #     print(array)
    #     return 'saiu'


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

print(quicksort(test))
