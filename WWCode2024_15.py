# Women Who Code (Python) Challenge No. 15
# Create a program that checks if a year is a leap year.

# The rules for a leap year according to the Gregorian Calendar:
    #1. The year is evenly divisible by 4 but not 100, or...
    #2. The year is evenly divisible by 400.

# Function
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Get year from user
year = int(input("Enter a year to check if it's a leap year: "))

# Get and print results
if leap_year(year) == True:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


'''
List of leap years to test:
1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024

List of non leap years to test:
1977, 1981, 1985, 1989, 1993, 1997, 2001, 2005, 2009, 2013, 2017, 2021, 2025
'''
