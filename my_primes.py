import my_binary_sort
import math

#Initialize a list of all single-digit primes
known_primes = [2, 3, 5, 7]
lowest_unchecked = 11

'''
    num: an integer
    returns True if num is prime and False otherwise
'''
def is_prime(num):
    global lowest_unchecked
    
    #Check whether num is a known prime
    if num in known_primes:
        return True
    if num < lowest_unchecked:
        return False

    #Check if any known primes are factors of num
    max_factor = math.sqrt(num)
    for p in known_primes:
        if p > max_factor:
            break
        if num % p == 0:
            return False

    #Check for new primes until we find a factor or run out of candidates
    while lowest_unchecked <= max_factor:
        if is_prime(lowest_unchecked):
            my_binary_sort.binary_insert(known_primes, lowest_unchecked, False)
            if num % lowest_unchecked == 0:
                lowest_unchecked += 2
                return False
        lowest_unchecked += 2 #The only even prime, 2, is already known

    #If we get here, num is prime
    my_binary_sort.binary_insert(known_primes, num, False)
    return True

'''
    num: an integer
    returns a list of the prime factors of num, including duplicates
'''
def prime_factors(num):
    global lowest_unchecked
    
    #Check whether num is a known prime
    if num in known_primes:
        return [num]

    #Check if any known primes are factors of num
    factor_list = []
    max_factor = math.sqrt(num)
    for p in known_primes:
        if p > max_factor or p > lowest_unchecked:
            break
        while num % p == 0:
            factor_list.append(p)
            num = num // p

    #Check for new primes until we run out of candidates
    while lowest_unchecked <= max_factor:
        if is_prime(lowest_unchecked):
            my_binary_sort.binary_insert(known_primes, lowest_unchecked, False)
            while num % lowest_unchecked == 0:
                factor_list.append(lowest_unchecked)
                num = num // lowest_unchecked
            max_factor = math.sqrt(num)
        lowest_unchecked += 2 #The only even prime, 2, is already known

    #If we get here, num is either 1 or prime
    if num > 1:
        my_binary_sort.binary_insert(known_primes, num, False)
        factor_list.append(num)
    return factor_list

if __name__ == '__main__':
    x = input('Int: ')
    while x != 'q':
        print(prime_factors(int(x)))
        x = input('Int: ')
