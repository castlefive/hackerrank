def check_weird(n):
    if n % 2 == 0 and (n > 20 or 2 < n < 5):
        print("Not Weird")
    else:
        print("Weird")


if __name__ == '__main__':
    N = int(input())
    check_weird(N)
