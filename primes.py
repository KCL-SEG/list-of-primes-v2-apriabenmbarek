"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("The number of primes chosen is either 0 or a negative number.")
    list = []
    num = 2
    while len(list) < number_of_primes:
        prime = True
        for x in range(2, num-1):
            if num % x == 0:
                prime = False
        if prime == True:
            list.append(num)
        num = num + 1
    return list
