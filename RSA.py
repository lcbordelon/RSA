import random
import math
import decimal

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


_string = "Tell me your favorite zoo animal(s)."
print(Convert_Text(_string))


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


_list = [84, 101, 108, 108, 32, 109, 101, 32, 121, 111, 117, 114, 32, 102, 97, 118, 111, 114, 105, 116, 101, 32, 122, 111, 111, 32, 97, 110, 105, 109, 97, 108, 40, 115, 41, 46]
print("USE THIS:", Convert_Num(_list))


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


a = 418543
b = 13

print("Euclidean_Alg:", Euclidean_Alg(a, b))

#m = 252
#n = 356

#print(EEA(m, n))

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

    return e


p = 571
q = 733

print("Public key progress:", Find_Public_Key_e(p, q))


#EXTENDED EUCLIDEAN ALGORITHM
def Find_Private_Key_d(m, n):

    x, y, u, v = 0, 1, 1, 0

    while m != 0:

        q = n // m
        k = n % m

        s = x - u * q
        t = y - v * q

        n, m = m, k
        x, y = u, v
        u, v = s, t

    gcd = n
    #Return the gcd and (x,y). (x,y) are the bezout's coefficients. For encryption, d = x.
    return gcd, x, y


def main():
    p = 571
    q = 733
    e = 13

    n = p * q

    w = (p - 1) * (q - 1)

    gcd, x, y = Find_Private_Key_d(e, w)
    d = x

    return d


print("This is d:", main())


def Encode(n, e, message):
    """
    Here, the message will be a string of characters.
    Use the function Convert_Text from 
    the basic tool set and get a list of numbers.
    
    Encode each of those numbers using n and e and
    return the encoded cipher_text.
    """

    cipher_text = []
    print(message)

    for ltr in message:
        en = (ltr**e)
        print(en)
        C = en % n
        print(C)
        cipher_text.append(C)

    return cipher_text


n = 418543
e = 13
message = Convert_Text(_string)

print("SEND THIS..ENCODED MSG:", Encode(n, e, message))


def Decode(n, d, cipher_text):
    """
    Here, the cipher_text will be a list of integers.
    First, you will decrypt each of those integers using 
    n and d.
    Later, you will need to use the function Convert_Num, that converts the integers to a string, 
    from the basic toolset to recover the original message as a string. 
    
    """
    msg = []

    for num in cipher_text:

        M = (num**d) % n
        msg.append(M)

        print(M)
        print(msg)

    message = ''
    return message


n = 418543
d = 160477
#cipher_text = Encode(n, e, message)
cipher_text = [230487, 182599, 229476, 229476, 
25439, 33798, 182599, 25439, 308894, 355570, 129591, 209063, 25439, 120553, 3904, 294194, 355570, 209063, 107955, 
291951, 182599, 25439, 396296, 355570, 355570, 25439, 3904, 152567, 107955, 33798, 3904, 229476, 61680, 242273, 9120, 333242]

#print("Decoded message #'s:", Decode(n, d, cipher_text))
#print("Converted decoded message #'s into letters:", Convert_Num(message))