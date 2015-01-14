# Chloe's time conversion. Converts seconds to minutes and hours
print("Chloe's time conversion program: converts seconds into minutes and hours.")
seconds = int(input("Enter any number of seconds to convert to both minutes and hours: "))
minutes = seconds / 60 #60 seconds in a minute
hours = minutes / 60 # 60 minutes in a hour
print(str(seconds) + ' seconds is ' + str(minutes) + 'minutes.') # prints minutes conversion
print(str(seconds) + ' seconds is ' + str(hours) + 'hours.') # prints hours