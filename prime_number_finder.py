# ------------------------------------------------------------
# Prime Number Finder
# Description:
#   Finds all prime numbers in a given range.
# Author: Abhishek Rana
# ------------------------------------------------------------

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    start = int(input("Enter start number: "))
    end = int(input("Enter end number: "))
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    print("Prime numbers:", primes)
