print('Welcome to the tip calculator!')

bill = float(input('What was the total bill? $'))
tip = int(input('How much tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))

tip /= 100
each = (bill / people)
result = each * tip
final_amount = each + result
final_amount = "{:.3f}".format(round(final_amount))

print(type(final_amount))

########################################################################
#second solution:
# print('Welcome to the tip calculator!')

# bill = float(input('What was the total bill? $'))
# tip = int(input('How much tip would you like to give? 10, 12, or 15? '))
# people = int(input('How many people to split the bill? '))

# tip /= 100
# each = (bill/people)
# times = (tip + 1) * each

# print(round(times, 2))
