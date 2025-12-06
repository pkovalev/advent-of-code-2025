def process_block(block, operator):
    data = list(filter(lambda f: len(f) > 0,map(lambda x: x.strip(), block)))
    if operator == '*':
        return multiply_all(data)
    if operator == '+':
        return add_all(data)
    return 0

def add_all(operands):
    return sum(map(lambda x: int(x), operands))

def multiply_all(operands):
    res = 1
    for x in operands:
        res = res * int(x)
    return res

cnt = 0
f = open("day6.txt")
lines = f.read().splitlines(False)
block = []
prev_operator = ''
for i in range(0,len(lines[0])):
    if lines[-1][i] == '*' or lines[-1][i] == '+':
        cnt = cnt + process_block(block, prev_operator)
        block = []
        prev_operator = lines[-1][i]
    vline = ''
    for row in range(0, len(lines)-1):
        vline = vline + lines[row][i]
    block.append(vline)
cnt = cnt + process_block(block, prev_operator)
print(cnt)
