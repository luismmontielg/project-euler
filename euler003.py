print """

Problem 3. Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
----------------------------------------------------------------------------
Using fundamental theorem of arithmetic:

There is only one unique set of prime factors for a number

330 = 2  3  5  11
"""

def largest_prime_factor(num):
    # start with first prime = 2
    current_number = 2
    prime_fact = 1
    while current_number * current_number <= num:
        if num % current_number == 0:  # is factor
            num = num / current_number  # keep factoring
            prime_fact = current_number
        else:
            # try with next number
            current_number = current_number + 1
    if num > prime_fact:
        return num
    return prime_fact

n = 600851475143 
print "largest prime factor of %d is %d"% (n, largest_prime_factor(n))
