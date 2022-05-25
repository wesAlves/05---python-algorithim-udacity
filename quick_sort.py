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

        array_smaller = array[:pivot_number]
        array_bigger = array[pivot_number:]

        if abs(pivot_number) == abs(head_compare):
            print('case 4 first if')

            return quicksort(array, -1, array.index(array[head_compare + 1]))

        if abs(pivot_number) != abs(head_compare):
            print('case 4 second if')
            return quicksort(array, pivot_number - 1, head_compare)


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

print(quicksort(test))
