#if-else
num=int(input("Enter a number:"))
if num > 0:
    print("Number is positive")
else:
    print("Number is negative or zero")


#switch statements
day = input("Enter a day : ")
match day:
    case "Monday":
        print("Start of the week")
    case "Friday":
        print("End of the week")
    case _:
        print("Midweek day")

