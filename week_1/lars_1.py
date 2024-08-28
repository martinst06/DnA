from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt
import contextlib

def test1(n):
    while n > 0:
        print(n)
        n = n - 1

def plot_function(f,n):
    with contextlib.redirect_stdout(None):
        # time the function for input sizes 0, 1, 2, ..., n
        T = []
        for i in range(n):
            start = timer()
            f(i)
            end = timer()
            T.append(end - start)

        # compute the average time 
        avg_T = []
        window = n//10 
        for i in range(len(T)-window+1):
            avg_T.append(np.mean(T[i:i+window]))

        # plot the time
        plt.plot(T)
        plt.plot(avg_T)
        plt.ylabel('Time')
        plt.xlabel('Input size')
        plt.show()

# plot the runtime of test1 
plot_function(test1, 10000)