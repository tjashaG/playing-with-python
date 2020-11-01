number = int(input("Pick a number between 1 and 100:\n"))

for element in range(1, number + 1,):
    if element % 5 == 0 and element % 3 == 0:
        print("fizzbuzz")
    elif element % 5 == 0:
        print("buzz")
    elif element % 3 == 0:
        print("fizz")
    else:
        print(element)
