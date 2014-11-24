def mergesort(unsorted_list):
    if len(unsorted_list) < 2:
        return unsorted_list
    sorted_list = []
    midpoint = len(unsorted_list) // 2
    first_half = mergesort(unsorted_list[:midpoint])
    second_half = mergesort(unsorted_list[midpoint:])
    while (len(first_half) > 0) and (len(second_half) > 0):
        if first_half[0] < second_half[0]:
            sorted_list.append(first_half.pop(0))
        else:
            sorted_list.append(second_half.pop(0))
    print sorted_list
    sorted_list += first_half
    sorted_list += second_half
    return sorted_list


def mergesort_inplace(list_to_sort):
    if len(list_to_sort) <= 1:
        return list_to_sort
    else:
        mid = len(list_to_sort) // 2
        left = mergesort_inplace(list_to_sort[:mid])
        right = mergesort_inplace(list_to_sort[mid:])
        left_counter, right_counter, main_counter = 0, 0, 0
        while left_counter < len(left) and right_counter < len(right):
            if left[left_counter] < right[right_counter]:
                list_to_sort[main_counter] = left[left_counter]
                left_counter += 1
                main_counter += 1
            else:
                list_to_sort[main_counter] = right[right_counter]
                right_counter += 1
                main_counter += 1
        if left_counter < right_counter:
            remaining = left
        else:
            remaining = right
        if remaining == left:
            remaining_counter = left_counter
        else:
            remaining_counter = right_counter
        while remaining_counter < len(remaining):
            list_to_sort[main_counter] = remaining[remaining_counter]
            remaining_counter += 1
            main_counter += 1
        return list_to_sort



        # while (len(first_half) > 0) and (len(second_half) > 0):
        #     if first_half[0] < second_half[0]:
        #         sorted_list.append(first_half.pop(0))
        #     else:
        #         sorted_list.append(second_half.pop(0))
        # print sorted_list
        # sorted_list += first_half
        # sorted_list += second_half
