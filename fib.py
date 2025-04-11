# Fibonacci sequence generator
def generate_fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer."
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[:n]

# User input
number_of_terms = int(input("Enter the number of Fibonacci terms to generate: "))
print("Fibonacci Sequence:")
print(generate_fibonacci(number_of_terms))
