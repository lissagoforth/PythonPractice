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
#   
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
#             
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
#              
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
#         
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
# print("Give me a number, any number.")
# n1 = int(input())
# print("Give me another number.")
# n2 = int(input())
# def maths(x,y):
#     return ((x+y)** 2)
# print(maths(n1,n2))

# -----------------------------------------------------------------

# 39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.
# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79
# Interest = amt * ((1+(.01*int)) ** years)
# def fv(pa, ir, yr):
#     res = pa * ((1+(.01*ir)) ** yr)
#     res = round(res, 2)
#     return res
# print(fv(10000,3.5,7))

# -----------------------------------------------------------------

# 40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
# import math
# x1 = 3
# y1 = -4
# x2 = 7
# y2 = 5
# def dist(a1, a2, b1, b2):
#     res = ((a1-b1)**2) + ((a2-b2)**2)
#     res = math.sqrt(res)
#     return round(res,2)
# print(dist(x1,y1,x2,y2))

# -----------------------------------------------------------------

# 41. Write a Python program to check whether a file exists.
# from pathlib import Path
# fn = Path("C:/Users/lgoforth/Documents/x.html")
# print(fn.is_file())

# -----------------------------------------------------------------

# 42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
# import platform
# print(platform.architecture())

# -----------------------------------------------------------------

# 43. Write a Python program to get OS name, platform and release information.
# import platform
# import os
# print("OS Name: {}\nPlatform: {}\nRelease Info: {}".format(os.name, platform.system(), platform.release()))

# -----------------------------------------------------------------

# 44. Write a Python program to locate Python site-packages.
# import site
# print(site.getsitepackages())

# -----------------------------------------------------------------

# 45. Write a python program to call an external command in Python.
# import subprocess
# print(subprocess.call('date'))

# -----------------------------------------------------------------

# 46. Write a python program to get the path and name of the file that is currently executing.
# import os
# print(os.path.realpath(__file__))

# -----------------------------------------------------------------

# 47. Write a Python program to find out the number of CPUs using.
# import multiprocessing as mp
# print("CPUs:",mp.cpu_count())

# -----------------------------------------------------------------

# 48. Write a Python program to parse a string to Float or Integer.
# print("Give a number")
# num = input()
# print(int(num), float(num))

# -----------------------------------------------------------------

# 49. Write a Python program to list all files in a directory in Python.
# from os import listdir
# from os.path import isfile, join
# files = [i for i in listdir("C:/Users/lgoforth/Documents") if isfile(join("C:/Users/lgoforth/Documents", i))]
# print(files)

# -----------------------------------------------------------------

# 50. Write a Python program to print without newline or space.
# for i in range(0, 10):
#     print('*', end="")
# print("\n")

# -----------------------------------------------------------------

# 51. Write a Python program to determine profiling of Python programs. 
# Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module. 
# import cProfile
# def doStuff(n):
#     sqrd = n * n
#     xtwo = n * 2
#     minus1 = n - 1
#     plus1 = n + 1
#     print("Squared", sqrd)
#     print("Times 2", xtwo)
#     print("Minus 1", minus1)
#     print("Plus 1", plus1)
# cProfile.run('doStuff(4)') 

# -----------------------------------------------------------------

# 52. Write a Python program to print to stderr. 
# from __future__ import print_function
# import sys
# def errorPrint(*args, **kwargs):
#     print(*args, file=sys.stderr, **kwargs)
# errorPrint("Here's", "Some", "Arguments", sep="*****")

# -----------------------------------------------------------------

# 53. Write a python program to access environment variables. 
# import os
# print(os.environ)

# -----------------------------------------------------------------

# 54. Write a Python program to get the current username
# import getpass
# print(getpass.getuser())

# -----------------------------------------------------------------

# 55. Write a Python to find local IP addresses using Python's stdlib
# import socket
# print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
# if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
# s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
# socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

# -----------------------------------------------------------------

# 56. Write a Python program to get height and width of the console window.
# ***I DO NOT UNDERSTAND THIS ONE***solution from https://gist.github.com/jtriley/1108174
# def windowDim(): #windows only as far as I know
#     from ctypes import windll, create_string_buffer
#     import struct
#     h = windll.kernel32.GetStdHandle(-12)
#     csbi = create_string_buffer(22)
#     res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
#     if res:
#         (bufx, bufy, curx, cury, wattr, left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
#         sizex = right - left + 1
#         sizey = bottom - top + 1
#         return sizex, sizey
            
# print("Columns and Rows:", windowDim())

# -----------------------------------------------------------------

# 57. Write a program to get execution time for a Python method.
# import time
# ****This returns calculation time as 0.0. I do not believe that.****
# def sum_of_n_numbers(n):
#     start_time = time.time()
#     s = 0
#     for i in range(1,n+1):
#         s = s + i
#     end_time = time.time()
#     return s,end_time-start_time

