def list_operations_numbers(numbers):
    summation = 0
    maximum = 0
    total_number = len(numbers)
    for number in numbers:
        summation += number
        maximum = maximum if maximum > number else number  # Direct method max(maximum,number) can be used
    return {
        "Sum": summation,
        "Average": summation / total_number,
        "Maximum": maximum,
    }

def list_operations_characters(chars):
    reversed_chars = []
    for char in reversed(chars):      # Instead of using for loop there is a direct method reverse, but I am handling it with custom logic
        reversed_chars.append(char)   # If build in method is used, it will be like:-
                                      # return chars.reverse()

    return reversed_chars


print(list_operations_numbers([1, 5, 3, 8, 2]))
print(list_operations_characters(["a", "b", "c", "d", "e"]))