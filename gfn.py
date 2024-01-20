#This code is to genrate fibonacci numbers 
#defining function
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq
# Example i usage
n = 20
fibonacci_sequence = fibonacci(n)
print(fibonacci_sequence)