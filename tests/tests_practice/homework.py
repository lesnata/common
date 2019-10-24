from math import log, sqrt
import re


def task1_common_list(a, b):
    """
    Take two lists, say for example these two:
    a =[1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b =[1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only
    the elements that are common between the lists (without duplicates).
    """
    return list(set(a) & set(b))


def task2_count_a(given_string, letter):
    """
    Return the number of times that the letter “a” appears anywhere in the given string
    Given string is “I am a good developer. I am also a writer” and output should be 5.
    """
    return given_string.count(letter)


def task3_power_of_three(integer):
    """
    task3: Write a Python program to check if a given positive integer is a power of three
    Input : 9
    Output : True
    """
    return log(integer, 3).is_integer()


def task4_add_digits(some_number):
    """
    Write a Python program to add the digits of
    a positive integer repeatedly until the result has a single digit.
    Input : 48
    Output : 3
    For example given number is 59, the result will be 5.
    Step 1: 5 + 9 = 14
    Step 1: 1 + 4 = 5
    """
    while some_number >= 10:
        some_number = sum(list(map(int, str(some_number))))
    return some_number


def task5_zeros_list(some_list):
    """Write a Python program to push all zeros to the end of a list.
    Input : [0,2,3,4,6,7,10]
    Output : [2, 3, 4, 6, 7, 10, 0]"""
    zero_count = some_list.count(0)
    some_list.remove(0)
    some_list.append(zero_count * 0)
    return some_list


def task6_arithmetic_progression(some_list):
    """Write a Python program to check a sequence of numbers is an arithmetic progression or not.
    Input : [5, 7, 9, 11]
    Output : True"""
    r1 = some_list[0]
    r2 = some_list[len(some_list) - 1]
    difference = some_list[1] - some_list[0]
    return some_list == [item for item in range(r1, r2 + 1, difference)]


def task7_non_duplicating_number(some_list):
    """
    Write a Python program to find the number in a list that doesn't occur twice.
    Input : [5, 3, 4, 3, 4]
    Output : 5
    """
    duplicated_list = [x for x in some_list if some_list.count(x) == 1]
    return ''.join(str(e) for e in duplicated_list)


def task8_missing_number(some_list):
    """
    Write a Python program to find a missing number from a list.
    Input : [1,2,3,4,6,7,8]
    Output : 5
    """
    result = [x for x in range(min(some_list), max(some_list) + 1) if x not in some_list]
    return ''.join(str(e) for e in result)


def task9_count_till_tuple(some_list):
    """
    Write a Python program to count the elements in a list until an element is a tuple.
    Sample Test Cases:
    Input: [1,2,3,(1,2),3]
    Output: 3
    """
    for counter, elem in enumerate(some_list):
        if isinstance(elem, tuple):
            break
    return counter


def task10_reversed_string(some_string):
    """
    Write a program that will take the str parameter being passed and
    return the string in reversed order.
    For example: if the input string is "Hello World and Coders"
    then your program should return the string sredoC dna dlroW olleH.
    """
    return some_string[::-1]


def task11_time_converter(some_number):
    """
    Write a program that will take the num parameter being passed and
    return the number of hours and minutes the parameter converts to
    (ie. if num = 63 then the output should be 1:3).
    Separate the number of hours and minutes with a colon.
    """
    return str(some_number // 60) + ':' + str(some_number % 60)


def task12_largest_word(some_string):
    """
    Write a program that will take the parameter being passed and
    return the largest word in the string.
    If there are two or more words that are the same length,
    return the first word from the string with that length. Ignore punctuation.
    Sample Test Cases:
    Input:"fun&!! time"
    Output:time
    Input:"I love dogs"
    Output:love
    """
    return max(re.sub("[^a-zA-Z]+", " ", some_string).split(" "), key=len)


def task13_backwards_string():
    """Write a program (using functions!) that asks the user for a long string containing multiple words.
    Print back to the user the same string, except with the words in backwards order."""
    some_input = input("Type your sentence:").split(" ")
    return ' '.join(reversed(some_input))


user_input = input("How many Fibonacci numbers to generate? ")
try:
    tested_user_input = int(user_input)
except ValueError:
    print("Please type integer")


def task14_fibonacci_sequence(tested_user_input):
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


def task15_even_list(a):
    """
    Let’s say I give you a list saved in a variable:
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
    Write one line of Python that takes this list a and
    makes a new list that has only the even elements of this list in it.
    """
    return [x for x in a if x % 2 == 0]


def task16_sum_all_numbers():
    """
    Write a program that will add up all the numbers from 1 to input number.
    For example: if the input is 4 then your program should
    return 10 because 1 + 2 + 3 + 4 = 10.
    """
    some_input = input("Enter your number:")
    some_sum = 0
    for i in range(some_input + 1):
        some_sum += i
    return some_sum


def task17_factorial():
    """
    Write a program that will take the parameter being passed and return the factorial of it.
    For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24.
    """
    some_input = input("Enter your number:")
    fact = 1
    for i in range(1, some_input + 1):
        fact = fact * i
    return fact


def task18_alphabet_modification(some_string):
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


def task19_alphabetical_string(some_string):
    """
    Write a program that will take the str string parameter being passed and
    return the string with the letters in alphabetical order (ie. hello becomes ehllo).
    Assume numbers and punctuation symbols will not be included in the string.
    Input: edcba
    Output: abcde
    """
    return ''.join(sorted(some_string.lower()))


def task20_numbers_comparison(num1, num2):
    """Write a program that will take both parameters being passed
    and return the true if num2 is greater than num1, otherwise return the false.
    If the parameter values are equal to each other then return the string -1"""
    return '-1' if num1 == num2 else num2 > num1






