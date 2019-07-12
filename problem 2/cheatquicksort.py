def get_pivot_index(int_list):
    return 0

def partition(int_list):
    """
    Assumes pivot is in first entry
    """
    if len(int_list) == 1:
        return [], []
    
    pivot = int_list[0]
    left = []
    right = []

    for val in int_list[1:]:
        if val > pivot:
            right.append(val)
        else:
            left.append(val)
    return left, right


def quicksort(int_list):

    if len(int_list) <= 1:
        return int_list, 0

    comparisons = len(int_list) - 1

    pivot_idx = get_pivot_index(int_list)
    pivot = int_list[pivot_idx]

    int_list[0], int_list[pivot_idx] = int_list[pivot_idx], int_list[0]

    left, right = partition(int_list)

    sorted_left, comparisons_left = quicksort(left)
    sorted_right, comparisons_right = quicksort(right)
    
    new_array = sorted_left + [pivot] + sorted_right
    total_comparisons = comparisons + comparisons_right + comparisons_left

    return new_array, total_comparisons


def load_file(filename):
    integer_list = []
    with open(filename, 'r') as f:
        for line in f:
            integer_list.append(int(line))
    return integer_list

def Main():
    filename = 'QuickSort.txt'
    integer_list = load_file(filename)
    #integer_list = [5, 3, 2]
    sorted_list, comparisons = quicksort(integer_list)
    print(sorted_list)
    print(comparisons)

if __name__ == "__main__":
    Main()