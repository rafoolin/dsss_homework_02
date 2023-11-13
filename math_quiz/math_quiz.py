import random


def generate_random_integer(min_value, max_value):
    """
    Generate a random integer within the specified range.(Including both end points)

    Parameters:
    - minimum (int): The minimum possible value for the random integer.
    - maximum (int): The maximum possible value for the random integer.

    Returns:
    int: A random integer between the user specified minimum and maximum values.

    Raise:
    Error: If min_value is bigger than max_value, it raise an error.

    Example:
    >>> generate_random_integer(1, 9)
    5
    >>> generate_random_integer(2,4)
    3
    >>> generate_random_integer(2,1)
    ValueError: empty range in randrange(2, 1)
    """
    return random.randint(int(min_value), int(max_value))


def generate_random_operator():
    """
    Generate a random arithmetic operator: '+', '-', or '*'.

    Returns:
    str: A randomly chosen arithmetic operator between '+', '-', or '*' options.

    Example:
    >>> generate_random_operator()
    '+'
    """
    return random.choice(["+", "-", "*"])


def perform_arithmetic_operation(left_operand, right_operand, operator):
    """
    Perform an arithmetic operation based on the provided numbers and operator.

    Parameters:
    - left_operand (int): The first/left operand.
    - right_operand (int): The second/right operand.
    - operator (str): The arithmetic operator.

    Returns:
    tuple: A tuple containing the expression (str) and the result of the expression (int).

    Raises:
    Exception: If an operator is not +, - or *.

    Example:
    >>> perform_arithmetic_operation(5, 3, '+')
    ('5 + 3', 8)
    >>> perform_arithmetic_operation(5, 3, 'q')
    Exception: Wrong operator!, only valid operators are "+", "-" and "*"
    """
    expression = f"{left_operand} {operator} {right_operand}"
    result = 0
    match operator:
        case "+":
            result = left_operand + right_operand
        case "-":
            result = left_operand - right_operand
        case "*":
            result = left_operand * right_operand
        case _:
            raise Exception(
                'Wrong operator!, only valid operators are "+", "-" and "*"'
            )
    return expression, result


def start_math_quiz():
    """Run a math quiz game where the user needs to solve randomly generated arithmetic problems.

    User will collect points and will get the total earned score point on the screen.

    Returns:
    None

    Example:
    >>> math_quiz()
    Welcome to the Math Quiz Game!
    You will be presented with math problems, and you need to provide the correct answers.

    Question: 3 + 3
    Your answer: 6
    Correct! You earned a point.

    Question: 1 * 8
    Your answer: 7
    Wrong answer. The correct answer is 8.

    Question: 5 - 2
    Your answer: 3
    Correct! You earned a point.

    Game over! Your score is: 2/3
    """
    earned_score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print(
        "You will be presented with math problems,"
        " and you need to provide the correct answers."
    )

    for _ in range(total_questions):
        number1 = generate_random_integer(1, 10)
        number2 = generate_random_integer(1, 5.5)
        operator = generate_random_operator()

        problem, answer = perform_arithmetic_operation(number1, number2, operator)
        print(f"\nQuestion: {problem}")
        user_answer = None
        while user_answer == None:
            try:
                user_answer = input("Your answer: ")
                user_answer = int(user_answer)
                break
            except:
                print("Try again!", end=" ")
                user_answer = None

        if user_answer == answer:
            print("Correct! You earned a point.")
            earned_score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {earned_score}/{total_questions}")


if __name__ == "__main__":
    start_math_quiz()
