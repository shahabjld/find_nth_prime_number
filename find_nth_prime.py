'''

Created on July 26, 2017
@author: jalalvand

This code returns the nth prime number. 
n = [1..10000000].

egs:
  python find_nth_prime.py 10001

'''

import sys
import math

def nth_prime( n ):

    prime_numbers = [2, 3] #the first and second primes
    if n == 1  or n == 2:
        print prime_numbers[n-1]

    current_num = 5 #start finding the primes from 5

    while not len(prime_numbers) == n: #check if nth prime is not found yet

        is_prime = True  #assume the current number is a prime

        i = 1 #skip the first prime. We won't consider the even numbers.
        while prime_numbers[i] <= math.sqrt( current_num ): #if current_num is not prime, then it is dividable by a prime number between [2,sqrt(current_num)]
	    if current_num % prime_numbers[i] == 0:
                is_prime = False #current_num is not prime
                break
            i += 1
        if is_prime:
            prime_numbers.append(current_num)

        current_num += 2 #do not consider even numbers

    return prime_numbers[-1] #return the last found prime number


def error_message():
    print 'Error!!! the entered value is not a valid integer.'
    print 'Please enter a number between 1 to 10000000.'
    print 'egs:\n  >>> python find_nth_prime.py 1001'


if __name__ == '__main__':

    try:
        n = int(sys.argv[1])
        if n >= 1 and n <= 10000000:            
            nthp = nth_prime(n) # find the nth prime
            print 'The %dth prime number is: %d\n' % (n,nthp)
        else:
	    error_message()

    except:
        error_message()

