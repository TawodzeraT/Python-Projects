# Program name: milesToKms.py
#
#Function
#This program converts miles to kilometers
#

KMS_PER_MILE = 1.609

#Prompt and read miles
milesStr = input("Enter distance in miles as a number: ")
miles = float(milesStr)

#Calculaute kilometers
kms = KMS_PER_MILE * miles

# Display kilometer to the screen
print("The miles your entered areb equal to", f'{kms:.2f}',"kilometers")
