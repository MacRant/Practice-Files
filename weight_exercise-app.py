#Weight Converter

#Variables
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', ',']
weight_list = []
compare_success = []

weight = input('Weight: ')

def weight_list_create():
    #weight_list function--adds each item in weight string to a list
    for item in weight:
        weight_list.append(item)

# # #Determine if weight is a valid number
def weight_numbers_compare():
    for values in weight_list:
        if values in numbers:
            compare_success.append(1)
            print(compare_success)
        else:
            print("Invalid value. Use numerical values only. Try again.")
            weight_input()


weight_list_create()
weight_numbers_compare()
    
    

# #Determines if previous input is Kg or Lbs
# k_or_l = input("(K)g or (L)bs: ")


# #Converts any input from k_or_l into upper case
# k_or_l = k_or_l.upper()

# #Conversion
# if k_or_l == "K":
#     print("Weight in Lbs = " + str(float(weight) / 0.45))
# elif k_or_l == "L":
#     print("Weight in Kg: " + str(float(weight) * 0.45))
# else:
#     print("Not a valid value. Re-run and try again.")
    
