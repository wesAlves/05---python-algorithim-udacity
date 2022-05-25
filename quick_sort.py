"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


from re import A


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

        array_smaller = array[:pivot_number - 3]
        array_bigger = array[pivot_number + 1:]

        if array_bigger[-1] > array_bigger[0]:
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

        if array_bigger[-1] < array_bigger[0]:
            print('caso 3  second if')
            return quicksort(array, )

        if array_bigger[-1] == array_bigger[0]:
            print('caso 3  third if')
            print(array_bigger)
            print(array_smaller)
            print(array)
            # print(array_bigger[0], array_bigger[-1])
            # print(pivot_number, head_compare)

        if array_smaller[-1] > array_smaller[0]:
            print('is smaller entrou')
            print(array_smaller)
            return quicksort(array, array.index(array_smaller[-1]), array[0])

        if array_smaller[-1] < array_smaller[0]:
            print('is smaller saiu')
            print(array_smaller)
            return quicksort(array, array.index(array_smaller[-1-1], array[0]))

        if array_smaller[-1] == array_smaller[0]:
            print('é igual')
            return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
# test = [6, 4, 1, 3, 9]

print(quicksort(test))
