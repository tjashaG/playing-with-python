# Exercise Question 11: Python program to display all the prime numbers within a range
# Note: A Prime Number is a whole number that cannot be made by multiplying other whole numbers
start, stop = input("Enter the START and END point: ").split()

for number in range(int(start), int(stop)):
    if number in (2, 3, 5, 7, 11):
        print(number)
    elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0 or number % 11 == 0:
        continue
    else:
        print(number)

# Official solution below

start = 25
end = 50
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    # all prime numbers are greater than 1
    # if number is less than or equal to 1, it is not prime
    if num > 1:
        for i in range(2, num):
            # check for factors
            if (num % i) == 0:
                # not a prime number so break inner loop and
                # look for next number
                break
        else:
            print(num)
