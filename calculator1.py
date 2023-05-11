# This is a program for a simple calculator application taking user choice of operation and two numbers.

with open("Equations.txt", "a") as file1:
    while True:
        # Takes input from the user.
        operation = input("Enter a number for a corresponding operation (1 to add, 2 to substract, 3 to multiply or 4 to divide)? ")
        
        # Depending on the choice it calculates and writes the equation to the Equations.txt file.
        if operation in ("1", "2", "3", "4"):
            try:
                x = float(input("Please enter the first number: "))
                y = float(input("Please enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                
                continue
                                     
                   
            if operation == "1" :
                print(f"{x} + {y} = {x + y}")
                print(f"{x} + {y} = {x + y}", file=file1)

            elif operation == "2" :
                print(f"{x} - {y} = {x - y}")
                print(f"{x} - {y} = {x - y}", file=file1)

            elif operation == "3" :
                print(f"{x} * {y} = {x * y}")
                print(f"{x} * {y} = {x * y}", file=file1)
            
            elif operation == "4" :
                if y ==0:
                    raise ZeroDivisionError("Cannot divide by zero. Please enter other number than 0")
                print(f"{x} / {y} = {x / y}")
                print(f"{x} / {y} = {x / y}", file=file1)
            
            # Break the loop if user doesn't want another operation.
            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation.lower() == "yes":
                continue
            if next_calculation.lower() == "no":
                break
            else:
                print("Please enter yes or no.")

        else:
            print ("Please enter correct operation.")

# Now asking the user whether he/she wants to read all equations and results from the previously created file.
while True:
    filename = input("What is the filename to access? ")
    try:
        file2 = open(filename, "r")
        print(file2.readlines())
    except FileNotFoundError:
        print("The file does not exist. Please try again.")
        continue
    # Break the loop if the user doesn't want to check the contents of another file.    
    next_file_to_check = input("Let's check the contents of another file? (yes/no): ")
    if next_file_to_check.lower() == "yes":
        continue
    if next_file_to_check.lower() == "no":
        break
    else:
        print("Please enter yes or no.")

