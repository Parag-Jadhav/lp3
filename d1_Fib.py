#ITERATIVE
def fibonacci_iterative_with_steps(n):
    step_count = 0
    
    if n == 0:
        return 0, step_count
    elif n == 1:
        return 1, step_count
    
    a, b = 0, 1
    for I in range(2, n + 1):
        a, b = b, a + b
        step_count += 1  # Increment step count for each addition
    
    return b, step_count

# Test the iterative function
n = 10
fib_value, steps = fibonacci_iterative_with_steps(n)
print(f"Iterative Fibonacci of {n}: {fib_value}, Steps: {steps}")


#RECURSIVE 
def fibonacci_recursive_with_steps(n, step_count=0):
    step_count += 1  # Count each function call
    
    if n == 0:
        return 0, step_count
    elif n == 1:
        return 1, step_count
    else:
        fib1, step_count = fibonacci_recursive_with_steps(n - 1, step_count)
        fib2, step_count = fibonacci_recursive_with_steps(n - 2, step_count)
        return fib1 + fib2, step_count

# Test the recursive function
n = 10
fib_value, steps = fibonacci_recursive_with_steps(n)
print(f"Recursive Fibonacci of {n}: {fib_value}, Steps: {steps}")

#TC= iterative:O(n) recursive:O(2^n)
#SC= iterativee=O(1) recusrive:O(n)