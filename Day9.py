import itertools

def get_square(a: str, b: str):
    a = list(map(lambda x: int(x), a.split(',')))
    b = list(map(lambda x: int(x), b.split(',')))
    return (abs(a[0]-b[0])+1) *  (abs(a[1]-b[1]) + 1)

cnt = 0
f = open("day9.txt")
lines = f.read().splitlines(False)
pairs = list(itertools.combinations(lines, 2))
sorted_pairs = sorted(pairs, key= lambda x: get_square(x[0], x[1]))
print(get_square(sorted_pairs[-1][0], sorted_pairs[-1][1]))