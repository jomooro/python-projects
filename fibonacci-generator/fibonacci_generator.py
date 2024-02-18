class FibonacciGenerator:
    def __init__(self):
        self.memo = {}

    def _fibonacci_recursive(self, n):
        if n <= 1:
            return n
        if n not in self.memo:
            self.memo[n] = self._fibonacci_recursive(n - 1) + self._fibonacci_recursive(n - 2)
        return self.memo[n]

    def _fibonacci_iterative(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def generate_sequence(self, count):
        if not isinstance(count, int) or count <= 0:
            raise ValueError("Count must be a positive integer.")
        return [self._fibonacci_iterative(i) for i in range(count)]

    def generate_range(self, start, end):
        if not all(isinstance(x, int) and x >= 0 for x in [start, end]):
            raise ValueError("Start and end must be non-negative integers.")
        
        sequence = []
        i = 0
        while True:
            current_fibonacci = self._fibonacci_iterative(i)
            if current_fibonacci > end:
                break
            if current_fibonacci >= start:
                sequence.append(current_fibonacci)
            i += 1
        return sequence

    def get_nth_fibonacci(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("n must be a non-negative integer.")
        return self._fibonacci_iterative(n)

# Example usage:
fibonacci_gen = FibonacciGenerator()

# Generate and print the first 10 Fibonacci numbers
sequence_10 = fibonacci_gen.generate_sequence(10)
print("First 10 Fibonacci numbers:", sequence_10)

# Generate and print Fibonacci numbers within the range [10, 100]
range_sequence = fibonacci_gen.generate_range(10, 100)
print("Fibonacci numbers in the range [10, 100]:", range_sequence)

# Get the 15th Fibonacci number
nth_fibonacci = fibonacci_gen.get_nth_fibonacci(15)
print("15th Fibonacci number:", nth_fibonacci)
