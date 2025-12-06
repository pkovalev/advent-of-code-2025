def biggest_and_pos(line, start, end):
    biggest = -1
    pos = -1
    for i in range(start, end):
        if int(line[i]) > biggest:
            pos = i
            biggest = int(line[i])
    return (biggest, pos)

cnt = 0
#Part 1
#digits_number = 2
#Part 2
digits_number = 12
f = open("day3.txt")
lines = f.read().splitlines(False)
for line in lines:
    res_str = ""
    start = 0
    for i in range(0, digits_number):
        res = biggest_and_pos(line, start, len(line) - digits_number + i + 1)
        start = res[1] + 1
        res_str = res_str + str(res[0])
    cnt = cnt + int(res_str)
print(cnt)