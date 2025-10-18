if __name__ == "__main__":

    def fibonacci_generator(stop=10):
        current_fib, next_fib = 0, 1
        for _ in range(0, stop):
            fib_number = current_fib
            current_fib, next_fib = (
                next_fib, current_fib + next_fib
            )
            yield fib_number
    
    print(list(fibonacci_generator()))
