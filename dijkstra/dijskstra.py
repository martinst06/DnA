eingabe = """5
0 7 7 9 5
0 0 2 1 0
0 3 0 6 0
0 9 3 0 1
0 5 0 0 0
10
3 3
2 0
1 0
2 3
2 0
2 1
4 2
4 0
0 1
4 4"""
lines = eingabe.splitlines()

n = int(lines[0]) # anzahl knoten
graph = [list(map(int, line.split())) for line in lines[1:n+1]]

for x in range(n):
    print(graph[x])

m = (int(lines[n+1]))
fragen = [list(map(int, line.split())) for line in lines[n+2:]]

for x in range(m):
    print(fragen[x])