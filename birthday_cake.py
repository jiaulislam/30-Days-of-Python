def find_max(my_ar):
    arrSo.sort()
    max_m = max(my_ar)
    count_elem = arrSo.count(max_m)
    return count_elem


if __name__ == '__main__':
    n = int(input())
    arrSo = [int(x) for x in input().split(" ")]
    maxNumber = find_max(arrSo)
    print(maxNumber)
