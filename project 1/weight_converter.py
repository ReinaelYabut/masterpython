weight = float(input("Enter weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"Your punds is {weight} {unit}")
elif unit.upper() == "L":
    weight = weight / 2.205
    unit = "Kg"
    print(f"Your kg is {weight} {unit}")
else:
    print("Invalid Unit")
    