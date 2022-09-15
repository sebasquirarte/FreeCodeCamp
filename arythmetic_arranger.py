# Sebastian Quirarte | sebastianquirajus@gmail.com | 15 Sep 22
# Part of FreeCodeCamp: Scientific Computing with Python

# Defines a function that can display and solve basic arithmetic operations.

# Usage ex.1: arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]).
# Usage ex.2: arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True).
# Optional second argument, if True will print answers.

# PSEUDOCODE
# 1. Verify conditions are met and prepare appropriate error messages.
# 2. Verify if answer will be printed.
# 3. If needed, calculate answers.
# 4. Display operations with or without answers.

def arithmetic_arranger(problems):
    count = 0
    #Splits values from each operation
    for i in problems:
        problems_pieces = problems[count].split()
        value1 = problems_pieces[0]
        value2 = problems_pieces[2]
        op = problems_pieces[1]
        # Determines amount of spaces needed to line up operation
        if value1 > value2 or value1 == value2:
            length = len(value1)
        else:
            length = len(value2)

        # Calcultaing answer to problem
        if op == "+":
            answer = int(value1) + int(value2)
        elif op == "-":
            answer = int(value1) - int(value2)

        print("  " + value1 + "\n" + op + " " + value2 + "\n-----\n  " + str(answer))
        print()
        count += 1

#return arranged_problems

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
