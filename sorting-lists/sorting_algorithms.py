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
        sorted_list = []
        

        # def switch(current):
        #     for n in current: # for j in n or msth for basically add one position after every comparison??
        #         if current[n] > current[n + 1]:
        #             current[n], current[n + 1] = current[n + 1], current[n]
        #             sorted_list.append(current)

        #         print(f"current2: {current}")
        #         return current

        def listThing(left, right):
            print(f"left: {left}")
            print(f"right: {right}")
            splitList(left)
            splitList(right)
        
        def splitList(A):
            if len(A) > 1:
                split = len(A) // 2
                left = A[:split]
                right = A[split:]
                listThing(left, right)

            elif len(A) == 1:
                sortt(A)

        temp = []
        def sortt(A):
            for i in A:
                temp.append(i)

                if (len(temp) % 2) == 1:
                    for i in temp:
                        sorted_list.append(i)
                        print(f"appended: {i}")
                    temp.clear()
                elif (len(temp) % 2) == 0:
                    if temp[0] > temp[1]:
                        temp[0], temp[1] = temp[1], temp[0]
                    for i in temp:
                        sorted_list.append(i)
                    temp.clear()

        def sorting(A):
            for n in A:
                for m in A:
                    if A[m] > A[n]:
                        # not done
                        sublist.append(A[n])
                    elif A[m] <= A[n]:
                        sublist.append(A[m])
                    elif A[m] == A[-1]:
                        sublist.append(A[m])
                    


        splitList(A)
        print(sorted_list)
        return sorted_list

if __name__ == "__main__":
    for s in [Bubblesort(), Quicksort(), Mergesort()]:
        a = [random.randint(0,100) for i in range(10)]
        # Test ob euer Sortierverfahren das gleiche zurueckgibt wie die Python Implementation
        assert s.sort(a) == sorted(a), \
                            "List is not propertly sorted. "+s.name+" returned: "+str(s.sort(a))+" but we expected: "+str(sorted(a))

    print("Well done! Now go and read: https://en.wikipedia.org/wiki/Timsort to see how Python does it.")