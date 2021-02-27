def loop(num):
    for x in range(1, 11):
        multiply = num * x
        print(f"{num} x {x} = {multiply}")

def Main():
    my_input = int(input())
    loop(my_input)


if __name__ == "__main__":
    Main()
