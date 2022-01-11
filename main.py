# This is a program to generate an advanced level calculator in python.
import helpers, time

constraint = 0
limit = False

while True:
    helpers.cls()
    print("Select a range.")
    print("Infinite (1) | Constrained (2)")
    inp = input("> ")

    if inp == "1": 
        helpers.cls()
        print("Selected infinite generation.")
        print("Starting to burn your pc.")

        # Almost infinite time has to pass in order to generate this file, as this requires 9.9999998e+15 operations, taking an average of 1157407 years to complete. Unless the user has a super computer or something, in which case please go do some actual useful stuff.
        limit = True
        constraint = 99999999
        break
    elif inp == "2":
        print("Enter the desired limit.")
        constraint = int(input("> "))
        limit = True
        helpers.cls()
        print("Selected constrained generation. Limit: " + str(constraint))
        print("Starting...")
        time.sleep(3)
        break
    else: 
        print("Command " + inp + " is not defined.")
        time.sleep(5)
    
operators = ["+", "-", "*", "/"]

code = ""
code += helpers.starterTemplate

print("\n------------\n")
if limit:
    for i in range(constraint):
        remaining = (constraint - i) * constraint * len(operators)
        print("Generating combinations for num1 = " + str(i) + " | Remaining operations = " + str(remaining))

        for j in range(constraint):
            for operator in operators:
                result = 0
                if operator == "+":
                    result = i + j
                elif operator == "-":
                    result = i - j
                elif operator == "*":
                    result = i * j
                elif operator == "/":
                    if j == 0:
                        result = "Not Defined"
                    else:
                        result = i / j

                generated = helpers.IfStatement(["num1 == " + str(i), "operator == '" + operator + "'", "num2 == " + str(j)], f"print('Result: {str(result)}')")
                code += generated
                code += "\n"

print("\nGeneration complete. Output file is located in /output/calculator.py\n")

with open('output/calculator.py', 'w') as file:
    file.write(code)

    
