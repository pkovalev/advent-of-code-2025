def do_step(prev, current):
    splits = 0
    for i in range(0, len(prev)):
        if prev[i] == 'S' and current[i] == '^':
            splits = splits + 1
            if i > 0:
                current = current[:i-1] + 'S' + current[i:]
            if i < len(current) -1:
                current = current[:i+1] + 'S' + current[i+2:]
        elif prev[i] == 'S' and current[i] == '.':
            current = current[:i] + 'S' + current[i+1:]
    return splits, current

cnt = 0
f = open("day7.txt")
lines = f.read().splitlines(False)
prev_line = None
for line in lines:
    if prev_line is None:
        prev_line = line
        continue
    res = do_step(prev_line, line)
    cnt = cnt + res[0]
    prev_line = res[1]
print(cnt)