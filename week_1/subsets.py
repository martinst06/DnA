def subsets(A):
    l = []
    n = len(A)

    for i in range(1, 1 << n):
        combi = []
        for j in range(n):
            if i & (1 << j):
                combi.append(A[j])
        l.append(combi)
    return l

        
print(subsets([1,2,3]))