# n = 5
# print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))

# -----------------------------------------------------------------

# 58. Write a python program to sum of the first n positive integers.
# print("Give me a number.")
# x=int(input())
# def sumOfn(n):
#     return (n*(n+1))/2
# print(sumOfn(x))

# -----------------------------------------------------------------

# 59. Write a Python program to convert height (in feet and inches) to centimeters.
# print("Input your height: ")
# ft = int(input("Feet: "))
# inch = int(input("Inches: "))
# def Convertcm(f,i):
#     i += ft * 12
#     cm = round(i * 2.54, 1)
#     return cm
# print("You're height in centimeters is:", Convertcm(ft, inch))

# -----------------------------------------------------------------

# 60. Write a Python program to calculate the hypotenuse of a right angled triangle.
# a^2 + b^2 = c^2
# import math
# print("Lets use Pythagorean's theorum to find the hypotenuse of a right triangle. Please provide the dimensions")
# a=int(input("Leg 1:"))
# b=int(input("Leg 2:"))
# def hypotenuse(x,y):
#     h = math.sqrt((x ** 2) + (y ** 2))
#     return h
# print("The hypotenuse is:", hypotenuse(a,b))    

# -----------------------------------------------------------------

# 61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.
# print("Lets convert distances. Please provide a distance.")
# dist = int(input("Feet:"))
# def inIn(n):
#     return n * 12
# def inYds(n):
#     return round((n / 3), 2)
# def inMiles(n):
#     return round((n / 5280), 2)
# print("""
# Inches: {}
# Yards: {}
# Miles: {}""".format(inIn(dist), inYds(dist), inMiles(dist)))

# -----------------------------------------------------------------

# 62. Write a Python program to convert all units of time into seconds.
# days = int(input("Days: ")) * 3600 * 24
# hours = int(input("Hours: ")) * 3600
# minutes = int(input("Minutes: ")) * 60
# seconds = int(input("Seconds: "))

# def inSeconds(d,h,m,s):
#     return d+h+m+s
# print("Total time in seconds:", inSeconds(days, hours, minutes, seconds))

# -----------------------------------------------------------------

# 63. Write a Python program to get an absolute file path.
#solution to get abspath of current directory
# import os
# path = input("Provide a file path: ")
# absPath = os.path.abspath(__file__)
# print("The absolute path is: ", absPath)
#solution to get abspath of given directory/file
# def absPath(path):
#     import os
#     return os.path.abspath(path)
# print("Absolute file path: ", absPath("../W3_beginner_exercises"))

# -----------------------------------------------------------------

# 64. Write a Python program to get file creation and modification date/times.
# import os, datetime
# path = input("Provide a file name: ")
# path = os.path.abspath(path)
# c_on = datetime.datetime.fromtimestamp(os.path.getctime(path)).strftime('%m/%d/%Y %H:%M:%S')
# m_on = datetime.datetime.fromtimestamp(os.path.getmtime(path)).strftime('%m/%d/%Y %H:%M:%S')
# print("File was created on: ", c_on)
# print("File was modified on: ", m_on)

# -----------------------------------------------------------------

# 65. Write a Python program to convert seconds to day, hour, minutes and seconds.
# sec = int(input("Give me a ridiculous number of seconds: "))
# def breakItDown(n):
#     totalsec = n
#     day = n // (24 * 3600)
#     n = n % (24 * 3600)
#     hour = n // 3600
#     n %= 3600
#     minutes = n // 60
#     n %= 60
#     seconds = n
#     print("{} converted is {} days {} hours {} minutes and {} seconds".format(totalsec, day, hour, minutes, seconds))
# breakItDown(sec)

# -----------------------------------------------------------------

# 66. Write a Python program to calculate body mass index.
# weight=int(input("What is your weight(lbs)? "))
# ht = int(input("How tall are you? Feet: "))
# htin = int(input("Inches: "))
# def bmi(w,f,i):
#     i += f * 12
#     bmi = round(w/(i * i) * 703, 1)
#     return bmi
# print("BMI: ", bmi(weight, ht, htin))

# -----------------------------------------------------------------

# 67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.
# kp = int(input("Provide a number of kilopascals: "))
# def convert(n):
#     kPa = n
#     psi = round(n / 6.96476, 2)
#     mmHg = round(n / 0.13332238741499935, 2)
#     atmo = round(n / 101.325, 2)
#     print("""{} kPa converts to
# {} psi,
# {} mmHg,
# {} atm""".format(kPa, psi, mmHg, atmo))
# convert(kp)

# -----------------------------------------------------------------

