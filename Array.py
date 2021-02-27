
def Main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.reverse()
    for x in A:
        print(x, end=' ')



if __name__ == '__main__':
    Main()