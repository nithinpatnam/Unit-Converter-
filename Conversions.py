#Unit Conversions Project
print("** Unit Conversions**")
conversions_available=[(1,'km','mi'),
                       (2,'mi','km'),
                       (3,'kg','lbs'),
                       (4,'lbs','kg'),
                       (5,'°F','°C'),
                       (6,'°C','°F')]
#Used to display the contents to select from the user for the COnversions of values
print("Conversions Available:")
for conversion_number,from_unit,to_unit in conversions_available:
    print(f'{conversion_number}){from_unit} -> {to_unit}')

#Asking the User Input for the Conversion of the Values
conversion=input("Enter the number of conversion to use -->")
if not conversion.isdigit():
    print('Invalid Input,Please Enter a Number')
else:    
    #This is because if the user selects 1 then it goes to 2 in the Conversions Availabel because it starts from the 0th index
    conversion_index=int(conversion)-1
    if conversion_index < 0 or conversion_index>=len(conversions_available):
        print("Invali Input,Please enter a valid number from the list.")
    else:
            conversion_number,from_unit,to_unit=conversions_available[conversion_index]
            #This helps in asking the user input value of conversions like 0 degree celcius or 1 degree celcius 
            from_value=float(input("Enter{from_unit} -->"))

            #This is Used to Check the conditions according to the given input

            if conversion_number==1:
                to_value=from_value * 0.62
            elif conversion_number==2:
                to_value=from_value * 1.61
            elif conversion_number==3:
                to_value=from_value* 2.205    
            elif conversion_number==4:
                to_value=from_value * 0.4536
            elif conversion_number==5:
                to_value=(from_value-32)/1.8
            elif conversion_number==6:
                to_value=from_value * 1.8+32
            #Printing the Result As an Output
            print(f'{from_value} {from_unit} -> {to_value} {to_unit}')