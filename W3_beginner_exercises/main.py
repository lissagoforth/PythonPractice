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

# print("""a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example""")
# -----------------------------------------------------------------
# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

# import datetime
# d1 = datetime.date(2014, 7, 2)
# d2 = datetime.date(2014, 7, 11)
# ds = d2 - d1
# print(ds.days, "days")
# -----------------------------------------------------------------

# 15. Write a Python program to get the volume of a sphere with radius 6.

# import math
# r = 6
# vol = (4/3)*(math.pi * (r ** 3))
# print(round(vol, 2))
# -----------------------------------------------------------------

# 16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference

# print("Please provide a number")
# n = int(input())
# diff = abs(n-17)
# if n > 17:
#     print(diff * 2)
# else:
#     print(diff)
# -----------------------------------------------------------------

# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

# def numCheck(n):
#     return ((abs(1000-n) <= 100) or (abs(2000-n) <= 100))
# print(numCheck(900))
# print(numCheck(700))
# print(numCheck(2100))
# -----------------------------------------------------------------

# 18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.

# print("Please provide a number")
# a = int(input())
# print("Please provide another number")
# b = int(input())
# print("Last time, I swear. Please provide a number")
# c = int(input())
# def numcheck(n1, n2, n3):
#     if n1 == n2 & n2 == n3:
#         print(n1 ** 3)
#     else:
#         print("The numbers are not equal")
# numcheck(a, b, c)
# -----------------------------------------------------------------

# 19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

# print("Please provide a word")
# word = input()
# def check(s):
#     if len(s) >= 2 and (s[:2] == "Is") or s[:2] == "is":
#         print(s)
#     else:
#         s = "Is" + s
#         print(s)
# check(word)
# -----------------------------------------------------------------

# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.

# print("Please provide a word")
# word = input()
# print("Please provide a number")
# num = int(input())
# def multiply(s, n):
#     res = ""
#     for i in range(n):
#         res += s
#     print(res)
# multiply(word, num)    
# -----------------------------------------------------------------

# 21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

# print("Please provide a number")
# num = int(input())
# def even_odd(n):
#     if n % 2 == 0:
#         print(n,"is an even number!")
#     else:    
#         print(n,"is an odd number!")
# even_odd(num)
# -----------------------------------------------------------------

# 22. Write a Python program to count the number 4 in a given list.

# nums = [1,5,6,8,4,7,2,5,4,3,6,7,4] # Expected output = 3
# def count4s(n):
#     cnt=0
#     for i in n:
#        if i == 4:
#            cnt += 1
#     print(cnt)
# count4s(nums)
# -----------------------------------------------------------------

# 23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

# print("Please provide a word(or some letters)")
# s = input()
# print("Please provide a number")
# i = int(input())
# def func(w, n):
#     if len(w) <= 2:
#         print(w)
#     else:
#         res = ""
#         for x in range(n):
#             res += w[:2]
#         print(res)
# func(s,i)            
# -----------------------------------------------------------------

# 24. Write a Python program to test whether a passed letter is a vowel or not.
# print("Please provide a letter")
# letter = input()
# def isVowel(l):
#     if l.lower() == 'a' or l.lower() == 'e' or l.lower() == 'i' or l.lower() == 'o' or l.lower() == 'u':
#         print(l,"is a vowel.")
#     else:
#         print(l, "is not a vowel.")
# isVowel(letter)
# -----------------------------------------------------------------

# 25. Write a Python program to check whether a specified value is contained in a group of values.
# Test Data: 
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

# print("Please provide a number")
# i = int(input())
# nums = [1, 5, 8, 3]
# def exists(x, arr):
#     for j in arr:
#         if x == j:
#             return True
#     return False
# print(exists(i, nums))
# -----------------------------------------------------------------

# 26. Write a Python program to create a histogram from a given list of integers.

# nums = [1,5,6,8,4,7]
# def graphIt(arr):
#     for n in arr:
#         output = ''
#         times = n
#         while (times>0):
#             output += '*'
#             times -= 1
#         print(output)
# graphIt(nums)
# -----------------------------------------------------------------

# 27. Write a Python program to concatenate all elements in a list into a string and return it.

# stuff = ["this", "is", "a", "list", "of", "some", "words"]
# seperator = " "
# seperator = seperator.join(stuff)
# print(seperator)
# # -----------------------------------------------------------------

# 28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]

# def find_evens(arr):
#     for i in arr:
#         if i % 2 == 0:
#             print(i)
#         if i == 237:
#             break
# find_evens(numbers)             
# -----------------------------------------------------------------

# 29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.
# Test Data : 
# color_list_1 = set(["White", "Black", "Red"]) 
# color_list_2 = set(["Red", "Green"])
# # Expected Output : 
# # {'Black', 'White'}

