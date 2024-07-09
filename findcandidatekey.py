from findsuperkey import find_all_super_keys, find_closure


def find_all_candidate_key(relation, fd_sets):
    result = []
    super_keys = find_all_super_keys(relation, fd_sets)

    for super_key in super_keys:
        ret = True
        for s in result:
            if s.issubset(super_key):
                ret = False
                break

        if not ret:
            continue

        super_key = super_key.copy()
        X = list(set(super_key.copy()))
        for i in range(len(X)):
            X_temp = set(super_key.copy())
            X_temp.remove(X[i])

            if find_closure(set(X_temp), fd_sets) == relation:
                super_key.remove(X[i])
        result.append(super_key)


    return result

if __name__ == '__main__':

    # relation = ['A','B','C','D','E','G','H']
    # fd_sets = [
    #     [['A', 'B'], ['C']],
    #     [['E'], ['D']],
    #     [['A', 'B', 'C'], ['D', 'E']],
    #     [['E'], ['A', 'B']],
    #     [['D'], ['A', 'G']],
    #     [['A', 'C', 'D'], ['B', 'E']],
    # ]

    # relation = ['A','B','C','D']
    # fd_sets = [
    #     [['A', ], ['B']],
    #     [['B', 'C'], ['D']],
    #     [['A', ], ['C']],
    # ]

    relation = ['A','B','C','D','E','G','H','I','J']
    fd_sets = [
        [['A', 'J'], ['I', 'B', 'E']],
        [['D', 'E', 'J'], ['I', 'H']],
        [['E', ], ['C', 'A']],
        [['C', 'G'], ['D', 'I']],
        [['A', 'G'], ['B', ]],
        [['A', 'D', 'I'], ['E', 'H']],
    ]


    candidate_keys = find_all_candidate_key(relation, fd_sets)

    for s in candidate_keys:
        print(s)
