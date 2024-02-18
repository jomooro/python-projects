def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Target found, return the index
    return -1  # Target not found

new_list = [10, 23, 14, 8, 17, 5, 12]
new_target_element = 17

result = linear_search(new_list, new_target_element)

if result != -1:
    print(f'Target element {new_target_element} found at index {result}.')
else:
    print(f'Target element {new_target_element} not found in the list.')
