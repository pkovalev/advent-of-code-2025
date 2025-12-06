import copy

def get_surrounding(col:int, row:int):
    res = 0
    if map[col - 1][row - 1] == '@': res = res + 1
    if map[col - 1][row] == '@': res = res + 1
    if map[col - 1][row + 1] == '@': res = res + 1
    if map[col][row - 1] == '@': res = res + 1
    if map[col][row + 1] == '@': res = res + 1
    if map[col + 1][row - 1] == '@': res = res + 1
    if map[col + 1][row] == '@': res = res + 1
    if map[col + 1][row + 1] == '@': res = res + 1
    return res

cnt = 0
f = open("day4.txt")
lines = f.read().splitlines(False)

#extend
width = len(lines[0])
height = len(lines)
map = ['.' * (width + 2)]
for line in lines:
    map.append('.' + line + '.')
map.append('.' * (width + 2))
new_map = copy.deepcopy(map)
while True:
    prev_cnt = cnt
    for col in range(1, width + 1):
        for row in range(1, height + 1):
            if map[col][row:row+1] == '@' and get_surrounding(col, row) < 4:
                cnt = cnt + 1
                new_map[col] = new_map[col][:row] + '.' + new_map[col][row+1:]
    if prev_cnt == cnt:
        break
    map = copy.deepcopy(new_map)
print(cnt)