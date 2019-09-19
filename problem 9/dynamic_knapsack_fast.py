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
    sol_arr = [0] * (capacity + 1)
    for item_num, item in enumerate(items):
        if item_num % 10 == 0:
            print(item_num)
        cap = capacity
        while cap >= item.weight:
            sol_arr[cap] = max(sol_arr[cap], sol_arr[cap - item.weight] + item.value)
            cap -= 1

    return sol_arr

def main():
    filename = args.filename
    capacity, num_items, items = read_file(filename)
    print(capacity, num_items)
    sol = solve_knapsack_dynamic(capacity, items)
    print(sol[capacity])

if __name__ == '__main__':
    main()

