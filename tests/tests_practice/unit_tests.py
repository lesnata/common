import unittest
from unittest.mock import patch
from homework import task1_common_list, task2_count_a, task3_power_of_three, task4_add_digits, task5_zeros_list, \
    task6_arithmetic_progression, task7_non_duplicating_number, task8_missing_number, task9_count_till_tuple, \
    task10_reversed_string, task11_time_converter, task12_largest_word, task13_backwards_string, \
    task14_fibonacci_sequence, task15_even_list, task16_sum_all_numbers, task17_factorial, task18_alphabet_modification,\
    task19_alphabetical_string, task20_numbers_comparison


class TestCases(unittest.TestCase):

    def setUp(self):
        self.task1_common_list_list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        self.task1_common_list_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.task2_count_a_string = "I am a good developer. I am also a writer"
        self.task2_count_a_string_letter = "a"
        self.task3_power_of_three_integer = 9
        self.task5_zeros_list_list = [0, 2, 3, 4, 6, 7, 10]
        self.task6_arithmetic_progression_list = [5, 7, 9, 11]
        self.task7_non_duplicating_number_list = [5, 3, 4, 3, 4]
        self.task8_missing_number_list = [1, 2, 3, 4, 6, 7, 8]
        self.task9_count_till_tuple_list = [1, 2, 3, (1, 2), 3]
        self.task10_reversed_string_string = "Hello World and Coders"
        self.task12_largest_word_string1 = "fun&!! time"
        self.task12_largest_word_string2 = "I love dogs"
        self.task13_backwards_string_string = "My name is Michele"
        self.task14_fibonacci_sequence_number = 4
        self.task15_even_list_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.task18_alphabet_modification_string = "abcd"
        self.task19_alphabetical_string_string = "edcba"

    def test_task1_common_list(self):
        real_result = task1_common_list(self.task1_common_list_list1, self.task1_common_list_list2)
        expected_result = [1, 2, 3, 5, 8, 13]
        self.assertListEqual(real_result, expected_result)

    def test_task2_count_a(self):
        real_result = task2_count_a(self.task2_count_a_string, self.task2_count_a_string_letter)
        expected_result = 5
        self.assertEqual(real_result, expected_result)

    def test_task3_power_of_three(self):
        real_result = task3_power_of_three(self.task3_power_of_three_integer)
        self.assertTrue(real_result)

    def test_task4_add_digits(self):
        real_result = task4_add_digits(59)
        expected_result = 5
        self.assertEqual(real_result, expected_result)

    def test_task5_zeros_list(self):
        real_result = task5_zeros_list(self.task5_zeros_list_list)
        expected_result = [2, 3, 4, 6, 7, 10, 0]
        self.assertListEqual(real_result, expected_result)

    def test_task6_arithmetic_progression(self):
        real_result = task6_arithmetic_progression(self.task6_arithmetic_progression_list)
        self.assertTrue(real_result)

    def test_task7_non_duplicating_number(self):
        real_result = task7_non_duplicating_number(self.task7_non_duplicating_number_list)
        expected_result = '5'
        self.assertEqual(real_result, expected_result)

    def test_task8_missing_number(self):
        real_result = task8_missing_number(self.task8_missing_number_list)
        expected_result = '5'
        self.assertEqual(real_result, expected_result)

    def test_task9_count_till_tuple(self):
        real_result = task9_count_till_tuple(self.task9_count_till_tuple_list)
        expected_result = 3
        self.assertEqual(real_result, expected_result)

    def test_task10_reversed_string(self):
        real_result = task10_reversed_string(self.task10_reversed_string_string)
        expected_result = "sredoC dna dlroW olleH"
        self.assertEqual(real_result, expected_result)

    def test_task11_time_converter(self):
        real_result = task11_time_converter(63)
        self.assertEqual(real_result, "1:3")

    def test_task12_largest_word(self):
        self.assertEqual(task12_largest_word(self.task12_largest_word_string1), "time")
        self.assertEqual(task12_largest_word(self.task12_largest_word_string2), "love")

    @patch('builtins.input', return_value='My name is Michele')
    def test_task13_backwards_string(self, mock):
        expected_result = "Michele is name My"
        self.assertEqual(task13_backwards_string(), expected_result)

    # @patch('builtins.input', return_value=4)
    # def test_task14(self, mock):
    #     expected_result = [1, 1, 2, 3]
    #     self.assertEqual(task14(), expected_result)

    def test_task14_fibonacci_sequence(self):
        real_result = task14_fibonacci_sequence(self.task14_fibonacci_sequence_number)
        expected_result = [1, 1, 2, 3]
        self.assertListEqual(real_result, expected_result)

    def test_task15_even_list(self):
        real_result = task15_even_list(self.task15_even_list_list)
        expected_result = [4, 16, 36, 64, 100]
        self.assertListEqual(real_result, expected_result)

    @patch('builtins.input', return_value=4)
    def test_task16_sum_all_numbers(self, mock):
        expected_result = 10
        self.assertEqual(task16_sum_all_numbers(), expected_result)

    @patch('builtins.input', return_value=4)
    def test_task17_factorial(self, mock):
        expected_result = 24
        self.assertEqual(task17_factorial(), expected_result)

    def test_task18_alphabet_modification(self):
        real_result = task18_alphabet_modification(self.task18_alphabet_modification_string)
        expected_result = "bcdE"
        self.assertEqual(real_result, expected_result)

    def test_task19_alphabetical_string(self):
        real_result = task19_alphabetical_string(self.task19_alphabetical_string_string)
        expected_result = "abcde"
        self.assertEqual(real_result, expected_result)

    def test_task20_numbers_comparison(self):
        real_result = task20_numbers_comparison(4, 4)
        expected_result = '-1'
        self.assertEqual(real_result, expected_result)


if __name__ == '__main__':
    unittest.main()

