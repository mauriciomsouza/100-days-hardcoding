def ConvAge2Days(age):
    if type(age) is not int or age < 0:
        return "Sorry, isn't a valid value."
    else:
        return f'{age * 365} days' 

print(ConvAge2Days(-9))