def merge_and_count(left, right):
    new_array = [None] * (len(left) + len(right))
    count = 0

    left_idx = 0
    right_idx = 0
    for idx, _ in enumerate(new_array):


        if (left_idx < len(left)) and (right_idx < len(right)):
            left_val = left[left_idx]
            right_val = right[right_idx]
            if left_val < right_val:
                new_array[idx] = left_val
                left_idx += 1
            elif left_val > right_val:
                new_array[idx] = right_val
                count += len(left) - (left_idx)
                right_idx += 1
                
            else:
                new_array[idx] = right_val
                right_idx += 1

        elif (left_idx == len(left)):
            new_array[idx:] = right[right_idx:]
            break

        elif (right_idx == len(right)):
            new_array[idx:] = left[left_idx:]
            break
    return new_array, count

def mergesort_and_count(integer_list):

    len_list = len(integer_list)
    if len_list == 1:
        return integer_list, 0
    else:
        split = len_list // 2    
        left, left_count = mergesort_and_count(integer_list[:split])
        right, right_count = mergesort_and_count(integer_list[split:])
    
    new_array, cross_count = merge_and_count(left, right)

    total_count = left_count + right_count + cross_count

    return new_array, total_count


def load_file(filename):
    integer_list = []
    with open(filename, 'r') as f:
        for line in f:
            integer_list.append(int(line))
    return integer_list

def Main():
    filename = 'IntegerArray.txt'
    integer_list = load_file(filename)
    _, count = mergesort_and_count(integer_list)
    print(count)

if __name__ == "__main__":
    Main()

