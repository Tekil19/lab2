def leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
     print("this is a leap year.")
    else:
     print("this is not a leap year.")

x=int(input("enter a year:"))
leap(x)
