#Block Pattern (using Nested FOR)
rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

