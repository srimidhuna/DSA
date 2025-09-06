def print_name(n, name):
    if n == 0:
        return
    print(name)
    print_name(n - 1, name)

name = input("Enter your name: ")
n = int(input("Enter how many times to print: "))
print_name(n, name)
