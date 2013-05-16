print """
Problem 4. Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def generate_palindrome(num):
    return int(str(num) + str(num)[::-1])

def get_largest_palindrome_product():
    prod = 0
    start = 999
    found = False
    while start > 99:
        start = start - 1
        palindrome = generate_palindrome(start)  # Generate desc palindromes
        print palindrome
        i = 999
        while i > 99:
            if palindrome > i * i or palindrome / i > 999:
                break
            if palindrome % i == 0:
                return i, palindrome / i, palindrome
            i = i - 1
    return -1, -1, -1

(first, second, palindrome) = get_largest_palindrome_product()
print "palindrome %d, factors: %d * %d" % (palindrome, first, second)
