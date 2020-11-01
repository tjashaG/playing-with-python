print("Welcome to unit converter!")

wants_to_continue = True
while wants_to_continue is True:
    option = float(input("Type 1 for speed, 2 for distance, 3 for area and 4 for weight: "))
    if option == 1:
        convert = float(input("Type 1 to convert MPH to KPH. Type 2 for KPH to MPH: "))
        if convert == 1:
            speed = float(input("Enter the speed in MPH: "))
            print(f"{speed} mph is {round((speed * 1.609), 2)} kph")
        else:
            speed = float(input("Enter the speed in KPH: "))
            print(f"{speed} kph is {round((speed / 1.609), 2)} mph")
    elif option == 2:
        convert = float(input("Type 1 to convert FT to M and 2 for M to FT: "))
        if convert == 1:
            distance = float(input("Enter distance in FEET: "))
            print(f"{distance} feet is {round((distance / 3.281), 2)} meters")
        else:
            distance = float(input("Enter distance in METERS: "))
            print(f"{distance} meters is {round((distance * 3.281), 2)} feet")
    elif option == 3:
        convert_area = float(input("Type 1 for FT2 to M2 and 2 for M2 to FT2: "))
        if convert_area == 1:
            area = float(input("Enter area in SQ FEET: "))
            print(f"{area} square feet is {round((area / 10.764), 2)} square meters")
        else:
            area = float(input("Enter area in SQ METERS: "))
            print(f"{area} square meters is {round((area * 10.764), 2)} square feet")
    else:
        convert_weight = float(input("Type 1 for LB to KG and 2 for KG to LB: "))
        if convert_weight == 1:
            weight = float(input("Enter weight in pounds: "))
            print(f"{weight} pounds is {round((weight / 2.205), 2)} kilos")
        else:
            weight = float(input("Enter weight in kg: "))
            print(f"{weight} kilograms is {round((weight * 2.205), 2)} pounds")
    wants_to_continue = input("Do you want to do any more conversions?(y/n): ")
    if wants_to_continue == "n":
        wants_to_continue = False
        print("Thank you for using this converter! Bye-bye!")
    else:
        wants_to_continue = True
