# Create a list with the first ten triangular numbers
# (see https://oeis.org/A000217)

L = [ i*(i+1)/2 for i in range(10)]

# Create a function to test if a number is prime
def is_prime(n):
    """
    Test if ``n`` is a prime.
    """
    if n < 1:
        return "Input number is either negative or 0" 
    elif n in [1,2]:
        return True 
    elif n%2==0:
        return False 
    else:
        for i in range(3,int(n**0.5)+1,2):
            if n%i==0:
                return False 
                break
        else:
            return True

# Tests
# is_prime(2033) == False
# is_prime(2039) == True

# Create a function which returns a list of the first ten prime numbers
# greater than or equal to n

def next_ten_primes(n):
    """
    Return the list of the first ten prime numbers greate than or equal to n
    """
    nxtprime=[]
    if n==2:
        nxtprime=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    elif n < 1:
        print "Input number is either negative or 0"
    else:
        nxtprime=[]
        k=1
        m=n
        while k<=10:
            if is_prime(m)== True:
                nxtprime.append(m)
                k+=1
            m+=2
    return nxtprime


# Tests
# next_ten_primes(2033) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]
# next_ten_primes(2039) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]






