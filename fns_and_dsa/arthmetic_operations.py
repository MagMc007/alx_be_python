def perform_operation(num1,num2,operation):
    match operation:
        case "add":
            return f"Result: {num1 + num2}"
        case "subtract":
            return f"Result: {num1 - num2}"
        case "multiply":
            return f"Result: {num1 * num2}"
        case "divide":
            if num2 != 0:
                return f"Result: {num1 / num2}"
            else:
                return "Cannot divide by zero"
            