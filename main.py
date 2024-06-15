# This function determines whether the given year is a leap year or not.
def is_year_leap(year):
    if year % 10 == 0:
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 == 0:
                return True
            else:
                return False          
    else:
        if year % 4 == 0:
            return True
        else:
            return False
# This function returns the number of days in a given month for a specified year, correctly accounting for leap years.
def days_in_month(year, month):
    
  if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31  
    else:
        return 30
    
#test case
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("Passed!")
	else:
		print("Failed!")
