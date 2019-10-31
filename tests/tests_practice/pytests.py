import builtins
import pytest

from homework import task10_reversed_string, task11_time_converter, task12_largest_word, task13_backwards_string, \
    task14_fibonacci_sequence, task15_even_list, task16_sum_all_numbers, task17_factorial, task18_alphabet_modification,\
    task19_alphabetical_string, task20_numbers_comparison


class TestsHomework:
    def test_task10_reversed_string(self):
        string = 'Hello World and Coders'
        actual_result = task10_reversed_string(string)
        expected_result = string[::-1]
        assert actual_result == expected_result

    @pytest.mark.parametrize('num, result', [(63, '1:3'), (120, '2:0'), (58, '0:58')])
    def test_task11_time_converter(self, num, result):
        assert task11_time_converter(num) == result

    @pytest.mark.parametrize('string, expected_output', [('fun&!! time', 'time'), ('I love dogs', 'love')])
    def test_task12_largest_word(self, string, expected_output):
        assert task12_largest_word(string) == expected_output

    @pytest.mark.parametrize('initial_input, result', [('My name is Michele', 'Michele is name My'),
                                                       ('Hey Developer Hello', 'Hello Developer Hey')])
    def test_task13_backwards_string(self, initial_input, result):
        assert task13_backwards_string(initial_input) == result

    @pytest.mark.parametrize('tested_user_input, expected_output', [(7, [1, 1, 2, 3, 5, 8, 13]), (4, [1, 1, 2, 3])])
    def test_task14_fibonacci_sequence(self, tested_user_input, expected_output):
        assert task14_fibonacci_sequence(tested_user_input) == expected_output

    @pytest.mark.parametrize('some_list, expected_output', [([1, 4, 9, 16, 25, 36, 49, 64, 81, 100], [4, 16, 36, 64, 100]),
                                                      ([2, 5, 3, 4, 3], [2, 4])])
    def test_task15_even_list(self, some_list, expected_output):
        assert task15_even_list(some_list) == expected_output

    @pytest.mark.parametrize('some_input, result', [(4, 10), (5, 15)])
    def test_task16_sum_all_numbers(self, some_input, result):
        assert task16_sum_all_numbers(some_input) == result

    @pytest.mark.parametrize('num, result', [(4, 24), (10, 3628800)])
    def test_task17_factorial(self, num, result):
        assert task17_factorial(num) == result

    @pytest.mark.parametrize('string, expected_output', [('abcd', 'bcdE'),
                                                         ('cat', 'dbU'),
                                                         ('mouse', 'npvtf')])
    def test_task18_alphabet_modification(self, string, expected_output):
        assert task18_alphabet_modification(string) == expected_output

    @pytest.mark.parametrize('string, expected_output', [('edcba', 'abcde'),
                                                         ('hello', 'ehllo')])
    def test_task19_alphabetical_string(self, string, expected_output):
        assert task19_alphabetical_string(string) == expected_output

    @pytest.mark.parametrize('num1, num2', [(13, 13), (-1, -1), (0, 0)])
    def task20_numbers_comparison(self, num1, num2):
        assert task20_numbers_comparison(num1, num2) == '-1'

