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
data = list(map(lambda x: list(filter(lambda y: len(y) > 0,x.split(' '))), lines))

for i in range(0, len(data[0])):
    operation = []
    for row in range(0, len(data)):
        operation.append(data[row][i])
    if operation[-1] == '+':
        cnt = cnt + add_all(operation[:-1])
    else:
        cnt = cnt + multiply_all(operation[:-1])
print(cnt)
