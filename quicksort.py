def quicksort(unsorted_list):
    if len(unsorted_list) < 1:
        return unsorted_list
    else:
        pivot = unsorted_list[-1]
        pivot_list = [pivot]    #using pivot_list should help with quicksort's difficulties with repeating elements
        left_partition = []
        right_partition = []
        for i in unsorted_list[:-1]:
            if i < pivot:
                left_partition.append(i)
            elif i > pivot:
                right_partition.append(i)
            else:
                pivot_list.append(i)
        return quicksort(left_partition) + pivot_list + quicksort(right_partition)


def quicksort_inplace(array):
    if len(array) < 2:
        return array
    _quicksort_inplace(array, 0, len(array) - 1)


def _quicksort_inplace(array, index1, index2):
    if index2 - index1 > 0:
        pivot, left, right = array[index1], index1, index2
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        _quicksort_inplace(array, index1, right)
        _quicksort_inplace(array, left, index2)
