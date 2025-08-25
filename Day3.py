#array
arr = eval(input("Enter an integer array: "))
maximum = max(arr)
minimum = min(arr)
print("Maximum element in the array:", maximum)
print("Minimum element in the array:", minimum)

#string
s = input("Enter a string: ")
is_palindrome = True
for i in range(len(s) // 2):
    if s[i] != s[-(i+1)]:
        is_palindrome = False
        break
if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")
