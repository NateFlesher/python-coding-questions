# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name):
    """Create a function that allows a user to input a username to output Hello_(user_name)"""
    user_name = input('Enter Username: ')
    print("hello_" + user_name + "!")
    return


hello_name(user_name='')


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """Create a function that prints out odd numbers but returns nothing"""
    for value in range(1, 100, 2):
        print(value)
    return


first_odds()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    """Pick the biggest number out of a given list"""
    max = a_list[0]
    for x in a_list:
        if x > max:
            max = x
    return max


print(max_num_in_list([1, 2, 3, -10, 5]))


# Question 4
# Write a function to return if the given year is a leap year
def is_leap_year(a_year):
    """Defining a leap year"""
    leap = False
    if (a_year % 400 == 0) and (a_year % 100 == 0):
        leap = True
    elif (a_year % 4 == 0) and (a_year % 100 != 0):
        leap = True
    else:
        pass
    return leap


print(is_leap_year(1998))
print(is_leap_year(2022))
print(is_leap_year(2024))
print(type(is_leap_year(2024)))


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers

def is_consecutive(a_list):
    """Write a function to confirm if numbers in a list are consecutive or not"""
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))


a_list = [2, , 3, 4, 5]

print(is_consecutive(a_list))
print(type(is_consecutive(a_list)))
