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
        sorted_list = []


        def getMedianOrSort(A):
            if len(A) < 3:
                if len(A) < 2:
                    for i in A:
                        sorted_list.append(i)
                elif len(A) == 2:
                    if A[0] > A[1]:
                        A[0], A[1] = A[1], A[0]
                    for i in A:
                        sorted_list.append(i)
            else:
                avg = random.sample(A, k = 3)
                median = (sum(avg) // len(avg))
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
        return sorted_list

class Mergesort(Sorter):
    """
        Implements MERGESORT as discussed in the lecture
        Tipp: Moeglicherweise eine Hilfs-methode merge(self, links, rechts) implementieren
    """
    name = "MERGESORT"
    def sort(self, A):
        A = list(A)
        print(A)

        def splitList(A):
            if len(A) <= 1:
                return A

            split = len(A) // 2
            left = splitList(A[:split])
            right = splitList(A[split:])

            return sorting(left, right)

        def sorting(left, right):
            a = b = 0
            orderedList = []
            while a < len(left) and b < len(right): # when one side is finished, while loop ends because it reaches the amount of items on that side
                if left[a] < right[b]:
                    orderedList.append(left[a])
                    a += 1

                else:
                    orderedList.append(right[b])
                    b += 1
            
            orderedList.extend(left[a:])
            orderedList.extend(right[b:])
            
            return orderedList


        return splitList(A)

if __name__ == "__main__":
    for s in [Bubblesort(), Quicksort(), Mergesort()]:
        a = [random.randint(0,100) for i in range(10)]
        # Test ob euer Sortierverfahren das gleiche zurueckgibt wie die Python Implementation
        assert s.sort(a) == sorted(a), \
                            "List is not propertly sorted. "+s.name+" returned: "+str(s.sort(a))+" but we expected: "+str(sorted(a))

    print("Well done! Now go and read: https://en.wikipedia.org/wiki/Timsort to see how Python does it.")