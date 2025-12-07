def do_step(current_line, next_line):
    for i in range(0, len(current_line)):
        if current_line[i] == -1:
            next_line[i] = current_line[i-1] + current_line[i+1]
        elif next_line[i] != -1:
            next_line[i] = current_line[i]

cnt = 0
f = open("day7.txt")
lines = f.read().splitlines(False)
prev_line = None
pos = lines[0].find('S')
for line in reversed(lines):
    #Replace empty cells with 1, splitters with -1 and start with -2
    line = list(map(lambda c: 1 if c == '.' else -2 if c == 'S' else -1, line))
    if prev_line is None:
        prev_line = line
        continue
    do_step(prev_line, line)
    prev_line = line
cnt = prev_line[pos]
print(cnt)