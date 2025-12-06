def get_if_fake(str):
    strlen = len(str)
    if strlen % 2 > 0:
        return 0
    if str[:strlen//2] == str[strlen//2:]:
        return int(str)
    else:
        return 0

def get_if_fake2(str):
    strlen = len(str)
    for chunk_length in range(1, strlen//2 + 1):
        made_str = str[:chunk_length] * (strlen // chunk_length)
        if made_str == str:
            print("found " + str)
            return int(str)
    return 0

cnt = 0
cnt2 = 0
f = open("day2.txt")
line = f.read()
pairs = line.split(',')
for pair in pairs:
    nums = pair.split('-')
    for i in range(int(nums[0]), int(nums[1]) + 1):
        cnt = cnt + get_if_fake(str(i))
        cnt2 = cnt2 + get_if_fake2(str(i))
print(cnt)
print(cnt2)
