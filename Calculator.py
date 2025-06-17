def add(P, Q):
    return P+ Q
def substract(P, Q):
    return P -Q
def multiply(P, Q):
    return P * Q
def divide(P, Q):
    return P / Q

print("Please Select The Operation.")
print("a. Add")
print("b. Substract")
print("c. Multiply")
print("d. Divide")

choice= input("Pleasr Enter an Operation: ")

num_1= int(input("Please Enter The First Number: "))
num_2= int(input("Please Enter The Second Number: "))

if choice == 'a':
    print(num_1, " + ", num_2, " = ", add(num_1, num_2))

elif choice == 'b':
    print(num_1, " - ", num_2, " = ", substract(num_1, num_2))

elif choice == 'c':
    print(num_1, " * ", num_2, " = ", multiply(num_1, num_2))

elif choice == 'd':
    print(num_1, " / ", num_2, " = ", divide(num_1, num_2))

else:
    print("This is an invalid input!!!")