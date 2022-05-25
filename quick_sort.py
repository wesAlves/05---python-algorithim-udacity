"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array, pivot_number=-1, head_compare=0):

    if array[pivot_number] > array[head_compare]:
        print('caso 1', pivot_number, head_compare)

        if head_compare + 1 < len(array):
            print('caso 1 first if')
            if array[pivot_number] > array[pivot_number - 1]:
                print('caso 1 first if / if')
                pivot_number += 1
                head_compare += 1

                return quicksort(array, pivot_number, head_compare)
            else:
                print('caso 1 first if /  else')
                head_compare += 1
                return quicksort(array, pivot_number, head_compare)
        else:
            print('caso 1 first else')
            return quicksort(array)

    if array[pivot_number] < array[head_compare]:
        print('caso 2', pivot_number, head_compare)

        temp_element = array[head_compare]

        array[head_compare] = array[pivot_number - 1]
        array[pivot_number - 1] = array[pivot_number]
        array[pivot_number] = temp_element

        pivot = pivot_number - 1

        return quicksort(array, pivot, head_compare)

    if array[pivot_number] == array[head_compare]:
        print('caso 3', pivot_number, head_compare)

        array_smaller = array[:pivot_number - 1]
        array_bigger = array[pivot_number + 1:]

        if array_bigger[0] >= array_bigger[-1]:
            print('caso 3  first if')

            if abs(pivot_number) == abs(head_compare):
                print('case 3 first if / first if')

                return quicksort(array, -1, array.index(array[head_compare + 1]))

            if abs(pivot_number) != abs(head_compare):
                print('case 3 first if / second if ')
                return quicksort(array, pivot_number - 1, head_compare)

            else:
                print('case 3 first if / else ')
                return array
        else:
            # print(array)
            # print(pivot_number)
            # print(head_compare)
            # print(array_smaller[0])
            # print(array_smaller[-1])
            print(array.index(array_smaller[-1]),
                  array.index(array_smaller[0]))
            # return array
            # return quicksort(array_smaller, array.index(array_smaller[-1]), array.index(array_smaller[0]))


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
# test = [6, 4, 1, 3, 9]

print(quicksort(test))
