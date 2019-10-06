from collections import defaultdict
from itertools import chain
import random
import math

def read_file(filename):
    clauses = set()

    with open(filename, 'r') as f:
        for line_num, line in enumerate(f):
            if line_num == 0:
                n = int(line.strip())
                continue
            x, y = map(int, line.strip().split(' '))
            clauses.add(frozenset([x, y]))
    
    return n, clauses

def reduce_clauses(clauses):

    reduced_clauses = clauses

    var_clause_dict = defaultdict(set)
    clause_var_dict = dict()
    for clause in clauses:
        x, y = abs(list(clause)[0]), abs(list(clause)[1])
        var_clause_dict[x].add(clause)
        var_clause_dict[y].add(clause)
        clause_var_dict[clause] = list(clause)
    
    num_singular = 0
    singular_vars = set()
    while True:
        for var in singular_vars:
            for clause in var_clause_dict[var].copy():
                reduced_clauses.remove(clause)

                vrs = clause_var_dict[clause]
                var_clause_dict[abs(vrs[0])].remove(clause)
                var_clause_dict[abs(vrs[1])].remove(clause)

        reduced_vars = set(chain(*reduced_clauses))
        singular_vars = set([abs(i) for i in reduced_vars if -i not in reduced_vars])
        if singular_vars == set():
            break
            
    return reduced_clauses

def papa(clauses):

    all_vars = set(map(abs, chain(*clauses)))
    num_repeats = int(math.log(len(all_vars), 2))
    num_searches = 2 * len(all_vars) * len(all_vars)

    for n in range(num_repeats):
        assign = dict()
        for var in all_vars:
            assign[abs(var)] = random.choice([True, False])
            assign[-abs(var)] = not assign[abs(var)]

        for m in range(num_searches):
            invalid_clauses = get_invalid_clauses(assign, clauses)
            if len(invalid_clauses) == 0:
                return 1
            rand_invalid = random.choice(invalid_clauses)
            x, y = list(map(abs, rand_invalid))
            change_var = random.choice([x, y])
            assign[change_var] = not assign[change_var]
            assign[-change_var] = not assign[-change_var]
    
    return 0

def get_invalid_clauses(assign, clauses):

    invalid_clauses = []
    for clause in clauses:
        if not  (assign[list(clause)[0]] | assign[list(clause)[1]]):
            invalid_clauses.append(clause)

    return invalid_clauses   

def main():
    filename = '2sat4.txt'
    n, clauses = read_file(filename)
    reduced_clauses = reduce_clauses(clauses)
    print(len(reduced_clauses))
    print(papa(reduced_clauses))

if __name__ == '__main__':
    main()