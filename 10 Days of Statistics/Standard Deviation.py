import math

n = 10.0
x = '64630 11735 14216 99233 14470 4978 73429 38120 51135 67060'

# n = float(input())
# x_list = [int(i) for i in input().split(' ')]
x_list = [int(i) for i in x.split(' ')]
x_list.sort()

mean = int(sum(x_list) / n)

total = 0
for i in x_list:
    total += (i - mean) ** 2

print(round(math.sqrt(total / n), 1))

