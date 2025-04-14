"""
This module generates a Fibonacci sequence based on user input.
"""

def generate_fibonacci(n):
    """
    Generate a Fibonacci sequence with 'n' terms.

    Args:
        n (int): The number of terms to generate.

    Returns:
        list: A list containing the Fibonacci sequence.
        str: A message if 'n' is not positive.
    """
    if n <= 0:
        return "Please enter a positive integer."
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]


if __name__ == "__main__":
    number_of_terms = int(input("Enter the number of Fibonacci terms to generate: "))
    print("Fibonacci Sequence:")
    print(generate_fibonacci(number_of_terms))
