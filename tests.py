import unittest
import random
from functions import func

class TestFunc(unittest.TestCase):
    def test_1(self):
        # Given
        input_value = ""
        expected_result = 0
        # When
        result = func(input_value)
        # Then
        self.assertEqual(expected_result, result)

    def test_2(self):
        # Given
        input_value = "3"
        expected_result = 3
        # When
        result = func(input_value)
        # Then
        self.assertEqual(expected_result, result)
    
    def test_3(self):
        # Given
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        input_value = f"{num1},{num2}"
        expected_result = num1 + num2
        # When
        result = func(input_value)
        # Then
        self.assertEqual(expected_result, result)
    
    def test_4(self):
        # Given
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        input_value = f"{num1}\n{num2}"
        expected_result = num1 + num2
        # When
        result = func(input_value)
        # Then
        self.assertEqual(expected_result, result)

    def test_5(self):
        # Given
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        num3 = random.randint(1, 100)
        input_value = f"{num1}\n{num2},{num3}"
        expected_result = num1 + num2 + num3
        # When
        result = func(input_value)
        # Then
        self.assertEqual(expected_result, result)

    def test_6(self):
        with self.assertRaises(ValueError):
            func("-3")
        with self.assertRaises(ValueError):
            func("3,-4")
        input_value = f"{4}\n{-5},{9}"
        with self.assertRaises(ValueError):
            func(input_value)

    def test_7(self):
        # Given
        input_value1 = "2000"
        expected_result1 = 0

        input_value2 = f"{4}\n{1500},{9}"
        expected_result2 = 13
        # When
        result1 = func(input_value1)
        result2 = func(input_value2)
        # Then
        self.assertEqual(expected_result1, result1)
        self.assertEqual(expected_result2, result2)
    
    def test_8(self):
        # Given
        input_value1 = "//#44#5"
        expected_result1 = 49

        input_value2 = f"//a44a6"
        expected_result2 = 50
        # When
        result1 = func(input_value1)
        result2 = func(input_value2)
        # Then
        self.assertEqual(expected_result1, result1)
        self.assertEqual(expected_result2, result2)

    def test_9(self):
        # Given
        input_value1 = "//[###]44###5###10"
        expected_result1 = 59

        input_value2 = f"//[abba]44abba6"
        expected_result2 = 50
        # When
        result1 = func(input_value1)
        result2 = func(input_value2)
        # Then
        self.assertEqual(expected_result1, result1)
        self.assertEqual(expected_result2, result2)

    def test_10(self):
        # Given
        input_value1 = "//[###][#]44###5#10"
        expected_result1 = 59

        input_value2 = f"//[abba][#]44#6abba5"
        expected_result2 = 55
        # When
        result1 = func(input_value1)
        result2 = func(input_value2)
        # Then
        self.assertEqual(expected_result1, result1)
        self.assertEqual(expected_result2, result2)

if __name__ == "__main__":
    unittest.main()