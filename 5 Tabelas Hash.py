# Rick Leal


n = int(input())
check = 0

while n:
    n -= 1
    # lista compreensiva ou lambda
    m, c = [int(x) for x in input().split()]
    hash = {str(x) : [] for x in range(m)}
    entrada = [int(x) for x in input().split()]

    if check:
        print()
    # sempre pelo resto
    for i in entrada:
        resto = i % m
        hash[str(resto)].append(int(i))

    for i in hash:
        print('%d -> ' % int(i), end = '')
        for j in hash[i]:
            print('%d -> ' % j, end = '')
        # duas barras para aparecer só uma (funcuntion \n)
        print('\\')

    check = 1
