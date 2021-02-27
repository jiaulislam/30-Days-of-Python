if __name__ == '__main__':
    n = int(input().strip())
    a = []
    for x in range(n):
        a.append(list(map(int, input().rstrip().split())))

    primary, secondary = 0, 0

    for i in range(len(a)):
        primary += a[i][i]
        secondary += a[i][len(a) - i - 1]
        
    print(f"{abs(primary - secondary)}")