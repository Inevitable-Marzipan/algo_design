from collections import defaultdict

def load_file(filename):
    input_nums = set()
    with open(filename, 'r') as f:
        for line in f:
            line = str.strip(line)
            input_nums.add(int(line))
    return input_nums

def compute_2_sum(num_set, t):

    for num in num_set:
        if (t - num) in num_set:
            if (t - num) == num:
                continue
            return True
    return False
        

def main():
    filename = 'algo1-programming_prob-2sum.txt'
    input_nums = load_file(filename)
    print(len(input_nums))
    t_vals = range(-10000, 10001)
    match_counts = 0
    for t_val in t_vals:
        valid_match = compute_2_sum(input_nums, t_val)
        match_counts += valid_match
        print(t_val, valid_match, match_counts)

    print('Total matches:', match_counts)



if __name__ == '__main__':
    main()
