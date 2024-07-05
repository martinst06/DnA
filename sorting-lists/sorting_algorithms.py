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
        print(A)

        max = len(A)


        for sm in A:
            currentPosition = 0
            for sm in A:
                num1 = currentPosition + 1
                num2 = currentPosition + 2
                if currentPosition == max - 1:
                    print(f"{currentPosition} sorted")
                    time.sleep(1)
                    

                elif A[currentPosition] > A[num1]:
                    A[currentPosition:num2] = [A[num1], A[currentPosition]]
                    currentPosition = currentPosition + 1
                    print(A)
                    time.sleep(0.1)

                elif A[currentPosition] < A[num1]:
                    currentPosition = currentPosition + 1
        else:
            return A


class Quicksort(Sorter):
    """
        Implements QUICKSORT as discussed in the lecture
    """
    name = "QUICKSORT"
    def sort(self, A):
        A = list(A)
        # TODO: Bitte implementieren
        return A

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