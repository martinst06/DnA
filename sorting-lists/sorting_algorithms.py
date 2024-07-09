import random, time

class Sorter:
    def sort(self, A):
        """
            Sort a list A in increasing order.
            Important: Always return a *copy* of the input list A, do *not* change the list A 
                       
            return: The sorted list A
        """
        raise NotImplementedError

class Bubblesort(Sorter):
    """
        Implements BUBBLESORT as discussed in the lecture
    """
    name = "BUBBLESORT"
    def sort(self, A):
        A = list(A)
        # print(A)

        n = len(A)


        for sm in range(n):
            for j in range(0, n - sm - 1):
                if A[j] > A[j + 1]:
                    A[j:j + 2] = [A[j + 1], A[j]]
                    j = j + 1
                    # print(A)
                    time.sleep(0.01)

                elif A[j] < A[j + 1]:
                    j = j + 1
        else:
            return A


class Quicksort(Sorter):
    """
        Implements QUICKSORT as discussed in the lecture
    """
    name = "QUICKSORT"
    def sort(self, A):
        A = list(A)
        print (A)
        sorted_list = []


        def getMedian(A):
            if len(A) < 3:
                if len(A) < 2:
                    print(f"one: {A}")
                    for i in A:
                        sorted_list.append(i)
                elif len(A) == 2:
                    if A[0] > A[1]:
                        A[0], A[1] = A[1], A[0]
                        print(f"two: {A}")
                        for i in A:
                            sorted_list.append(i)

            else:
                avg = random.sample(A, k = 3)
                print(f"avg nrs: {avg}")
                median = (sum(avg) // len(avg))
                print(f"median {median}")
                sort(median, A)
                print()

        def sort(median, A):
            time.sleep(1)
            smaller = []
            bigger = []
            for i in A:
                if i <= median:
                    smaller.append(i)
                elif i >= median:
                    bigger.append(i)
            print(f"smaller: {smaller}")
            getMedian(smaller) # do if smaller is empty, call: getMedian(bigger)
            # getMedian(bigger)


        getMedian(A)
        if len(sorted_list) == len(A):
            return sorted_list
        print(f"SL: {sorted_list}")

class Mergesort(Sorter):
    """
        Implements MERGESORT as discussed in the lecture
        Tipp: Moeglicherweise eine Hilfs-methode merge(self, links, rechts) implementieren
    """
    name = "MERGESORT"
    def sort(self, A):
        A = list(A)
        # TODO: Bitte implementieren
        return A

if __name__ == "__main__":
    for s in [Bubblesort(), Quicksort(), Mergesort()]:
        a = [random.randint(0,100) for i in range(10)]
        # Test ob euer Sortierverfahren das gleiche zurueckgibt wie die Python Implementation
        assert s.sort(a) == sorted(a), \
                            "List is not propertly sorted. "+s.name+" returned: "+str(s.sort(a))+" but we expected: "+str(sorted(a))

    print("Well done! Now go and read: https://en.wikipedia.org/wiki/Timsort to see how Python does it.")