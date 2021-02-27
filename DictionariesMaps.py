
def solve():
    pass


if __name__=='__main__':
    n = int(input())
    name_number = [input().split() for _ in range(n)]
    phone_book = {k: v for k, v in name_number}
    while True:
        try:
            key = input()
            if key in phone_book.keys():
                print(f'{key}={phone_book.get(key)}')
            else:
                print("Not found")
        except:
            break