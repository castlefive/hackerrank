n = 5
x = '10 40 30 50 20'
f = '1 2 3 4 5'

# n = int(input())
# x_list = [int(i) for i in input().split(' ')]
# f_list = [int(i) for i in input().split(' ')]

x_list = [int(i) for i in x.split(' ')]
f_list = [int(i) for i in f.split(' ')]


def get_q(q_list):
    if len(q_list) % 2 == 0:
        q = int((q_list[int(len(q_list)/2)] + q_list[int(len(q_list)/2-1)]) / 2)
    else:
        q = int(q_list[int((len(q_list)-1)/2)])

    return q


s_list = []
for i in range(0, len(f_list)):
    for j in range(0, int(f_list[i])):
        s_list.append(x_list[i])

s_list.sort()

if len(s_list) % 2 == 0:
    middle = int(sum(f_list) / 2)
else:
    middle = int(sum(f_list) / 2) + 1

q1_list = s_list[:middle]
q3_list = s_list[middle:]

q1 = get_q(q1_list)
q3 = get_q(q3_list)

print(float(q3-q1))
