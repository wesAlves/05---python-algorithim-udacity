"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array, pivot_number=-1, head_compare=0):

    if array[pivot_number] > array[head_compare]:
        # print('case 1', pivot_number, head_compare)
        # print(array, 'case 1')
        # print(pivot_number, head_compare)

        head_compare += 1
        # pivot_number -= 1

        return quicksort(array, pivot_number, head_compare)

    if array[pivot_number] < array[head_compare]:
        # print('case 2', pivot_number, head_compare)
        # print(array, 'case 2')

        temp_element = array[head_compare]

        array[head_compare] = array[pivot_number - 1]
        array[pivot_number - 1] = array[pivot_number]
        array[pivot_number] = temp_element

        pivot = pivot_number - 1

        return quicksort(array, pivot, head_compare)

    # if array[pivot_number] == array[head_compare] and array.index(array[pivot_number]) != array.index(array[head_compare]):
    #     print('case 3', pivot_number, head_compare)

    #     print(array.index(array[pivot_number]) !=
    #           array.index(array[head_compare]))

    if array[pivot_number] == array[head_compare]:
        print('case 4', pivot_number, head_compare)

        # print(array.index(array[pivot_number]) !=
        #       array.index(array[head_compare]))
        # print(array[pivot_number], array[head_compare])
        print(abs(pivot_number), abs(head_compare))

        if abs(pivot_number) != abs(pivot_number):
            print('case 4 cheguei aqui!!')

            return 'casa'
            # print(abs(pivot_number), abs(head_compare))
            # print(array)
            # print(array.index(array[pivot_number]),
            #   array.index(array[head_compare]))

            # return quicksort(array, pivot_number - 1)

            # return 'banana'

        if head_compare + 1 < len(array):
            # print('is smaller')
            # print(array, 'case 4 if')
            return quicksort(array, -1, head_compare)
        else:
            print('case 4 else')
            return array

        # print(array[pivot_number] == array[head_compare])

        # go smaller first
        # array_smaller = array[:pivot_number]
        # array_bigger = array[pivot_number + 1:]

        # if array_smaller[-1] > array_smaller[0]:
        #     print('array last is samaller than fisrt')
        # print(array)

        # print(pivot)
        # quicksort(array, pivot_smaller, head_compare)
        # quicksort(array, array.index(
        #     array[-1]), array.index(array_bigger[0]))

        # print(
        #     array_bigger,
        #     array.index(array_bigger[0]),
        #     array.index(array[-1])
        # )

        # return array

        # else:
        #     print('array last is bigger than fisrt')
        #     print(pivot_number)

        #     pivot = array.index(array_bigger[0])
        #     print(pivot)

        # return array

        # if array_smaller[-1] == array_smaller[0]:
        #     print('array last is not samller than fisrt')
        #     # print(array[pivot_number] == array[head_compare])

    # return array

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
