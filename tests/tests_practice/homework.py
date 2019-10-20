from math import log, sqrt
import re


def task1(a, b):
    return list(set(a) & set(b))


def task2(given_string, letter):
    return given_string.count(letter)


def task3(integer):
    '''
    task3: Write a Python program to check if a given positive integer is a power of three
    Input : 9
    Output : True
    '''
    return log(integer, 3).is_integer()


def task4(some_number):
    while some_number >= 10:
        some_number = sum(list(map(int, str(some_number))))
    return some_number


def task5(some_list):
    """Write a Python program to push all zeros to the end of a list.
    Input : [0,2,3,4,6,7,10]
    Output : [2, 3, 4, 6, 7, 10, 0]"""
    zero_count = some_list.count(0)
    some_list.remove(0)
    some_list.append(zero_count * 0)
    return some_list


def task6(some_list):
    """Write a Python program to check a sequence of numbers is an arithmetic progression or not.
    Input : [5, 7, 9, 11]
    Output : True"""
    r1 = some_list[0]
    r2 = some_list[len(some_list) - 1]
    difference = some_list[1] - some_list[0]
    return some_list == [item for item in range(r1, r2 + 1, difference)]


def task7(some_list):
    duplicated_list = [x for x in some_list if some_list.count(x) == 1]
    return ''.join(str(e) for e in duplicated_list)


def task8(some_list):
    result = [x for x in range(min(some_list), max(some_list) + 1) if x not in some_list]
    return ''.join(str(e) for e in result)


def task9(some_list):
    for counter, elem in enumerate(some_list):
        if isinstance(elem, tuple):
            break
    return counter


def task10(some_string):
    return some_string[::-1]


def task11(some_number):
    return str(some_number // 60) + ':' + str(some_number % 60)


def task12(some_string):
    return max(re.sub("[^a-zA-Z]+", " ", some_string).split(" "), key=len)


def task13():
    """Write a program (using functions!) that asks the user for a long string containing multiple words.
    Print back to the user the same string, except with the words in backwards order."""
    some_input = input("Type your sentence:").split(" ")
    return ' '.join(reversed(some_input))


user_input = input("How many Fibonacci numbers to generate? ")
try:
    tested_user_input = int(user_input)
except ValueError:
    print("Please type integer")


def task14(tested_user_input):
    """Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
     Take this opportunity to think about how you can use functions.
     Make sure to ask the user to enter the number of numbers in the sequence to generate.
     (Hint: The Fibonnaci sequence is a sequence of numbers where the next number
     in the sequence is the sum of the previous two numbers in the sequence.
    The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)"""
    fibonacci_numbers = [1, 1]
    for i in range(2, tested_user_input):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    return fibonacci_numbers


def task15(a):
    return [x for x in a if x % 2 == 0]


def task16():
    user_input = input("Enter your number:")
    some_sum = 0
    for i in range(user_input + 1):
        some_sum += i
    return some_sum


def task17():
    some_input = input("Enter your number:")
    fact = 1
    for i in range(1, some_input + 1):
        fact = fact * i
    return fact


def task18(some_string):
    """Write a program that will take the str parameter being passed and
    modify it using the following algorithm.
    Replace every letter in the string with the letter following it in the alphabet
    (ie. cbecomes d, zbecomes a).
    Then capitalize every vowel in this new string (a, e, i, o, u)
    and finally return this modified string.
    Input: abcd
    Output: bcdE
    cdE
    """

    my_list = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiou'

    for i in some_string:
        if i == 'z':
            my_list.append('A')
        else:
            try:
                updated_index = alphabet.index(i) + 1
                updated_value = alphabet[updated_index]
                if updated_value in vowels:
                    my_list.append(updated_value.upper())
                else:
                    my_list.append(updated_value)
            except ValueError:
                continue
    return "".join(my_list)


def task19(some_string):
    return ''.join(sorted(some_string.lower()))


def task20(num1, num2):
    """Write a program that will take both parameters being passed
    and return the true if num2 is greater than num1, otherwise return the false.
    If the parameter values are equal to each other then return the string -1"""
    return '-1' if num1 == num2 else num2 > num1






