def subsets(A):
    l = []
    n = len(A)

    for i in range(1 << n):
        singleCombination = []
        for j in range(n):
            if i &(1 << j):
                singleCombination.append(A[j])
        l.append(singleCombination)
    return l

print(subsets([1,2,3]))