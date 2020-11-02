# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
level = int(input("How many levels (1 - 10?): "))

for row in range(1, level + 1):
    for column in range(1, row + 1):
        print(column, end=" ")
    print(" ")
