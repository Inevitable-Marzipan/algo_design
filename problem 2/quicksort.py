def mean3(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    else:
        return c

def _get_pivot_idx(int_list, l, r):

    first = int_list[l]
    last = int_list[r - 1]

    if (r - l) % 2: # odd
        middle_idx = int(l + ((r - l) // 2))
    else: # even
        middle_idx = int(l + ((r - l) / 2))  - 1
    
    middle = int_list[middle_idx]

    median_val = mean3(first, middle, last)

    if median_val == first:
        return l
    elif median_val == middle:
        return middle_idx
    else:
        return r - 1


def _partition(int_list, l, r):

    pivot = int_list[l]
    i = l + 1
    seen_bigger_than_p = False

    for j in range(i, r):
        val = int_list[j]
        
        if seen_bigger_than_p:
            if val < pivot:
                int_list[i], int_list[j] = int_list[j], int_list[i]
                i += 1
        elif not seen_bigger_than_p:
            if val <= pivot:
                i += 1
            else:
                seen_bigger_than_p = True
    
    int_list[l], int_list[i - 1] = int_list[i - 1], int_list[l]

    return i - 1

def _quicksort(int_list, l, r):

    total_comparisons = 0
    if l < r:
        total_comparisons += r - l - 1
        pivot_idx = _get_pivot_idx(int_list, l, r)
        int_list[l], int_list[pivot_idx] = int_list[pivot_idx], int_list[l]

        split_point = _partition(int_list, l, r)

        left_comparisons = _quicksort(int_list, l, split_point)
        right_comparisons = _quicksort(int_list, split_point + 1, r)
        total_comparisons += left_comparisons + right_comparisons
    
    return total_comparisons


def quicksort(int_list):
    
    comparisons = _quicksort(int_list, 0, len(int_list))
    return comparisons

def load_file(filename):
    integer_list = []
    with open(filename, 'r') as f:
        for line in f:
            integer_list.append(int(line))
    return integer_list

def Main():
    filename = 'QuickSort.txt'
    integer_list = load_file(filename)
    #integer_list = [1, 2, 3, 4]
    comparisons = quicksort(integer_list)
    print(integer_list)
    print(comparisons)

if __name__ == "__main__":
    Main()








