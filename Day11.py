class Node:
    def __init__(self):
        self.linked: set[str] = set()

def ways_out(node: Node) -> int:
    ways: int = 0
    for way in node.linked:
        if way == 'out':
            ways = ways + 1
        ways = ways + ways_out(nodes[way])
    return ways

cnt = 0
f = open("day11.txt")
lines = f.read().splitlines(False)
nodes: dict[str, Node] = {'out': Node()}
for line in lines:
    parsed = line.split(': ')
    outputs = parsed[1].split(' ')
    if parsed[0] not in nodes:
        nodes[parsed[0]] = Node()
    for output in outputs:
        nodes[parsed[0]].linked.add(output)
print(f"Part 1: {ways_out(nodes['you'])}")
