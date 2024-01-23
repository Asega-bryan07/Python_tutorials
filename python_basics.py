# Comments - they are ignored by the interpreter ''' Your comment '''/ #

# def class_one():
    
#     #'''this funnction defines class 1'''
#     # ctrl + / -comments out
#     name = 'John'


# data types - float, int, bool, "string"
# string  - alphabet A-Z, z-a
# print('Hello World!') # string

# integer - 0 - 9 -> 10_000_000
# a = 10
# b = 30
# c = -5
# print(f"first Variable is {a}, second Variable is {b}, third Variable is {c}")

# float - any number with a 0.0, 0.1, 100_000.0
# a = 10.2
# b = 30.5
# c = -5.8
# add_float = a +b + c
# print(add_float)
# print(f"first is {a}, second is {b}, third is {c}")

# boolean - True / False 
# is_paid = False # 0 1
# print(is_paid)

# variables
# previous_school = "St. John's Kisumu"
# a = 0.5
# b = 10
# c = False

# comparison operators

# == means equal to, != does not equal to, assignment(+= adds to, -= subtracts to), ++ increment, -- decrement

# input
# name = input("What is your name? ")
# b_year = 2024 - int(input("Enter Your Birth Year: "))
# print(f"Hello {name} You are {b_year} Years Old!")

# x = 40 + (3 * 2) / 2 - 1
# print(x)
# x = 3 == 2 '><!=' 


# arithmetic operators '+ - * / // ** % - modulo '
# x = 3
# y = 10
# def addition():
#     print(x + y)
# def div(): 
#     print(x / y)
# def mul():
#     print(x * y)
# def division():
#     print(x // y)
# def mod():
#     print(x % y)

# addition()
# div()
# mul()
# division()
# mod()


# x = 20 % 3
# print(x)
# object 
# array 
# names = ['John', 'Erick', 'Jane', 'Melvin', 'Jeff', 'Hilda']
# names[1] = 'Bob'
# print(names[0:-2])


# tuple
# names = ('John', 'Erick', 'Jane', 'Melvin', 'Jeff', 'Hilda')

# print(names)

# Lists
# names = ["John", "erick", "jonny", "vic"]
# print(names)

# Dictionary - JSON

# locations = { 'KITUI': {'Latitude': 39.33154, 'Longitude' : 30.00554},
#               'KAMPALA': {'Latitude': 39.33154, 'Longitude' : 30.00554},
#               'NAIROBI': {'Latitude': 39.33154, 'Longitude' : 30.00554},
#               'THIKA': {'Latitude': 39.33154, 'Longitude' : 30.00554},
#               'KISUMU': {'Latitude': 39.33154, 'Longitude' : 30.00554},
#               'MIGORI': {'Latitude': 39.33154, 'Longitude' : 30.00554}}

#                 # 'Deputy' : 'Mrs. Hilda', 'age' : 29,
#                 #  'staff1' : 'Mr. vic', 'age' : 30 ,
#                 #   'staff2' : 'Mr. Ema', 'age' : 30 ,
#                 #    'staff3' : 'Mr. Elvis', 'age' : 30 ,
#                 #     'staff3' : 'Mr. Mike', 'age' : 30 }
# print(locations)

# # sets
# set1 = {"Val", "Emily", "Nancy"}
# set2 = {"Elvis", "Chris", "Mike"}
# # print(set1)
# print("Val" in set1)

# logical operators (and - both cases must be true, or - one meets requirements, not) 
# price = 5000
# if price > 100 and price < 1000:
#     print("Price is between 100 and 1000")
# elif price > 1000:
#     print("Price is over 1000")
# else:
#     print("Price is Below 100")



# if else statements
# temperature = 0
# if temperature > 30:
#     print("A very hot Day!\nDrink plenty of water")

# elif temperature > 20:
#     print("A hot day\nNothing")

# elif temperature > 10:
#     print("A bit cold\nNothing")

# else:
#     print("It's a cold day\t\nnobody")
# name = input("Enter Your Name: ")

# if name == "":
#     print("Please Enter Your Name")
# else:
#     print(f"Hello {name}")
# age = int(input("Enter your age in numbers: "))
# def is_adult():
#     if age > 18:
#         print("You are an Adult")
#     else:
#         print("You are a Child")
# is_adult()

# loops - for, while, do...while
# for num in range(1, 21):
#     print(num, end=", * ")

# for num in range(-10, 20, 4):
#     print(num)

# for i in range(ord('z'), ord('a') -1, -1):
#     if i % 2 == 0:
#         diff = 0 
#     else:
#         diff = 32
#     print('{}'.format(chr(i - diff)), end='')

# for x in range(1, 11):
#     if x == 7: # for continue, 7 is an exception
#         break # for break, 7 is the exception
#     else:
        
#         print(x, end=", ")

# print('\n\tDone with code\nWe\'ve escaped the loop') # we are done \n - new line \t - tab

#  while
# attendance = 23
# while attendance > 1:
#     print('People Turned Up')
#     attendance = attendance - 2
# print("There was no Attendance")
# name = str(input("Enter your name: "))

