import math

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1 ):
        if n % i == 0:
            return False
    return True

def truncateN(n, lr):
    ns = str(n)
    truncated = []
    for i in range(0,len(ns)):
        if not lr:
            truncated.append(int(ns[:len(ns)-i]))
        else:
            truncated.append(int(ns[i:]))
    return truncated

completePrimes = []
for i in range(9,2540160, 2):
    completePrime = True
    for t in truncateN(i, False):
        if not isPrime(t):
            completePrime = False
    for t in truncateN(i, True):
        if not isPrime(t):
            completePrime = False
    if completePrime:
        completePrimes.append(i)
        if len(completePrimes) == 11:
            break
        
print(sum(completePrimes))
