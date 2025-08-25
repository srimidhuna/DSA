#for loop
n=int(input("Enter a number: "))
for i in range(n):
    if(i%2==0):
        print(i,"\n")

#while loop
# While loop to add numbers until total >= 20
total = 0
while total < 20:
    num = int(input("Enter a number: "))
    total = total + num
    print("Current total:", total)
print("Loop ended! Final total is:", total)

