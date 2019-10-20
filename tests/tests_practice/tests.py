import unittest
from unittest.mock import patch
from homework import task1, task2, task3, task4, task5, task6, task7, task8, task9, task10, \
    task11, task12, task13, task14, task15, task16, task17, task18, task19, task20


class TestCases(unittest.TestCase):

    def setUp(self):
        self.task1_list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        self.task1_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.task2_string = "I am a good developer. I am also a writer"
        self.task2_letter = "a"
        self.task3_integer = 9
        self.task5_list = [0, 2, 3, 4, 6, 7, 10]
        self.task6_list = [5, 7, 9, 11]
        self.task7_list = [5, 3, 4, 3, 4]
        self.task8_list = [1, 2, 3, 4, 6, 7, 8]
        self.task9_list = [1, 2, 3, (1, 2), 3]
        self.task10_string = "Hello World and Coders"
        self.task12_string1 = "fun&!! time"
        self.task12_string2 = "I love dogs"
        self.task13_string = "My name is Michele"
        self.task14_number = 4
        self.task15_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.task18_string = "abcd"
        self.task19_string = "edcba"

    def test_task1(self):
        real_result = task1(self.task1_list1, self.task1_list2)
        expected_result = [1, 2, 3, 5, 8, 13]
        self.assertListEqual(real_result, expected_result)

    def test_task2(self):
        real_result = task2(self.task2_string, self.task2_letter)
        expected_result = 5
        self.assertEqual(real_result, expected_result)

    def test_task3(self):
        real_result = task3(self.task3_integer)
        self.assertTrue(real_result)

    def test_task4(self):
        real_result = task4(59)
        expected_result = 5
        self.assertEqual(real_result, expected_result)

    def test_task5(self):
        real_result = task5(self.task5_list)
        expected_result = [2, 3, 4, 6, 7, 10, 0]
        self.assertListEqual(real_result, expected_result)

    def test_task6(self):
        real_result = task6(self.task6_list)
        self.assertTrue(real_result)

    def test_task7(self):
        real_result = task7(self.task7_list)
        expected_result = '5'
        self.assertEqual(real_result, expected_result)

    def test_task8(self):
        real_result = task8(self.task8_list)
        expected_result = '5'
        self.assertEqual(real_result, expected_result)

    def test_task9(self):
        real_result = task9(self.task9_list)
        expected_result = 3
        self.assertEqual(real_result, expected_result)

    def test_task10(self):
        real_result = task10(self.task10_string)
        expected_result = "sredoC dna dlroW olleH"
        self.assertEqual(real_result, expected_result)

    def test_task11(self):
        real_result = task11(63)
        self.assertEqual(real_result, "1:3")

    def test_task12(self):
        self.assertEqual(task12(self.task12_string1), "time")
        self.assertEqual(task12(self.task12_string2), "love")

    @patch('builtins.input', return_value='My name is Michele')
    def test_task13(self, mock):
        expected_result = "Michele is name My"
        self.assertEqual(task13(), expected_result)

    # @patch('builtins.input', return_value=4)
    # def test_task14(self, mock):
    #     expected_result = [1, 1, 2, 3]
    #     self.assertEqual(task14(), expected_result)

    def test_task14(self):
        real_result = task14(self.task14_number)
        expected_result = [1, 1, 2, 3]
        self.assertListEqual(real_result, expected_result)

    def test_task15(self):
        real_result = task15(self.task15_list)
        expected_result = [4, 16, 36, 64, 100]
        self.assertListEqual(real_result, expected_result)

    @patch('builtins.input', return_value=4)
    def test_task16(self, mock):
        expected_result = 10
        self.assertEqual(task16(), expected_result)

    @patch('builtins.input', return_value=4)
    def test_task17(self, mock):
        expected_result = 24
        self.assertEqual(task17(), expected_result)

    def test_task18(self):
        real_result = task18(self.task18_string)
        expected_result = "bcdE"
        self.assertEqual(real_result, expected_result)

    def test_task19(self):
        real_result = task19(self.task19_string)
        expected_result = "abcde"
        self.assertEqual(real_result, expected_result)

    def test_task20(self):
        real_result = task20(4, 4)
        expected_result = '-1'
        self.assertEqual(real_result, expected_result)


if __name__ == '__main__':
    unittest.main()
