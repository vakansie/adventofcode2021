import day12put
from collections import defaultdict
count = 0
paths = []

class Path():
    def __init__(self, cave, visited, doubled):
        self.cave = cave
        self.visited = visited
        self.doubled = doubled
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
                if connected not in self.visited or connected.isupper():
                    self.visited.append(connected)
                    Path(cave=connected, visited=self.visited.copy(), doubled=self.doubled)
                    self.visited.remove(connected)
                elif connected in self.visited and connected in smalls and not self.doubled:
                    self.doubled = True
                    self.visited.append(connected)
                    Path(cave=connected, visited=self.visited.copy(), doubled=self.doubled)
                    self.visited.remove(connected)
                    self.doubled = False

connections = day12put.exa
condict = defaultdict(list)

for connection in connections:
    if connection[1] not in condict[connection[0]]: condict[connection[0]].append(connection[1])
    if connection[0] not in condict[connection[1]]: condict[connection[1]].append(connection[0])
print(f'\n{condict}\n')

smalls = [key for key in condict if key.islower() and key not in ['start', 'end']]
print(smalls)

Path(cave='start', visited=['start'], doubled=False)

for path in paths:
    print(path)
print(len(list(paths)))
print(f'{count=}')