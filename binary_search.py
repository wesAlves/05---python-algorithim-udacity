def binary_search(input_array, value):
    """Your code goes here."""
    new_input_array = input_array
    half_array_index = round(len(input_array)/2)

    array_pos = -1


    def new_array_from(oldArray, first_array_position, last_array_position):
        new_array = oldArray[int(first_array_position) : last_array_position]
        return new_array
    
    while half_array_index >= 3:
        
        if value > new_input_array[int(half_array_index - 1)]:
            if value == new_input_array[half_array_index]:
                return new_input_array.index(value)
            
            elif len(new_input_array) > 3:
                new_input_array = new_array_from(new_input_array, half_array_index, new_input_array[-1])
                half_array_index= half_array_index = round(len(new_input_array)/2)
                # print(len(new_input_array))

            elif value == new_input_array[half_array_index + 1]:
                print(len(new_input_array))
                # return -11
            
    return array_pos
        
        # print(half_array_index, new_input_array)


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))