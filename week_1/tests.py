def test1(n):
    while n > 0:
        print(n)
        n = n-1

def test2(n):
    if n <= 0:
        return
    print(n)
    test2(n-1)

def test3(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i*j*k)

def test4(n):
    print (n)

def test5(x, A):
    print (x, A)
    if len(A) == 0:
        return False
    m = int(len(A)/2)
    if A[m] > x:
        return test5(x, A[:m])
    elif A[m] < x:
        return test5(x, A[m+1:])
    else:
        return True

def test6(A):
    i = 0
    while i < len(A):
        print (A[i])
        i += 3




