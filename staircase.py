def staircase(var):
    count = var - 1
    for x in range(0, var):
        for i in range(var):
            if i < count:
                print(" ", end='')
            else:
                print("#", end='')
        print("")
        count -= 1


if __name__ == '__main__':
    N = int(input())
    staircase(N)