print """
Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
------------------------------------------------------------------------------

1 + 2 + 3 + 4 + ... + N = (N*(N+1)/2)

The sequences for any number divisible by n can be written as n*N*(N+1)/2...

Divisible by 3: 3 + 6 + 9 + 12 + ... + 999 = 3 * (1 + 2 + 3 + 4 + ... + 333)
"""

def sum_divisibles(a, b):
    """
    sum of n first multiples of x = x*n*(n+1)/2
    n = b/a
    """
    return a * (b/a) * ((b/a) + 1) / 2


print "result:"
print sum_divisibles(3, 999) + sum_divisibles(5, 999) - sum_divisibles(15, 999)
