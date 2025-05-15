import random
def binary_search(L, k):
    split = len(L) // 2
    mid = L[split]
    if len(L) > 1:
        if mid > k:
            return binary_search(L[:split], k)

        elif mid < k:
            return binary_search(L[split:], k)

        elif mid == k:
            return k

    return None

#
L = range(0, 100)
k = random.randint(0,100)
# k = 101
print("k: ", k)
binary_search(L, k)