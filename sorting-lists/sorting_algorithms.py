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
        n = len(A)

        for sm in range(n):
            for j in range(0, n - sm - 1):
                if A[j] > A[j + 1]:
                    A[j:j + 2] = [A[j + 1], A[j]]
        else:
            return A


class Quicksort(Sorter):
    """
        Implements QUICKSORT as discussed in the lecture
    """
    name = "QUICKSORT"
    def sort(self, A):
        A = list(A)
        sortedList = []

        def sortNum(A):
            for i in A:
                sortedList.append(i)

        def getMedianOrSort(A):
            n = len(A)

            if n < 3:
                if n < 2:
                    sortNum(A)
                elif n == 2:
                    if A[0] > A[1]:
                        A[0], A[1] = A[1], A[0]                    
                    sortNum(A)

            else:
                avg = random.sample(A, k = 3)
                median = (sum(avg) // len(avg))#not median
                split(median, A)


        def split(median, A):
            smaller = []
            bigger = []
            for i in A:
                if i <= median:
                    smaller.append(i)
                elif i > median:
                    bigger.append(i)
            getMedianOrSort(smaller)
            getMedianOrSort(bigger)
        getMedianOrSort(A)
        return sortedList


class Mergesort(Sorter):
    """
        Implements MERGESORT as discussed in the lecture
        Tipp: Moeglicherweise eine Hilfs-methode merge(self, links, rechts) implementieren
    """
    name = "MERGESORT"
    def sort(self, A):
        A = list(A)

        def splitList(A):
            if len(A) <= 1:
                return A

            split = len(A) // 2
            left = splitList(A[:split])
            right = splitList(A[split:])

            return sorting(left, right)

        def sorting(left, right):
            a = b = 0
            sortedList = []
            while a < len(left) and b < len(right): # when one side is finished, while loop ends because it reaches the amount of items on that side

                if left[a] < right[b]:
                    sortedList.append(left[a])
                    a += 1

                else:
                    sortedList.append(right[b])
                    b += 1
            
            sortedList.extend(left[a:] + right[b:])

            return sortedList

        return splitList(A)

if __name__ == "__main__":
    for s in [Bubblesort(), Quicksort(), Mergesort()]:
        a = [random.randint(0,100) for i in range(10)]
        # Test ob euer Sortierverfahren das gleiche zurueckgibt wie die Python Implementation
        assert s.sort(a) == sorted(a), \
                            "List is not propertly sorted. "+s.name+" returned: "+str(s.sort(a))+" but we expected: "+str(sorted(a))

    print("Well done! Now go and read: https://en.wikipedia.org/wiki/Timsort to see how Python does it.")