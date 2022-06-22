import calendar

def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(string):
    return len(string)

def join_string(str1, str2):
    return str1 + str2

def add_string_as_number(string1, string2):
    return int(string1) + int(string2)

def number_to_full_month_name(num):
    return calendar.month_name[num]

def number_to_short_month_name(num):
    return calendar.month_abbr[num]

def volume(num):
    return num*num*num

def reversed(string):
    return string[::-1]

def ftoc(num):
    return (num - 32) * 5/9