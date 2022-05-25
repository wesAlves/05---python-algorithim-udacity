"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array, pivot_number=-1, head_compare=0):

    # pivot = array[pivot_number]

    if array[pivot_number] > array[head_compare]:
        print('I pivot is bigger')
        # print (pivot_number)

        head_compare += 1
        print(head_compare)

        return quicksort(array, pivot_number, head_compare)

        # if array[pivot_number] > array[head_compare]:
        #     print ('seunda posição')

        #     temp_element = array[head_compare]

        #     array[head_compare] = array[pivot_number - 1]
        #     array[pivot_number - 1] = array[pivot_number]
        #     array[pivot_number] = temp_element

        #     pivot = pivot_number -1
        #     return quicksort(array, pivot, head_compare )
        # else:
        #     return array
    #     return quicksort(array)

    if array[pivot_number] < array[head_compare]:

        temp_element = array[head_compare]

        array[head_compare] = array[pivot_number - 1]
        array[pivot_number - 1] = array[pivot_number]
        array[pivot_number] = temp_element

        pivot = pivot_number - 1

        print('I  pivot is less')
        # print(head_compare)
        # print (pivot)
        # print (array)

        # return (array)
        return quicksort(array, pivot, head_compare)

    # if pivot == array[0]:
    #     print ('I dono yet')
    #     return array
    else:
        return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]

print(quicksort(test))