# def get_diff(a,b):
#     return (list(set(a) - set(b)))
# print(get_diff(color_list_1, color_list_2))
# -----------------------------------------------------------------

# 30. Write a Python program that will accept the base and height of a triangle and compute the area
# print("Lets find the area of a triangle! Provide a number for the base.")
# base = int(input())
# print("Okay, now provide a height")
# height = int(input())
# def area(b,h):
#     return (b * h)/2
# print(area(base, height))
# -----------------------------------------------------------------

# 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers
# print("Let's find the the greatest common divisor. Please provide a number.")
# n1 = int(input())
# print("We still need one more number.")
# n2 = int(input())
# def gcd(x, y):
#     res = 1
#     if x % y == 0:
#         return y
#     for i in range(int(y/2), 0, -1):
#         if x % i == 0 and y % i == 0:
#             res = i
#             break
#     return res
# print(gcd(n1,n2))        
# -----------------------------------------------------------------

# 32. Write a Python program to get the least common multiple (LCM) of two positive integers.
# print("Let's find the the least common multiple. Please provide a number.")
# n1 = int(input())
# print("We still need one more number.")
# n2 = int(input())
# def lcm(x,y):
#     if x>y:
#         n = x
#     else:
#         n = y
#     while(True):
#         if((n%x == 0) and (n%y == 0)):
#             res = n
#             break
#         n += 1
#     return res
# print(lcm(n1,n2))
# -----------------------------------------------------------------

# 33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero
# print("Let's have fun with numbers! Gimme one.")
# n1 = int(input())
# print("Gimme another one.")
# n2 = int(input())
# print("Gimme one more.")
# n3 = int(input())
# def fun(x,y,z):
#     if (x==y) or (x==z) or (y==z):
#         return 0
#     else:
#         return x + y + z
# print(fun(n1,n2,n3))
# -----------------------------------------------------------------

# 34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
# print("Let's have fun with numbers! Gimme one.")
# n1 = int(input())
# print("Gimme another one.")
# n2 = int(input())
# def scope(x,y):
#     if (x+y) <= 20 and (x+y) >= 15:
#         return 20
#     else:
#         return x+y
# print(scope(n1,n2))
# -----------------------------------------------------------------

# 35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
# print("Let's have fun with numbers! Gimme one")
# n1 = int(input())
# print("Gimme another one.")
# n2 = int(input())
# def test(x,y):
#     if (x == y) or (x + y == 5) or (abs(x - y) == 5):
#         return True
#     else:
#         return False
# print(test(n1,n2))
# -----------------------------------------------------------------

# 36. Write a Python program to add two objects if both objects are an integer type.
# def add_em(x,y):
#     if not (isinstance(x,int) and isinstance(y,int)):
#         raise TypeError("I NEED NUMBERS TO ADD, FOOL, NOT STRINGS OR SOME SHIT")
#     return x + y
# print("What is 2+5?", add_em(2,5))
# print("What is cat + dog?", add_em("cat","dog"))
# -----------------------------------------------------------------

# 37. Write a Python program to display your details like name, age, address in three different lines.
# print("What's your name?")
# name=input()
# print("How old are you?")
# age=int(input())
# print("What's your address?")
# address=input()
# print("To summarize: \nName:", name, "\nAge:", age, "\nAddress:", address)
# #alternative solution
# print("To summarize: \nName: {}\nAge: {}\nAddress: {}".format(name, age, address))
# -----------------------------------------------------------------

# 38. Write a Python program to solve (x + y) * (x + y).
# Test Data : x = 4, y = 3
# Expected Output : (4 + 3) ^ 2) = 49
print("Give me a number, any number.")
n1 = int(input())
print("Give me another number.")
n2 = int(input())
def maths(x,y):
    return (()**)

# -----------------------------------------------------------------

# 39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79
# -----------------------------------------------------------------

# 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
# -----------------------------------------------------------------

# 41. Write a Python program to check whether a file exists.
# -----------------------------------------------------------------

# 42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
# -----------------------------------------------------------------

# 43. Write a Python program to get OS name, platform and release information.
# -----------------------------------------------------------------

# 44. Write a Python program to locate Python site-packages.
# -----------------------------------------------------------------

# 45. Write a python program to call an external command in Python.
# -----------------------------------------------------------------

# 46. Write a python program to get the path and name of the file that is currently executing.
# -----------------------------------------------------------------

# 47. Write a Python program to find out the number of CPUs using.
# -----------------------------------------------------------------

# 48. Write a Python program to parse a string to Float or Integer. 
# -----------------------------------------------------------------

# 49. Write a Python program to list all files in a directory in Python. 
# -----------------------------------------------------------------

# 50. Write a Python program to print without newline or space.
# -----------------------------------------------------------------

# -----------------------------------------------------------------




























