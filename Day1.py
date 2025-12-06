def zerosClockwise(start, steps):
    i = 0
    nextZeroAt = 100
    while start + steps > nextZeroAt:
        if start < nextZeroAt:
            i = i + 1
        nextZeroAt = nextZeroAt + 100
    return i
def zerosCCwise(start, steps):
    i = 0
    nextZeroAt = 0
    while start - steps < nextZeroAt:
        if start > nextZeroAt:
            i = i + 1
        nextZeroAt = nextZeroAt - 100
    return i
pos = 50
cnt = 0
with(open("day1.txt")) as f:
    lines = f.read().splitlines(False)
    for line in lines:
        if line[0] == 'L':
            cnt = cnt + zerosCCwise(pos, int(line[1:]))
            pos = pos - int(line[1:])
            while pos < 0:
                pos = 100 + pos
        else:
            cnt = cnt + zerosClockwise(pos, int(line[1:]))
            pos = pos + int(line[1:])
            while pos > 99:
                pos = pos - 100
        if pos == 0:
            cnt = cnt + 1
print('+++')
print(cnt)
