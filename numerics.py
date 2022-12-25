def has_numbers(inputString):
    return any(char.isdigit() for char in inputString if char !="." )
x=has_numbers("rahul.us.us234 .uds")
print(x)