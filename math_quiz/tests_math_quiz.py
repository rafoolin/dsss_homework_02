import unittest
from math_quiz import (
    generate_random_integer,
    generate_random_operator,
    perform_arithmetic_operation,
)


class TestMathGame(unittest.TestCase):
    def test_function_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        # Test a large number of random values
        for _ in range(1000):
            random_number = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= random_number <= max_val)

    def test_function_generate_random_operator(self):
        for _ in range(1000):
            random_operator = generate_random_operator()
            self.assertTrue(random_operator in ["+", "-", "*"])

    def test_function_perform_arithmetic_operation(self):
        test_cases = [(5, 2, "+", "5 + 2", 7), (5, 2, "-", "5 - 2", 3)]
        # These are only test that do not raise exception. We can test exceptions as well.
        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = perform_arithmetic_operation(num1, num2, operator)
            self.assertTrue(problem == expected_problem)
            self.assertTrue(answer == expected_answer)


if __name__ == "__main__":
    unittest.main()
