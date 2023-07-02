questions = [

    {
        'question': 'What is the output of the following code?\nprint(2 * 3 + 4)',
        'options': ['a. 10', 'b. 14', 'c. 9', 'd. 7'],
        'answer': 'b'
    },
    {
        'question': 'Which data type is used to store a sequence of characters in Python?',
        'options': ['a. int', 'b. float', 'c. str', 'd. bool'],
        'answer': 'c'
    },
    {
        'question': 'What is the result of 2 + 2?',
        'options': ['a. 1', 'b. 3', 'c. 4', 'd. 5'],
        'answer': 'c'
    },
    {
        'question': 'What is the output of the following code?\nprint("Hello, world!")',
        'options': ['a. Hello, world!', 'b. "Hello, world!"', 'c. print("Hello, world!")', 'd. None of the above'],
        'answer': 'a'
    },
    {
        'question': 'Which of the following is an example of a Python keyword?',
        'options': ['a. module', 'b. function', 'c. for', 'd. print'],
        'answer': 'c'
    },
    {
        'question': 'What is the correct syntax for a multiline comment in Python?',
        'options': ['a. /* comment */', 'b. <!-- comment -->', 'c. // comment', 'd. # comment'],
        'answer': 'd'
    },
    {
        'question': 'Which method can be used to remove whitespace from the beginning and end of a string?',
        'options': ['a. strip()', 'b. trim()', 'c. remove()', 'd. delete()'],
        'answer': 'a'
    },
    {
        'question': 'What is the output of the following code?\nprint(3 > 5)',
        'options': ['a. True', 'b. False', 'c. None', 'd. Error'],
        'answer': 'b'
    },
    {
        'question': 'Which operator is used to perform exponentiation in Python?',
        'options': ['a. +', 'b. -', 'c. *', 'd. **'],
        'answer': 'd'
    },
    {
        'question': 'What is the result of the following code?\nprint("Hello, " + "world!")',
        'options': ['a. Hello, + world!', 'b. Hello,world!', 'c. Hello, world!', 'd. None of the above'],
        'answer': 'c'
    },
    {
        'question': 'What is the correct syntax for defining a function in Python?',
        'options': ['a. def my_function()', 'b. function my_function()', 'c. my_function def()', 'd. function my_function:'],
        'answer': 'a'
    },
    {
        'question': 'Which of the following data structures stores elements in a key-value pair format?',
        'options': ['a. list', 'b. tuple', 'c. dictionary', 'd. set'],
        'answer': 'c'
    },
    {
        'question': 'What is the output of the following code?\nprint(len("Python"))',
        'options': ['a. 5', 'b. 6', 'c. 7', 'd. None of the above'],
        'answer': 'a'
    },
    {
        'question': 'Which method is used to convert a string to lowercase in Python?',
        'options': ['a. upper()', 'b. capitalize()', 'c. lower()', 'd. swapcase()'],
        'answer': 'c'
    },
    {
        'question': 'What is the correct way to import the math module in Python?',
        'options': ['a. import Math', 'b. from math import', 'c. import math', 'd. include math'],
        'answer': 'c'
    },
    {
        'question': 'Which of the following is NOT a valid Python variable name?',
        'options': ['a. my_variable', 'b. 123variable', 'c. _myVariable', 'd. MY_VARIABLE'],
        'answer': 'b'
    },
    {
        'question': 'What is the output of the following code?\nprint(10 / 3)',
        'options': ['a. 3', 'b. 3.333', 'c. 3.33', 'd. 3.0'],
        'answer': 'b'
    },
    {
        'question': 'Which of the following is a mutable data type in Python?',
        'options': ['a. int', 'b. float', 'c. str', 'd. list'],
        'answer': 'd'
    },
    {
        'question': 'What is the correct way to create an empty list in Python?',
        'options': ['a. list()', 'b. []', 'c. ()', 'd. {}'],
        'answer': 'b'
    },
    {
        'question': 'What is the output of the following code?\nprint(not True)',
        'options': ['a. True', 'b. False', 'c. None', 'd. Error'],
        'answer': 'b'
    }
]

def run_quiz():
    score = 0
    for question in questions:
        print(question['question'])
        for option in question['options']:
            print(option)
        user_answer = input("Enter your option (a, b, c, d): ")
        if user_answer.lower() == question['answer']:
            score = score + 1
            print(score)
    print('Quiz Completed')
    print('Your score is : ',score, '/', len(questions))
run_quiz()
