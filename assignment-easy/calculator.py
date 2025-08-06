def calculator(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 / number2
    return None

print(calculator(15, 3, "+"))
print(calculator(15, 3, "-"))
print(calculator(15, 3, "*"))
print(calculator(15, 3, "/"))