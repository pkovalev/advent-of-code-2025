cnt = 0
cnt2 = 0
f = open("day5.txt")
lines = f.read().splitlines(False)

ranges = []
ids = []
is_ranges = True
for line in lines:
    if len(line) == 0:
        is_ranges = False
    else:
        if is_ranges:
            ranges.append(list(map(lambda x: int(x),line.split('-'))))
        else:
            ids.append(int(line))
for item in ids:
    for r in ranges:
        if item in range(r[0], r[1]+1):
            cnt = cnt + 1
            break
print(cnt)

ranges_line = []
for r in ranges:
    ranges_line.append(('a', r[0]))
    ranges_line.append(('b', r[1]))
#sort by number and then by end to start
ranges_line = sorted(ranges_line, key=lambda x: (x[1], x[0]))

start = 0
deep = 0
for item in ranges_line:
    if str(item[0]).endswith('a'):
        deep = deep + 1
        if deep == 1:
            start = item[1]
    else:
        deep = deep - 1
    if deep == 0:
        cnt2 = cnt2 + (item[1] - start) + 1
print(cnt2)
