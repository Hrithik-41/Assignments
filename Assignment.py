#Assignment 1
#Task 1
# first_number = int(input("Enter first number : "))
# second_number = int(input("Enter second number : "))
#
# addition = first_number + second_number
# subtraction = first_number - second_number
# multiplication = first_number * second_number
# division = first_number / second_number
#
# print("Addition : ", addition)
# print("Subtraction : ", subtraction)
# print("Multiplication : ", multiplication)
# print("Division : ", division)

#Task 2
# first_name = input("Enter first name : ")
# last_name = input("Enter last name : ")
# full_name = first_name + " " + last_name
# print("Hello,",full_name+"!", "Welcome to the Python program.")



#Assignment 2
#Task 1
# num = int(input("Enter Your Number : "))
# if (num % 2 ==0):
#     print(num, "is an Even Number")
# else:
#     print(num, "is an Odd Number")

#Task 2
# num = 50
# sum = 0
# for i in range(num+1):
#     sum += i
# print(sum)



#Assignment 3
#Task 1
# num = int(input("Enter a number : "))
# def factorial(num):
#     if num < 2:
#         return 1
#     else:
#         return num * factorial(num - 1)
# print("Factorial of", num, "is", factorial(num))

#Task 2
# import math
# num = float(input("Enter Your Number : "))
# print("Square Root :", math.sqrt(num))
# print("Logarithm :", math.log(num))
# print("Sine :", math.sin(num))



#Assignment 4
'''Task 1
try :
    file = open("sample.txt", "r")
    read_file = file.read()
    print(read_file)
except FileNotFoundError:
    print("The file 'sample.txt' was not found")'''

#Task 2
'''text = input('Enter text to write to the file : ')
file = open('test', 'w')
print("Data successfully written to output.txt")
file.write(text)
file.close()

text = input('Enter additional text to append : ')
file= open('test', 'a')
write_file2 = file.write(text)
print("Data successfully appended")
file.close()

file = open('test', 'r')
text = file.read()
print("Final content of output.txt")
print(text)
file.close()'''