# 68. Write a Python program to calculate the sum of the digits in an integer.
# num = input("Please provide a number, a big one. ")
# def sumNum(n):
#     res = 0
#     for i in n:
#         i = int(i)
#         res += i
#     return res
# print("The sum of the components is: ", sumNum(num))

# -----------------------------------------------------------------

# 69. Write a Python program to sort three integers without using conditional statements and loops.

# a = int(input("Please provide some numbers to sort. "))
# b = int(input("Please provide another number. "))
# c = int(input("Please provide one more number. "))

# low = min(a,b,c)
# hi = max(a,b,c)
# mid = (a + b + c) - low - hi
# print("""The largest number is: {}
# The smallest number is: {}
# The middle number is {}""".format(hi, low, mid))

# -----------------------------------------------------------------

# 70. Write a Python program to sort files by date.
# import os
# import glob

# files = glob.glob("../../../Documents/*.xlsx")
# files.sort(key=os.path.getmtime)
# print("\n".join(files))

# -----------------------------------------------------------------

# 71. Write a Python program to get a directory listing, sorted by creation date.
# import os
# print("\n".join(os.listdir("../../../Documents")))
# -----------------------------------------------------------------

# 72. Write a Python program to get the details of math module.
# import math
# print("\n". join(dir(math)))

# -----------------------------------------------------------------

# 73. Write a Python program to calculate midpoints of a line.
# x1 = 3
# y1 = -4
# x2 = 7
# y2 = 5
# def midpoint(a1, a2, b1, b2):
#     x = ((a1 + b1)/2)
#     y = ((a2 + b2)/2)
#     return "({}, {})".format(x, y)
# print("The midpoint between (3, -4) and (7, 5) is: ", midpoint(x1, y1, x2, y2))

# -----------------------------------------------------------------

# 74. Write a Python program to hash a word.
# import hashlib
# x = input("Lets encrypt some words. Give me something to work with: ")
# out =  hashlib.sha256(x.encode())
# out = out.hexdigest()
# print("the hashed version of your input is: ", out)

# -----------------------------------------------------------------

# 75. Write a Python program to get the copyright information.
# import sys
# print("Copyright Info: ", sys.copyright)

# -----------------------------------------------------------------

# 76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
#****My solution after googling****
# import argparse
# print("Command line arguments: ", argparse.__all__)
#****W3's solution****
# import sys
# print("Name of the script: ", sys.argv[0])
# print("Number of arguments: ", len(sys.argv))
# print("List of arguments: ", str(sys.argv))
# IN CONSOLE TYPE 'python main.py arg1 arg2 arg3'

# -----------------------------------------------------------------

# 77. Write a Python program to test whether the system is a big-endian platform or little-endian platform.
# import sys
# print("Its either 'big' or 'little': ", sys.byteorder)

# -----------------------------------------------------------------

# 78. Write a Python program to find the available built-in modules.
# import sys
# print("All available modules:\n", "\n".join(sys.builtin_module_names))

# -----------------------------------------------------------------

# 79. Write a Python program to get the size of an object in bytes.
# import sys
# x = input("Let's find the how many bytes are in your input. Type anything: ")
# print(str(sys.getsizeof(x)), "bytes")

# -----------------------------------------------------------------

# 80. Write a Python program to get the current value of the recursion limit. 
# import sys
# print("Current recursion limit: ", sys.getrecursionlimit())

# -----------------------------------------------------------------

# 81. Write a Python program to concatenate N strings.
# a = input("Type something, we'll do some stuff with it. ")
# b = input("Type something else. ")
# c = input("One more time. ")
# x = []
# x.append(a)
# x.append(b)
# x.append(c)
# sep = "---"
# print(sep.join(x))
# -----------------------------------------------------------------

# 82. Write a Python program to calculate the sum over a container.
# nums = [13, 17, 89, 11, 20]
# res = 0
# for i in nums:
#     res += i
# print("150 is expected outcome: ", res)
# -----------------------------------------------------------------

# 83. Write a Python program to test whether all numbers of a list is greater than a certain number.
# nums = [13, 17, 89, 11, 20]
# x = int(input("Give me a number. "))
# def gThan(n):
#     glist = []
#     for i in nums:
#         if i > x:
#             glist.append(i)
#     if len(glist) < 1:
#         return "There are no numbers in the list bigger than the number you provided"
#     return glist
# print("Here are the numbers greater than {}: {}".format(x, gThan(x)))

# -----------------------------------------------------------------

# 84. Write a Python program to count the number occurrence of a specific character in a string.
# sent = "Sphinx of black quartz, judge my vow"
# letter = input("Give me a letter: ")
# c = 0
# for i in sent.lower():
#     if i == letter:
#         c += 1
# print("Your letter occurs in '{}' {} time(s)".format(sent, c))

# -----------------------------------------------------------------

