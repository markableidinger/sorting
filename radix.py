def radix_sort(unsorted_list):
    finished = False
    current_digit = 0
    while True:
        buckets = [[] for e in range(10)]
        for num in unsorted_list:
            sig_digit = (num % (10 ** (current_digit + 1))) // (10 ** current_digit)
            buckets[sig_digit].append(num)
        if len(buckets[0]) == len(unsorted_list):
            return unsorted_list
        new_list = []
        for e in buckets:
            new_list += e
        current_digit += 1
        unsorted_list = new_list

#runtime: O(greatest int length * list length)
