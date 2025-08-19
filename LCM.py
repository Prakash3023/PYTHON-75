#LCM (using WHILE-INFINITE loop)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

greater = max(a, b)

while True:
    if greater % a == 0 and greater % b == 0:
        print("LCM is:", greater)
        break
    greater += 1
