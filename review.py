def getEvenOddString(strings):
    oddString = ''
    for x in range(len(strings)):
        if x % 2 == 0 or x == 0:
            print(strings[x], end = '')
        else:
            oddString += strings[x]
    print("", oddString, end= '')
    print()
def Main():
    T = int(input())
    strings = []
    for x in range(T):
        strings.append(input())

    for x in range(T):
        getEvenOddString(strings[x])
        

if __name__ == "__main__":
    Main()