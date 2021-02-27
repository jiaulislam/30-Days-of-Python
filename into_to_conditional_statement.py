if __name__ == '__main__':
    N = int(input())
    if N % 2 == 0:
        if N <= 5 and N >= 2:
            print("Not Weird")
        elif N >= 6 and N <= 20:
            print("Weird")
        else:
            print("Not Weird")

    else:
        print("Weird")
