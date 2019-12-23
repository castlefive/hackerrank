# n = '10'
# x = '64630 11735 14216 99233 14470 4978 73429 38120 51135 67060'

n = int(input().strip())

x_list = [int(i) for i in input().strip().split(' ')]
x_list.sort()


def get_mean(n, x_list):
    mean = sum(x_list) / n
    return mean


def get_median(n, x_list):
    if n % 2 == 0:
        median = (x_list[int(n / 2)] + x_list[int(n / 2) - 1]) / 2
    else:
        median = x_list[int(n - 1) / 2] / 2

    return median


def get_mode(x_list):
    count_list = []

    for i in x_list:
        count_list.append(x_list.count(i))

    if max(count_list) > 1:
        mode = x_list[count_list.index(max(count_list))]
    else:
        mode = min(x_list)
    return mode


print(get_mean(n, x_list))
print(get_median(n, x_list))
print(get_mode(x_list))
