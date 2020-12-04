# test suite for the Binomial Coefficient Algorithm

# Note: this implementation is the Dynamic Programming solution to the binomial coefficient
# from geeksforgeeks.com. The link is:
# https://www.geeksforgeeks.org/binomial-coefficient-dp-9/

import random
# Please not that we use math.comb which is only available on Python 3.8 or above.
import math

def binomialCoeff(n , k):

    # Declaring an empty array
    C = [0 for i in range(k+1)]
    C[0] = 1

    for i in range(1,n+1):

        # Compute next row of pascal triangle using
        # the previous row
        j = min(i ,k)
        while (j>0):
            C[j] = C[j] + C[j-1]
            j -= 1

    return C[k]


# This function tests the binomial coefficient function by generating a random int for the value of n and k, calculating the binomial coefficient of those values, and asserting that the function calculated the same value.
def test_binomialCoeff():
    n = random.randint(0, 10000)
    k = random.randint(0,n)


    assert(binomialCoeff(n,k) == math.comb(n,k))
