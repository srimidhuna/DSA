num = input("Enter a number: ")
power = len(num)
total = sum(int(d)**power for d in num)

if total == int(num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")