n = int(input("Enter N: "))

def print_numbers(current):
    if current > n:
        return
    print(current)
    print_numbers(current + 1)

print_numbers(1)
