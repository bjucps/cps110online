# The Chicken Feed Calculator

current_temp = int(input('Enter the temperature in degrees fahrenheit: '))
total_weight = int(input('Enter total chicken weight in pounds:'))

if current_temp < 60:
    print("It's cold! temperature =", current_temp)   # for debugging
    total_feed = total_weight * .12
elif current_temp > 90:
    print("It's hot! temperature =", current_temp)    # for debugging
    total_feed = total_weight * .08
else:
    print("It's comfortable! temperature =", current_temp) # for debugging
    total_feed = total_weight * .1

print(f"Feed them {total_feed} pounds of Robert's Best.")

