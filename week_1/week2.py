import time
import matplotlib.pyplot as plt

def test1(n):
    while n > 0:
        n = n - 1

nValues = [10**i for i in range(1, 7)]
runtimes = []


for n in nValues:
    startTime = time.time()
    test1(n)
    endTime = time.time()
    runtimes.append(endTime - startTime)

plt.plot(nValues, runtimes, marker='o')
plt.xlabel('n')
plt.ylabel('Runtime (seconds)')
plt.title('Runtime')
plt.xscale('log')
plt.yscale('log')
plt.show()