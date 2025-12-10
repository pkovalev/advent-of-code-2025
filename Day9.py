import itertools

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class LineSegment:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b
        
    def minMaxX(self):
        return min(self.a.x, self.b.x), max(self.a.x, self.b.x)
    def minMaxY(self):
        return min(self.a.y, self.b.y), max(self.a.y, self.b.y)

    def in_square(self, corner1: Point, corner2: Point):
        min_x = min(corner1.x, corner2.x)
        max_x = max(corner1.x, corner2.x)
        min_y = min(corner1.y, corner2.y)
        max_y = max(corner1.y, corner2.y)
        self_x = self.minMaxX()
        self_y = self.minMaxY()
        res =  (self_x[0] < max_x 
                and self_x[1] > min_x
                and self_y[0] < max_y
                and self_y[1] > min_y)
        return res

def get_square(a: Point, b: Point):
    return (abs(a.x - b.x) + 1) *  (abs(a.y - b.y) + 1)


cnt = 0
f = open("day9.txt")
lines = f.read().splitlines(False)
lines = list(map(lambda item: Point(int(item.split(',')[0]), int(item.split(',')[1])) ,lines))
pairs = list(itertools.combinations(lines, 2))
sorted_pairs = sorted(pairs, key= lambda x: get_square(x[0], x[1]))
print(f'Part 1: {get_square(sorted_pairs[-1][0], sorted_pairs[-1][1])}')

border_lines = list(map(lambda x: LineSegment(x[0], x[1]), filter(lambda x: x[0].x == x[1].x, pairs)))
border_lines.extend(map(lambda x: LineSegment(x[0], x[1]), filter(lambda x: x[0].y == x[1].y, pairs)))
sorted_pairs.reverse()

for pair in sorted_pairs:
    has_intersections = False
    for v_line in border_lines:
        has_intersections = has_intersections | v_line.in_square(pair[0], pair[1])
        if has_intersections:
            break
    if not has_intersections:
        print(f'Part2: {get_square(pair[0], pair[1])}')
        break
