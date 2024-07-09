import itertools

def find_closure(relation, fd_sets):
    closure = set(relation)
    ret = True

    while ret:
        ret = False
        for W, Z in fd_sets:
            if set(W).issubset(closure) and len(set(Z).difference(closure)) !=0:
                closure = closure.union(set(Z))
                ret = True
    return closure

def is_super_key(relation, fd_sets, R):
    return find_closure(relation, fd_sets) == set(R)

def find_all_super_keys(relation, fd_sets):
    result = []
    for i in range(1, len(relation)+1):
        for subset in itertools.combinations(relation, i):
            subset = set(subset)
            if is_super_key(subset, fd_sets, set(relation)):
                result.append(subset)
    return result

if __name__ == '__main__':

    relation = ['A','B','C','D','E','G','H']
    fd_sets = [
        [['A', 'B'], ['C']],
        [['E'], ['D']],
        [['A', 'B', 'C'], ['D', 'E']],
        [['E'], ['A', 'B']],
        [['D'], ['A', 'G']],
        [['A', 'C', 'D'], ['B', 'E']],
    ]

    super_keys = find_all_super_keys(relation, fd_sets)

    for s in super_keys:
        print(s)

