# Declare my variables
miles = input("Enter the number of miles: ")
yards = input("Enter the number of yards: ")
feet = input("Enter the number of feet: ")
inches = input("Enter the number of inches: ")

# Convert the user input string into their int values
miles = int(miles)
yards = int(yards)
feet = int(feet)
inches = int(inches)

# Declare my formulas:
# Convert all of users input to inches
totalInches = (63360 * miles + 36 * yards + 12 * feet + inches)

# Convert total inches into a metric unit of measurement
totalMetres = (totalInches / 39.37)

# Set kilometres equal to the whole number of totalMetres / 1000
kilometres = int(totalMetres / 1000)

# Set metres equal to the whole number of the remainder of totalMetres / 1000
metres = int(totalMetres % 1000)

# Create a second metres variable to get centimetres
metres1 = totalMetres % 1000

# Set centimetres equal to the rounded number of the remainder of (metres1*100) / 100 , one decimal to the right
centimetres = round((metres1*100)%100,1)

# Print the converted values to the user
print("\nThe metric length is " + str(kilometres) + " kilometres, " + str(metres) + " metres, and " + str(centimetres) + " centimetres.")
