import random
import math

max_PrimLength = 10000000


def Convert_Text(_string):

    ##Define this function such that it takes in a simple
    ##string such as "hello" and outputs the corresponding
    ##standard list of integers (ascii) for each letter in the word hello.

    #will store list
    integer_list = []

    for ch in _string:
        integer_list.append(ord(ch))

    return integer_list


print(Convert_Text("lindsay"))


def Convert_Num(_list):
    """
    Do the opposite of what you did in the Convert_Text
    function defined above.
    
    Define this function such that it takes in a list of integers
    and outputs the corresponding string (ascii).
    
    For example:
    _list = [104, 101, 108, 108, 111]
    _string = hello
    """
    _string = ''
    for i in _list:
        _string += chr(i)
    return _string


_list = [108, 105, 110, 100, 115, 97, 121]
print(Convert_Num(_list))


def Convert_Binary_String(_int):
    """
    Here, you need to define a function that converts an integer to
    a string of its binary expansion.
    
    For example:
    _int = 345
    bits = 101011001
    """
    bits = bin(_int)[2:].zfill(8)

    return bits


_int = 345
print(Convert_Binary_String(_int))


## A MIX OF SRIRAM'S AND MY OWN TRY
##b^n mod m..
##Define the function, pass parameters of b, n, and m
def FastModularExponentiation(b, n, m):
    #initialize the result to be 1
    res = 1
    #initialize the while loop to start when k is greater than 1. k will start at the first bit position.
    while n > 1:
        #if the least significant bit of the number is 1, not 0, move into the below code block. If the least significant bit is 0, skip it.
        if n & 1:
            #update the result variable with an assignment of the current result (1) multiplied by the current b
            # (starting at least significant bit so b = 3, 3mod645 = 3.)
            #this is only updated if the bit is 1!! If the bit wasn't 1, it would stay at res = 1
            res = (res * b) % m
        #regardless of if the bit is 1 or 0,
        # update b to be bsquared modulo m. For this first iteration it would be (3*3)mod645 = 9.
        # This is passed to the next iteration as b.
        b = b**2 % m
        #k will now be divided by 2, setting it up for the bit operation at the beginning of the
        #next iteration of the loop
        n >>= 1
    #At the very end, return the final b(111) multiplied by the final res(471) modulo m (645). =36
    return (b * res) % m


b = 2081
n = 937
m = 2537

print(FastModularExponentiation(b, n, m))


def Euclidean_Alg(a, b):
    """
    1. Calculate the Greatest Common Divisor of a and b.
    
    2. Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    The function must return a single integer 'x' which is
    the gcd of a and b.
    """
    while a != 0:
        q = b // a
        k = b % a
        b, a = a, k
    gcd = b
    return gcd


a = 77
b = 14

print("Euclidean_Alg:", Euclidean_Alg(a, b))


#EXTENDED EUCLIDEAN ALGORITHM
def EEA(m, n):
    #Setting the bezout's coefficients to (0,1) and (1,0) to begin the EEA process.
    x, y, u, v = 0, 1, 1, 0
    #'while m is not equal to 0' is also saying
    # 'continue to run this loop all the way down until m = 0 and then stop.'
    # this will also terminate the loop when n % m is 0, because m = k
    while m != 0:
        #during each iteration define q as n divided by m (integer).
        #define k as 'n modulo m'
        #the loop is keeping track of these as they change during each iteration
        q = n // m
        k = n % m
        #setting s to x-u*q and setting t to y-v*q
        #this is calculating s2 & t2 and will be used during the next iteration of the loop
        s = x - u * q
        t = y - v * q
        #at the end of each loop, n,m is set as m,k; x,y is set as u,v; u,v is set as s,t
        #it does this because when the loop reaches the terminating iteration (a = 1),
        # x & y need to be set as the previous u&v (s1 & t1).
        # This sets x & y with the final Bezout's Coefficients
        n, m = m, k
        x, y = u, v
        u, v = s, t

        #added the print statement to see what each variable is in each iteration of the loop
        #print(m, n, q, k, x, y, u, v, s, t)
    #After the last loop iteration, set the gcd(m,n) to n
    gcd = n
    #Return the gcd and (x,y). (x,y) are the bezout's coefficients. For encryption, d = x.
    return gcd, x, y


m = 252
n = 356

print(EEA(m, n))

#def random_prime():
#   count = 10000000
#  while True:
#     isprime = True
#    for x in range(2, int(math.sqrt(count) + 1)):
#       if count % x == 0:
#          isprime = False
#         break

#if isprime:
#   return count
#count += 1
#print("Prime number:", random_prime)


def Find_Public_Key_e(p, q):
    """
    Implement this function such that
    it takes 2 primes p and q.
    
    Use the gcd function that you have 
    defined before.
    
    The function should return 2 elements as follows:
    public key: n
    public key: e
    
    
    HINT: this function will run a loop to find e such 
    that e is relatively prime to (p - 1) (q - 1) 
    and not equal to p or q.
    """
    n = p * q
    w = (p - 1) * (q - 1)

    e = random.randint(1, w)
    gcd = Euclidean_Alg(e, w)
    while gcd != 1:
        e = random.randint(1, w)
        gcd = Euclidean_Alg(e, w)

    return e, n


p = 43
q = 59

print("Public key progress:", Find_Public_Key_e(p, q))
