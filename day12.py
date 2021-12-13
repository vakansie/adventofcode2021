import day12put
from collections import defaultdict
count = 0
paths = []

class Path():
    def __init__(self, cave, visited):
        self.cave = cave
        self.visited = visited
        self.visit_connected()

    def visit_connected(self):
        global count
        global paths
        if 'end' in condict[self.cave]:
            fin = self.visited.copy()
            fin.append('end')
            paths.append(', '.join(fin))
            count += 1

        for connected in condict[self.cave]:
            if connected not in ['start', 'end']:
                if (connected not in self.visited) or connected.isupper():
                    self.visited.append(connected)
                    Path(cave=connected, visited=self.visited.copy())
                    self.visited.pop(-1)

connections = day12put.input1
condict = defaultdict(list)

for connection in connections:
    if connection[1] not in condict[connection[0]]: condict[connection[0]].append(connection[1])
    if connection[0] not in condict[connection[1]]: condict[connection[1]].append(connection[0])
print(f'\n{condict}\n')

Path(cave='start', visited=['start'])

for path in paths:
    continue
    print(path)
print(len(list(paths)))
print(f'{count=}')