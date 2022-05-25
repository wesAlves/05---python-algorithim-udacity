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

            new_head_position = head_position
            new_pivot_position = pivot_position - 1

            print(arr, 'end')

            return quicksort(arr, pivot_position=new_pivot_position, head_position=new_head_position)

        if arr[pivot_position] > arr[head_position]:
            print('second if')
            print(arr, 'start')

            print(head_position)
            print(pivot_position)
            print(arr, 'start')

            new_head_position = head_position + 1

            print(arr)

            return last_is_bigger_than_first(
                arr, pivot_position=pivot_position, head_position=new_head_position)

        else:
            print('last else')
            smaller_than = arr[:pivot_position]

            if len(smaller_than) > 3:

                print(smaller_than, 'smallest start')

                print('pivot', pivot_position)
                print('head', head_position)

                return last_is_bigger_than_first(
                    arr, head_position=arr.index(smaller_than[0]), pivot_position=arr.index(smaller_than[-1]))

            else:
                print('is over')

                bigger_than = arr[int(len(arr)/2 + 1):]

                final_index = max(index for index, item in enumerate(
                    arr) if item == bigger_than[-1])

                if len(bigger_than) > 3:
                    return last_is_bigger_than_first(
                        arr, head_position=arr.index(arr[arr.index(bigger_than[0])]), pivot_position=final_index)

                # print(arr.index(arr[arr.index(bigger_than[0])]))
                # print(final_index)
                # print(arr[final_index])
                # print(arr.index(arr[arr.index(bigger_than[-1])]))

                # print(arr.index(arr[arr.index(bigger_than[0])]))
                # print(final_index)

                return arr

                return last_is_bigger_than_first(
                    arr, head_position=arr.index(arr[arr.index(bigger_than[0])]), pivot_position=final_index)

    array = last_is_bigger_than_first(array, **kwargs)

    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
# test = [25, 20, 21, 21]
# test = [6, 4, 1, 3, 9]

print(quicksort(test))
