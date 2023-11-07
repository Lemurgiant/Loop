
try:
    First_Name = input("Input your first name: ")
    Last_Name = input("Input your last name: ")
    Salary = int(input("Input your salary: "))
    Rating = int(input("Input your performance rating: "))
    Bonus = 0
    Valid_Ratings = [1, 2, 3, 4]       # Easier to check if invalid rating

    if Rating == 1:
        Bonus = Salary * 0.1
    elif Rating == 2:
        Bonus = Salary * 0.06
    elif Rating == 3:
        Bonus = Salary * 0.03
    elif Rating == 4:
        pass
        

    if Rating in Valid_Ratings:
        print(f"\nFirst Name: {First_Name}")
        print(f"Last Name: {Last_Name}")
        print(f"Salary: {Salary}")
        print(f"Rating: {Rating}")
        print(f"\n======================\n")
        print(f"Name: {First_Name} {Last_Name}")
        print(f"Salary: {Salary}")
        print(f"Rating: {Rating}")
        print(f"Bonus: {round(Bonus)}")
    else:
        print("Invalid Rating")

except ValueError:
    print("Error Values")





