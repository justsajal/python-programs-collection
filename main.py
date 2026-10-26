from dataclasses import asdict, dataclass
from typing import List


def factorial(number: int) -> int:
    """Return the factorial of a non-negative integer."""
    if number < 0:
        raise ValueError("Factorial is not defined for negative integers.")

    result = 1
    for value in range(2, number + 1):
        result *= value
    return result


def fibonacci(count: int) -> List[int]:
    """Return the first count Fibonacci numbers, starting with 0, 1."""
    if count < 0:
        raise ValueError("Count cannot be negative.")

    sequence = []
    first, second = 0, 1

    for _ in range(count):
        sequence.append(first)
        first, second = second, first + second

    return sequence


@dataclass
class Student:
    """Example structure that can be converted to a dictionary."""
    name: str
    course: str
    year: int


def structure_to_dictionary(student: Student) -> dict:
    """Convert a dataclass object into a regular dictionary."""
    return asdict(student)


def read_non_negative_integer(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter zero or a positive integer.")
                continue
            return value
        except ValueError:
            print("Invalid input. Enter a whole number, such as 5.")


def main() -> None:
    while True:
        print("\n=== Python Programs Collection ===")
        print("1. Factorial")
        print("2. Fibonacci sequence")
        print("3. Structure-to-dictionary conversion")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            number = read_non_negative_integer("Enter a non-negative integer: ")
            print(f"{number}! = {factorial(number)}")
        elif choice == "2":
            count = read_non_negative_integer("How many Fibonacci numbers? ")
            print(fibonacci(count))
        elif choice == "3":
            student = Student(name="Aarav", course="B.Tech CSE", year=2)
            print(structure_to_dictionary(student))
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
