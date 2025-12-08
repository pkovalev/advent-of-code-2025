import itertools

def multiply_x(a: str, b: str):
    a = list(map(lambda x: int(x), a.split(',')))
    b = list(map(lambda x: int(x), b.split(',')))
    return a[0]*b[0]

def get_distance_square(a: str, b: str):
    a = list(map(lambda x: int(x), a.split(',')))
    b = list(map(lambda x: int(x), b.split(',')))
    return pow(a[0]-b[0], 2) + pow(a[1]-b[1], 2) + pow(a[2] - b[2], 2)

last = 0
group_id = 1
groups = {}
f = open("day8.txt")
lines = f.read().splitlines(False)
lines = list(map(lambda x: [0, x], lines))
pairs = list(itertools.combinations(lines, 2))
sorted_pairs = sorted(pairs, key= lambda x: get_distance_square(x[0][1], x[1][1]))
limit = 1000
i = 0
while i < len(sorted_pairs):
    if 0 < sorted_pairs[i][0][0] == sorted_pairs[i][1][0]:
        pass
    elif sorted_pairs[i][0][0] == 0 and sorted_pairs[i][1][0] == 0:
        groups[group_id] = [sorted_pairs[i][0], sorted_pairs[i][1]]
        sorted_pairs[i][0][0] = group_id
        sorted_pairs[i][1][0] = group_id
        group_id = group_id + 1
    elif sorted_pairs[i][0][0] == 0 and sorted_pairs[i][1][0] > 0:
        groups.get(sorted_pairs[i][1][0]).append(sorted_pairs[i][0])
        sorted_pairs[i][0][0] = sorted_pairs[i][1][0]
        last = multiply_x(sorted_pairs[i][0][1], sorted_pairs[i][1][1])
    elif sorted_pairs[i][0][0] > 0 and sorted_pairs[i][1][0] == 0:
        groups.get(sorted_pairs[i][0][0]).append(sorted_pairs[i][1])
        sorted_pairs[i][1][0] = sorted_pairs[i][0][0]
        last = multiply_x(sorted_pairs[i][0][1], sorted_pairs[i][1][1])
    elif sorted_pairs[i][0][0] > 0 and sorted_pairs[i][1][0] > 0:
        #merge two groups
        groups.get(sorted_pairs[i][0][0]).extend(groups.pop(sorted_pairs[i][1][0]))
        if len(groups) == 1:
            last = multiply_x(sorted_pairs[i][0][1], sorted_pairs[i][1][1])
        for item in groups.get(sorted_pairs[i][0][0]):
            item[0] = sorted_pairs[i][0][0]
    i = i + 1

print(last)