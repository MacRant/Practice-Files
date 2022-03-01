print("°F to °C converter...")

# input captures values as a string value (aka text)
temp_to_convert = input("Enter a temperature (in °F): ")

# convert from string to float (a decimal value)
temp_to_convert_float = float(temp_to_convert)

# calculate value
temp_in_c = ((temp_to_convert_float - 32) * 5)/9

# print value
print(f"{temp_to_convert_float} °F is {temp_in_c:.2f} °C")

# the f before "" lets you put a variable inside the text you want to print
# anything inside {} has to be a variable
# things inside {} can be formatted if you put a : after it, ex:
# {temp_in_c:.2f} means print the value inside temp_in_c and format the decimal to 2 places
# temp_in_c is the variable to print, : tells python to format it and .2f tells python to format to 2 decimal places
