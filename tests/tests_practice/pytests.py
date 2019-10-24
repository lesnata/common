
import builtins
import pytest

from homework import task10_reversed_string, task11_time_converter, task12_largest_word, task13_backwards_string, \
    task14_fibonacci_sequence, task15_even_list, task16_sum_all_numbers, task17_factorial, task18_alphabet_modification,\
    task19_alphabetical_string, task20_numbers_comparison


class TestsHomework:
    def test_task10_reversed_string(self):
        string = 'I am a good developer. I am also a writer'
        actual_result = task10_reversed_string(string)
        expected_result = string[::-1]
        assert actual_result == expected_result

    @pytest.mark.parametrize('num, result', [(120, '2:0'), (187, '3:7'), (675, '11:15')])
    def test_task11_time_converter(self, num, result):
        assert task11_time_converter(num) == result

    @pytest.mark.parametrize('string, expected_output', [('fun&!! time', 'time'),
                                                         ('I love dogs', 'love'),
                                                         ('I am a #verygood developer', 'developer')])
    def test_task12_largest_word(self, string, expected_output):
        assert task12_largest_word(string) == expected_output

    def test_task13_backwards_string(self):
        with mock.patch.object(builtins, 'input', lambda _: 'My name is Michele'):
            assert task13_backwards_string() == 'Michele is name My'

    def test_task14_fibonacci_sequence(self):
        with mock.patch.object(builtins, 'input', lambda _: 7):
            assert task14_fibonacci_sequence() == '1, 1, 2, 3, 5, 8, 13'

    @pytest.mark.parametrize('lst, expected_output', [([1, 2, 3, 4, 21, 34, 55, 89], [2, 4, 34]),
                                                      ([0, 2, -3, -4, -6, 7, -10], [0, 2, -4, -6, -10]),
                                                      ([2, 5, 3, 4, 3], [2, 4])])
    def test_task15_even_list(self, lst, expected_output):
        assert task15_even_list(lst) == expected_output

    def test_task16_sum_all_numbers(self):
        with mock.patch.object(builtins, 'input', lambda _: 4):
            assert task16_sum_all_numbers() == 10

    @pytest.mark.parametrize('num, result', [(4, 24), (10, 3628800), (24, 620448401733239439360000)])
    def test_task17_factorial(self, num, result):
        assert task17_factorial(num) == result

    @pytest.mark.parametrize('string, expected_output', [('abcd', 'bcdE'),
                                                         ('klmnsaprst', 'lmnOtbqstU'),
                                                         ('dmtr', 'EnUs')])
    def test_task18_alphabet_modification(self, string, expected_output):
        assert task18_alphabet_modification(string) == expected_output

    @pytest.mark.parametrize('string, expected_output', [('edcba', 'abcde'),
                                                         ('!?klmnsaprst%%', 'aklmnprsst'),
                                                         ('wwwdmtr_', 'dmrtwww')])
    def test_task19_alphabetical_string(self, string, expected_output):
        assert task19_alphabetical_string(string) == expected_output

    @pytest.mark.parametrize('num1, num2', [(13, 13), (-98, -98), (0, 0)])
    def task20_numbers_comparison(self, num1, num2):
        assert task20_numbers_comparison(num1, num2) == '-1'
