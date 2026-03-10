import random

def generate_numbers(count):
    numbers = []
    for i in range(count):
        numbers.append(random.randint(1, 100))
    return numbers


def multiply_numbers(numbers):
    result = []
    for n in numbers:
        result.append(n * 10)
    return result


def calculate_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def main():
    print("Simple Random Data Processor")

    nums = generate_numbers(11)
    print("Generated numbers:", nums)

    multiplied = multiply_numbers(nums)
    print("After multiply:", multiplied)

    total = calculate_sum(multiplied)
    print("Total sum:", total)


if __name__ == "__main__":
    main()