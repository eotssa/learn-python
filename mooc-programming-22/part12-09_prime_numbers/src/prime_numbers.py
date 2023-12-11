# Write your solution here
def prime_numbers():
    def is_prime(num):
        if num < 2:
            return False

        for i in range (2, num - 1):
            if num % i == 0: 
                return False
        return True

    num = 2
    while True:
        if is_prime(num):
            yield num 
        num += 1

if __name__ == "__main__":

    # Test the generator
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))