# 85. Write a Python program to check if a file path is a file or a directory.
# import os 
# file = "../../PythonPractice"
# if os.path.isfile(file):
#     print("The filename is a file")
# elif os.path.isdir(file):
#     print("The filename is a directory")
# else:
#     print("The filename is neither a file nor a directory")

# -----------------------------------------------------------------

# 86. Write a Python program to get the ASCII value of a character.
# a = input("Type a letter to get the ASCII value. ")
# print(ord(a))

# -----------------------------------------------------------------

# 87. Write a Python program to get the size of a file.
# import os
# file = "./main.py"
# print("Python practice's file size is: ", os.path.getsize(file), "Bytes")

# -----------------------------------------------------------------

# 88. Given variables x=30 and y=20, write a Python program to print t "30+20=50".
# x = 30
# y = 20
# a = 50
# print("{} + {} = {}".format(x,y,a))

# -----------------------------------------------------------------

# 89. Write a Python program to perform an action if a condition is true.
# Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.
# x = 1543
# if x % 2 == 0:
#     print("My variable is an even number")
# else:
#     print("My variable is an odd number")

# -----------------------------------------------------------------

# 90. Write a Python program to create a copy of its own source code.
#****This is another one I don't quite understand, too meta****
# print((lambda str='print(lambda str=%r: (str %% str))()': (str % str))())

# -----------------------------------------------------------------

# 91. Write a Python program to swap two variables.
# x = 'dog'
# y = 'cat'
# print("Before: x = {} y = {}".format(x, y))
# x, y = y, x
# print("After: x = {} y = {}".format(x, y))

# -----------------------------------------------------------------

# 92. Write a Python program to define a string containing special characters in various forms.
#****Solution from W3**** Expected Output \#{'}${"}@/
# print("\#{'}${"'"'"}@/") #wrap double quotes in single quotes
# print(r"""\#{'}${"}@/""") #r followed by triple quotes to maintain format
# print('\#{\'}${"}@/') #wrap in single quotes and escape the single quote with a \
# print('\#{'"'"'}${"}@/') #wrap in single quotes and use double quotes around the single quote
# print(r'''\#{'}${"}@/''') #r followed by triple single quotes to maintain format

# -----------------------------------------------------------------

# 93. Write a Python program to get the identity of an object.
# a = 63
# b = "dog"
# c = {}
# d = {}
# print("a is: {}\nb is: {}\nc is: {}\nd is: {}".format(id(a), id(b), id(c), id(d)))
# -----------------------------------------------------------------

# 94. Write a Python program to convert a byte string to a list of integers. 


# -----------------------------------------------------------------

# 95. Write a Python program to check if a string is numeric.


# -----------------------------------------------------------------

# 96. Write a Python program to print the current call stack.


# -----------------------------------------------------------------

# 97. Write a Python program to list the special variables used within the language.


# -----------------------------------------------------------------

# 98. Write a Python program to get the system time.


# -----------------------------------------------------------------

# 99. Write a Python program to clear the screen or terminal.


# -----------------------------------------------------------------

# 100. Write a Python program to get the name of the host on which the routine is running.


# -----------------------------------------------------------------

# 101. Write a Python program to access and print a URL's content to the console.


# -----------------------------------------------------------------

# 102. Write a Python program to get system command output.


# -----------------------------------------------------------------

# 103. Write a Python program to extract the filename from a given path. 


# -----------------------------------------------------------------

# 104. Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process.


# -----------------------------------------------------------------

# 105. Write a Python program to get the users environment.


# -----------------------------------------------------------------

# 106. Write a Python program to divide a path on the extension separator. 


# -----------------------------------------------------------------

# 107. Write a Python program to retrieve file properties.


# -----------------------------------------------------------------

# 108. Write a Python program to find path refers to a file or directory when you encounter a path name.


# -----------------------------------------------------------------

# 109. Write a Python program to check if a number is positive, negative or zero.


# -----------------------------------------------------------------

# 110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.


# -----------------------------------------------------------------

# 111. Write a Python program to make file lists from current directory using a wildcard.


# -----------------------------------------------------------------

# 112. Write a Python program to remove the first item from a specified list. 


# -----------------------------------------------------------------

# 113. Write a Python program to input a number, if it is not a number generate an error message.


# -----------------------------------------------------------------

# 114. Write a Python program to filter the positive numbers from a list.


# -----------------------------------------------------------------

# 115. Write a Python program to compute the product of a list of integers (without using for loop).


# -----------------------------------------------------------------

# 116. Write a Python program to print Unicode characters.


# -----------------------------------------------------------------

# 117. Write a Python program to prove that two string variables of same value point same memory location.


# -----------------------------------------------------------------

# 18. Write a Python program to create a bytearray from a list.


# -----------------------------------------------------------------




























