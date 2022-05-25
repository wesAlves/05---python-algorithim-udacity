"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


from re import A


def quicksort(array, **kwargs):

    def last_is_bigger_than_first(arr, head_position=0, pivot_position=-1):
        if arr[pivot_position] < arr[head_position]:
            print('if')
            print(arr, 'start')

            print(head_position)
            print(pivot_position)
            print(arr, 'start')

            temp_arr_0 = arr[head_position]

            arr[head_position] = arr[pivot_position - 1]
            arr[pivot_position - 1] = arr[pivot_position]
            arr[pivot_position] = temp_arr_0

            # new_head_position =
            new_pivot_position = pivot_position - 1

            print(arr, 'end')

            return quicksort(arr, pivot_position=new_pivot_position)

        if arr[pivot_position] > arr[head_position]:
            print('else')
            print(arr, 'start')

            print(head_position)
            print(pivot_position)
            print(arr, 'start')

            new_head_position = head_position + 1

            print(arr)

            return last_is_bigger_than_first(arr, pivot_position=pivot_position, head_position=new_head_position)

    array = last_is_bigger_than_first(array, **kwargs)

    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
# test = [6, 4, 1, 3, 9]

print(quicksort(test))
