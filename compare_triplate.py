if __name__ == '__main__':
    a = [int(x) for x in input().split(" ")]
    b = [int(x) for x in input().split(" ")]
    ac = 0
    bc = 0
    for x in range(len(a)):
        if a[x] > b[x]:
            ac += 1
        elif a[x] == b[x]:
            pass
        else:
            bc += 1
    print(ac, bc)