# while name == "":
#     print("You didn\'t enter a name :(")
#     name = input("Enter your name:) ")
# print(f'Hello! So You are {name}!')



# functions

# def hello(name="Smith"):
#     print(f"hello {name}")
# hello()
# def happy_birthday(name, age): # arguments are passed in the ()
#     print(f"Happy Birth Day {name}!")
#     print(f"You are {age} years old!")
# happy_birthday("John", 20) # a block of reusable code and must have ()


# def display_invoice(username, amount, due_date):
#     print(f"Hello Mr. {username}!")
#     print(f"Your bill of Ksh.{amount} is due {due_date}")

# display_invoice('John', 20_000, 'Saturday 13th January 2024')



# classes - we create the class, and then we write the function in it
# class Person: 
#     def __init__(self, age, name, gender, residence, dob):
#         self.age = age
#         self.name = name
#         self.gender = gender
#         self.residence = residence
#         self.dob = dob
#     def display_info(self):
#         print(f"Hello {self.name}, you are {self.age} years old\n You are {self.gender}\
#                 from {self.residence}, born on {self.dob}")

# person1 = Person(20, "John", "Male", "Kisumu", "12th January 2000")
# person1.display_info()
# # class Student(Person):
# #     def __init__(self, age, name, gender, residence, dob, school):
# #         super().__init__(age, name, gender,       


# inheritance
# Animals - Rabbit(walk, alive, eat), Dog(walk, alive, eat), Hawk(fly, alive, eat)
# class Animal: # parent 
#     alive = True
#     def eat(self):
#         print("This animal can eat")
#     def walk(self):
#         print("This animal can walk")
#     def sleep(self):
#         print("This animal can sleep")

# class Rabbit(Animal): # child
#     pass
# class Tortoise(Animal):
#     pass
# class Dog(Animal):
#     pass

# rabbit = Rabbit()
# dog = Dog()
# tort = Tortoise()

# dog.walk() # grand child
# dog.sleep()
# dog.eat() # ctrl + D

# class Ytdownload:
#     import sys
#     from sys import argv
#     from pytube import YouTube

#     link = sys.argv[1]
#     print(link)
#     yt = YouTube(link)


#     print("Song Title: ", yt.title)
#     print("Song Views: ", yt.views, end=(" "))

#     youtube_downloads = yt.streams.get_highest_resolution()

# nested loops
# modules & imports --> importing from a function to another file
# packages
# pip
# virtualenv
# decorators
# generators
# iterators
# comprehensions



# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

# class Square(Rectangle):
#     def __int__(self, legth, width):
#         super().__init__(legth, width)


#     def area(self):
#         return self.length * self.width

# class Cube(Rectangle):
#     def __int__(self, length, width, heigth):
#         self.length = length
#         self.width = width
#         self.heigth = heigth

# square = Square(3,3)
# cube = Cube(3,6,7)



# class Robot:
#     # init method or a constructor(__init__)
#     def __init__(self, name):
#         self.name = name

#     def say_hi(self):
#         print(f'Hello My Name is {self.name}')

# r = Robot('Robocop')
# r.say_hi()

# return 
# class HP:
#     def __init__(self, name, company, date_started):
#         self.name = name
#         self.company = company
#         self.date_started = date_started

#     def __str__(self):# __str__ is a method used to define how an object is represented (string)
#         return f"I am a French Company; {self.company}, and I started in {self.date_started}. Welcome to {self.name}\n\
#             Enjoy Digital Life!"

# comp = HP("HP", "MineMedia", "Two Years Ago")
# print(comp)

# if __name__ == "__main__":
#     pass


# class Person(object): # OOP
#     '''Constructor'''
#     def __init__(self, name):
#         self.name = name

#     '''To get name'''
#     def getName(self):
#         return  self.name 
    
#     '''To see if the person is an employee'''
#     def isEmployee(self):
#         return False


# '''Lets do the inheritance from the Person class'''
# class Employee(Person):
#     '''lets True instead of False'''
#     def isEmployee(self):
#         return True
    
# emp = Person("John Matemba") # Object
# print(f'I am an employee, my name is {emp.getName()}, and I have a status of {emp.isEmployee()} employment')

# emp = Employee("Mike Iminza") # second obj
# print(f'I am an employee, my name is {emp.getName()}, and I have a status of {emp.isEmployee()} employment')



# nested loops - a loop inside another loop

# rows = int(input("Enter the number of rows you need$: "))
# columns = int(input("Enter the number of columns you need$: "))
# symbol = input("Enter the symbols you need to show the flower rectangle$: ")

# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end=' ')

#     print()
    



# Exceptions - try & except & finally


# try: 
#     j = 5 // 0
#     print(j)
# #     some code
# except ZeroDivisionError:
#     print("Cannot divide by zero") 
    
# finally:
#     result = 1
# print(f'The result is: {result}')

balance = 999.5
while True:
    try:
        num = float(input("Enter Deposit amount: "))
    except ValueError:
        print("Input must have a floating point number")
    finally:

        balance += num
    print(f"Balance: {balance}")

print(f"Balance: {balance}")
