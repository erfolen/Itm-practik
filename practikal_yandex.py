from sys import stdin

sum_res = 0

for line in stdin:
    a = line.rstrip('\n').split()
    sum_res += sum(list(map(int, a)))
    # sum_res += sum(map(int, line))


print(sum_res)
