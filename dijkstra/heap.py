from random import *

class Heap:
    def __init__(self):
        self.data = []

    def insert(self, key):
        # insert at last position
        self.data.append(key)

        # bubble up
        index = len(self.data) - 1
        while index > 0 and self.data[index] > self.data[(index - 1) // 2]:
            self.data[index], self.data[(index - 1) // 2] = self.data[(index - 1) // 2], self.data[index]
            index = (index - 1) // 2

    def pop(self):
        # swap first with last element and remove it
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        key = self.data.pop()

        # sift down top element
        index = 0
        self.data.append(-float("inf"))
        while True:
            left, right = index * 2 + 1, index * 2 + 2
            if left >= len(self.data):
                break
            if right >= len(self.data) or self.data[left] > self.data[right]:
                if self.data[left] > self.data[index]:
                    self.data[index], self.data[left] = self.data[left], self.data[index]
                    index = left
                else:
                    break
            else:
                if self.data[right] > self.data[index]:
                    self.data[index], self.data[right] = self.data[right], self.data[index]
                    index = right
                else:
                    break
        self.data.pop()
        return key

def heapsort(L):
    h = Heap()
    for l in L:
        h.insert(l)
    return [h.pop() for _ in L]

if __name__ == "__main__":
    print(heapsort([randint(0, 1000) for _ in range(100)]))
