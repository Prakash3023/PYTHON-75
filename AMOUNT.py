#we are supposed to return the sum if the input is 0 and we should not consider the input which is less than 40 and greater than 100
total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    
    if num == 0:
        break  
    
    if 40 <= num <= 100:    
        total += num

print("Sum of valid numbers is:", total)
