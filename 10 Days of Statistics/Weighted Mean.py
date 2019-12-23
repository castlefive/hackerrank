# n 5
# x 10 40 30 50 20
# w 1 2 3 4 5

n = int(input())
x_list = [int(i) for i in input().split(' ')]
w_list = [int(i) for i in input().split(' ')]

son = 0
mother = 0

for i in range(0, n):
    son += x_list[i] * w_list[i]
    mother += w_list[i]

print(round(son/mother, 1))