import argparse
from collections import namedtuple

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str,
                    help='input file')

args = parser.parse_args()

Item = namedtuple('Item', ['value', 'weight'])

def read_file(filename):
    items = []

    with open(filename, 'r') as f:
        for line_num, line in enumerate(f):
            if line_num == 0:
                capacity, num_items = map(int, line.strip().split(' '))
                continue
            value, weight = map(int, line.strip().split(' '))
            item = Item(value, weight)
            items.append(item)
    
    return capacity, num_items, items

def solve_knapsack_dynamic(capacity, items):
    num_items = len(items)

    sol_arr = [[0] * (num_items + 1) for _ in range(capacity + 1)]

    for item_num, item in enumerate(items, 1):
        if item_num % 10 == 0:
            print(item_num)
        for cap in range(1, capacity + 1):
            item_less_val = sol_arr[cap][item_num - 1]
            if cap - item.weight < 0:
                sol_arr[cap][item_num] = item_less_val
            else: 
                include_item_val = sol_arr[cap - item.weight][item_num - 1] + item.value
                sol_arr[cap][item_num] = max(item_less_val, include_item_val)


    return sol_arr

def main():
    filename = args.filename
    capacity, num_items, items = read_file(filename)
    print(capacity, num_items)
    sol = solve_knapsack_dynamic(capacity, items)
    #for line in sol:
    #    print(line)
    print(sol[capacity][num_items])

if __name__ == '__main__':
    main()

