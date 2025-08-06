def convert_temperature(temperature,unit):
    if unit == 'Celsius':
        temperature = (temperature - 32) * 5/9
        return str(temperature) + " Celsius"
    elif unit == 'Fahrenheit':
        temperature = temperature * 1.8 + 32
        return str(temperature) + " Fahrenheit"
    return None

print(convert_temperature(15,"Fahrenheit"))
print(convert_temperature(15,"Celsius"))