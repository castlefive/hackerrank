# n = 10
# x = '3 7 8 5 12 14 21 15 18 14'

n = input()
x_list = [int(i) for i in input().split(' ')]
x_list.sort()


def get_q(q_list):
    if len(q_list) % 2 == 0:
        q = int((q_list[int(len(q_list)/2)] + q_list[int(len(q_list)/2)-1]) / 2)
    else:
        q = int(q_list[int((len(q_list)-1)/2)])

    return q


q2 = get_q(x_list)

q1_list = [int(i) for i in x_list if i < q2]
q3_list = [int(i) for i in x_list if i > q2]

q1 = get_q(q1_list)
q3 = get_q(q3_list)

print(int(q1))
print(int(q2))
print(int(q3))
