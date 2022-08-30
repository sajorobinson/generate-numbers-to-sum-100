import random

# This is how many resulting numbers you want to create
results = 3

# This is a container for the number generating process
numbers = []

# This is a container for the output results
outputs = []

def generate_random_numbers(results):

    while results > 0:
        n = random.randint(0, 100)
        numbers
        numbers.append(n)
        results = results - 1

def normalize_numbers(numbers):

    sum = 0

    for number in numbers:
        sum = sum + number

    for number in numbers:
        division = number / sum
        result = division * 100
        outputs
        outputs.append(result)

def print_output(output):

    for output in outputs:
        print(output)

generate_random_numbers(results)
normalize_numbers(numbers)
print_output(outputs)
