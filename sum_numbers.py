# Exercise Question 3: Accept number from user and calculate the sum
# of all number between 1 and given number
# For example user given 10 so the output should be 55

users_number = int(input("Pick a number, any number: "))
result = 0
for num in range(1, users_number + 1):
    result += num
print(f"The sum of all numbers up to and including {users_number} is {result}")
