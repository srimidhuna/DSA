num = input("Enter a number to check palindrome: ")
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

a = int(input("Enter first number for GCD: "))
b = int(input("Enter second number for GCD: "))

while b != 0:
    a, b = b, a % b

print("GCD is:", a)
