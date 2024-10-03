def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            result = num1 + num2
            # print("The result is: ", result)

        case "subtract":
            result = num1 - num2
            # print("The result is: ", result)

        case "multiply":
            result = num1 * num2
            # print("The result is: ", result)

        case "divide":
            if num2 == 0:
                return "Cannot divide by zero."
            else:
                result = num1 / num2
                # print("The result is: ", result)
    return result
