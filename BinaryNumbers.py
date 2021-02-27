import re


if __name__=='__main__':
    n = int(input())
    binary_digits =[]
    reg_x = r"1+"
    while n > 0:
        rem = n % 2
        n = n//2
        binary_digits.append(rem)

    binary_string = ""
    for ob in binary_digits:
        binary_string += str(ob)

    pattern = re.compile(reg_x)
    matches = pattern.finditer(binary_string)
    longest_match = 0
    for match in matches:
        value=match.span()
        if longest_match < (value[1]-value[0]):
            longest_match = value[1] - value[0]

    print(longest_match)
