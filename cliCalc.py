# Create lists to store results and equations
historyResult = []
historyEq = []

# While loop to run until the user has finished with calc
while True:
    # Gather user input to calc
    n1 = float(input("Please enter first number: "))
    operand = input("Please pick an operator (+, -, *, /): ")
    n2 = float(input("Please pick your second number: "))
    historyEq.append(f"{n1} {operand} {n2}")

    # Get answer based off of user input
    if operand == "+":
        answer = n1 + n2
        historyResult.append(answer)
    elif operand == "-":
        answer = n1 - n2 
        historyResult.append(answer)
    elif operand == "*":
        answer = n1 * n2
        historyResult.append(answer)
    elif operand == "/":
        # Create redundancy if user tries dividing by zero
        if n2 != 0:
            answer = n1 / n2
            historyResult.append(answer)
        else:
            print("Error: division by zero!")
            continue
    else:
        print("Invalid operator!")
        continue

    # Print answer, ask for replay
    print("Answer: ", answer)
    replay = input("Would you like to do another equation? (Y/N) ")

    # Loop until user input valid
    while replay.lower() not in ["y", "n"]:
        print("Invalid option. Please type 'Y' or 'N'.")
        replay = input("Would you like to do another equation? (Y/N) ")
    if replay.lower() == "n":
        break

# Combine result and equation for complete history
history = [f"{historyEq[i]} = {historyResult[i]}" for i in range(len(historyEq))]

# Print history
print("Your Calculator history: ")
print(history)