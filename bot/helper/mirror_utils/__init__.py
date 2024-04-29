from typing import List, Optional

def is_prime(n: int) -> bool:
    """
    Returns True if the input integer n is a prime number, and False otherwise.

    A prime number is a natural number greater than 1 that has no positive
    divisors other than 1 and itself. This function checks if a number is prime
    by iterating from 2 to the square root of n and checking if n is divisible
    by any of these numbers. If n is not divisible by any number in this range,
    it is considered a prime number.

    :param n: The integer number to check for primality.
    :return: A boolean value indicating whether n is prime or not.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def largest_prime(numbers: List[int]) -> Optional[int]:
    """
    Returns the largest prime number in the input list of integers.

    If the input list is empty, this function returns None. The function iterates
    through the input list and checks each number for primality using the
    is_prime() function. If a number is prime and is greater than the current
    largest prime, it becomes the new largest prime.

    :param numbers: The list of integers to find the largest prime in.
    :return: The largest prime number in the input list, or None if the list is empty.
    """
    largest_prime: Optional[int] = None
    for num in numbers:
        if is_prime(num):
            if largest_prime is None or num > largest_prime:
                largest_prime = num
    return largest_prime
