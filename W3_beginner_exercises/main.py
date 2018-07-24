# 1. Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are

# print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")
# -----------------------------------------------------------------

# 2. Write a Python program to get the Python version you are using.

# import sys
# print("Python Version: ", sys.version)
# print("Version Info: ", sys.version_info)
# -----------------------------------------------------------------

# 3. Write a Python program to display the current date and time.
# Sample Output : 
# Current date and time : 
# 2014-07-05 14:34:14

# import datetime
# print("Current date and time: ", datetime.datetime.now())
# -----------------------------------------------------------------

# 4. Write a Python program which accepts the radius of a circle from the user and compute the area.
# Sample Output : 
# r = 1.1
# Area = 3.8013271108436504

# import math
# r = 1.1
# area = math.pi * (r ** 2)
# print("r = ", r)
# print("Area = ", area)
# -----------------------------------------------------------------

# 5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
 
# print("Please provide your first name")
# Fname = input()
# print("Please provide your last name")
# Lname = input()
# print(Lname +" "+ Fname)
# -----------------------------------------------------------------

# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output : 
# List : ['3', ' 5', ' 7', ' 23'] 
# Tuple : ('3', ' 5', ' 7', ' 23')

# print("Please provide 4 random numbers")
# a,b,c,d = [input(),input(),input(),input()]
# numlist = [a,b,c,d]
# numtup = (a,b,c,d)
# print("List: ", numlist)
# print("Tuple: ", numtup)
# -----------------------------------------------------------------

# 7. Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java 
# Output : java

# print("Please provide a filename")
# file = input()
# ext = file.split('.')[1]
# print("File Extension: ", ext)
# -----------------------------------------------------------------

# 8. Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]

# color_list = ["Red","Green","White" ,"Black"]
# first = color_list[0]
# last = color_list[-1]
# print("First: ", first, "\nLast: ", last)
# -----------------------------------------------------------------

# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

# exam_st_date = (11, 12, 2014)
# print("The exam starts on: %i/%i/%i"%exam_st_date)
# -----------------------------------------------------------------

# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5 
# Expected Result : 615 => 5+55+555

# print("Please provide a number")
# n = int(input())
# n1 = int( "%s" % n ) 
# n2 = int( "%s%s" % (n,n) )
# n3 = int( "%s%s%s" % (n,n,n) )
# print(n1+n2+n3)
# -----------------------------------------------------------------

# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
# Sample function : abs()
# Expected Result : 
# abs(number) -> number
# Return the absolute value of the argument.

# print(abs.__doc__)
# -----------------------------------------------------------------

# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

# import calendar
# print("What year is it?")
# y = int(input())
# print("What month is it? (ex. 7 for July)")
# m = int(input())
# print(calendar.month(y,m))
# -----------------------------------------------------------------

# 13. Write a Python program to print the following here document.
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example


# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------
# -----------------------------------------------------------------




























