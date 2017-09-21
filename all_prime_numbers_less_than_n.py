import math
import sys
import time
def prime_numbers(n):
    import time
    ls = [True] * (n + 1)
    ls[0] = False
    ls[1] = False
    #root = math.floor(math.sqrt(n))

    for c1 in range(2, n + 1):
        root = math.floor(math.sqrt(c1))
        #if current number is already flagged as non prime. No need to check
        if ls[c1]:
            for c2 in range(2, root):
                if math.floor(c1 % c2) == 0:
                    ls[c1] = False
        #sieve multiples of current prime number
        #e.g. multiples of 2 will not be be prime numbers. therefore filter them
        if ls[c1] == True:
            for c3 in range(2 * c1, n + 1, c1):
                ls[c3] = False

    list_of_primes = []
    for index, value in enumerate(ls):
        if value:
            list_of_primes.append(index)
    return list_of_primes

if __name__ == '__main__':
    then = time.time()
    print('number of primes', len(prime_numbers(int(sys.argv[1]))))
    print(' time taken ', time.time() - then, ' seconds')
