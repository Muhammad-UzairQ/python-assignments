import re

def validate(value, data_type):
    if data_type == 'int':
        try:
             int(value)
             return True
        except ValueError:
            return False
    elif data_type == 'float':
        try:
             float(value)
             return True
        except ValueError:
            return False
    elif data_type == 'email':
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, value) is not None
    else:
        return None

print(validate("uzair", "int"))
print(validate("1501", "int"))
print(validate("Ali", "float"))
print(validate("100_00", "float"))
print(validate("184.24", "float"))
print(validate("uzair@emumba.com", "email"))
print(validate("emumba.com", "email"))