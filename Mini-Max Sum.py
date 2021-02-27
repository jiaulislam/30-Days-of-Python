def min_max_sum(my_arr):
    value = []
    for x in range(len(my_arr)):
        sums = 0
        for j in range(len(my_arr)):
            if x == j:
                continue
            else:
                sums += my_arr[j]
        value.append(sums)
    return value


if __name__ == '__main__':
    my_arr = [int(x) for x in input().split(" ")]
    lst = min_max_sum(my_arr)
    lst.sort()
    minV = lst[0]
    maxV = lst[4]
    print(minV, maxV)
