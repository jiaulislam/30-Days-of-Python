def get_fraction(number, size):
    var = float(number)/float(size)
    print(f"{var: .6f}")


if __name__ == '__main__':
    N = int(input())
    my_arr = [int(x) for x in input().split(' ')]
    positive_fraction = 0
    negative_fraction = 0
    zero_fraction = 0
    for i in range(len(my_arr)):
        if my_arr[i] > 0:
            positive_fraction += 1
        elif my_arr[i] < 0:
            negative_fraction += 1
        else:
            zero_fraction += 1

    get_fraction(positive_fraction, len(my_arr))
    get_fraction(negative_fraction, len(my_arr))
    get_fraction(zero_fraction, len(my_arr))
