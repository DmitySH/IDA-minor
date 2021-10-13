fin = open('input.txt', 'r', encoding='utf-8')

nums = [0] * 99

for line in fin:
    sp_line = list(map(int, line.split()[2:]))

    nums[sp_line[0] - 1] += 1
for i in range(99):
    if nums[i] == max(nums):
        print(i + 1, end=' ')
