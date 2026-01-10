# Program Name: Quinary-Decimal Converter
# Author: Tavonga Tawodzera
# Date: 2025-09-30
# Description: This program converts numbers between quinary (base 5) and decimal (base 10).
# The user chooses the conversion type. Loops and selection statements are used as required.


# added loop so program keeps running until user quits
while True:   
    conversion_type = input("\nEnter conversion type: quinary to decimal (q), decimal to quinary (d), or exit (x): ")

    if conversion_type.lower() == 'x':  
        print("Goodbye!")
        break

    if conversion_type.lower() == 'q':
        quinary_number = int(input("Enter a number whose digits range from 0 to 4: "))
        
        decimal_number = 0  
        power = 0           
        
        while quinary_number > 0:
            remainder = quinary_number % 10
            decimal_number += remainder * (5 ** power)
            quinary_number //= 10
            power += 1

        print("The decimal of your number is:", decimal_number)

    elif conversion_type.lower() == 'd':
        decimal_number = int(input("Enter a decimal number: "))
        
        quinary_string = ""
        
        while decimal_number > 0:
            remainder = decimal_number % 5
            quinary_string = str(remainder) + quinary_string
            decimal_number //= 5

        print("The quinary of your number is:", quinary_string)

    else:
        print("Invalid choice. Please enter 'q', 'd', or 'x'.")   
