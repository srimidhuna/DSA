#call by value
def add(a):
    a = a + 5
    print("Inside function:", a)
x = 10
add(x)
print("Outside function:", x)

#call by reference
def add(lst):
    lst[1] = lst[1] + lst[0]
    print("Inside function:", lst)
values = [10, 20]
add(values)
print("Outside function:", values)
