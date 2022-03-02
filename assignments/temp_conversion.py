#temp input

temp = float(input("Input a temperature in fahrenheit or celcius below: "))

temp_type = str(input("Is the temperture above in fahrenheit or celcius? Type 'f' for fahrenheit, and 'c' for celcius: "))

#conversion calc

if temp_type == "c":
    temp_final = str((temp * (9/5) + 32))
    
elif temp_type == "f":
    temp_final = str((temp - 32) * (5/9))

print("Your temperature is " + temp_final)

