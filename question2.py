'''This function checks whether the given  number is prime or not'''
def is_prime(n):
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    for i in range(2, int(n ** 0.5) + 1):  # Check up to square root of n
        if n % i == 0:
            return False  # If divisible, it's not a prime
    return True  # If no divisors found, it's prime

# Example usage
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")