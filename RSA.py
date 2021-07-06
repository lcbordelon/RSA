#def hello_world():
 #   return "Hello World"

#print(hello_world)


#FME ------------------------------------------------------------------------

#this is for b^(2^k) mod m
#def FastModularExponentiation(b, k, m):
 #   b %= m
  #  for _ in range(k):
   #     b = b ** 2 % m
    #return b



## A MIX OF SRIRAM'S AND MY OWN TRY
##b^k mod m..
##Define the function, pass parameters of b, k, and m
def FastModularExponentiation(b, k, m):
    #initialize the result to be 1
    res = 1
    #initialize the while loop to start when k is greater than 1. k will start at the first bit position. 
    while k > 1:
        #if the least significant bit of the number is 1, not 0, move into the below code block. If the least significant bit is 0, skip it.
        if k & 1:
            #update the result variable with an assignment of the current result (1) multiplied by the current b 
            # (starting at least significant bit so b = 3, 3mod645 = 3.)
            #this is only updated if the bit is 1!! If the bit wasn't 1, it would stay at res = 1
            res = (res * b) % m
        #regardless of if the bit is 1 or 0, 
        # update b to be bsquared modulo m. For this first iteration it would be (3*3)mod645 = 9. 
        # This is passed to the next iteration as b.
        b = b ** 2 % m
        #k will now be divided by 2, setting it up for the bit operation at the beginning of the
        #next iteration of the loop
        k >>= 1
    #At the very end, return the final b(111) multiplied by the final res(471) modulo m (645). =36
    return (b * res) % m 




b = 2081
k = 937
m = 2537

print(FastModularExponentiation(b, k, m))


#EXTENDED EUCLIDEAN ALGORITHM
def EEA(a, b):
    #Setting the bezout's coefficients to (0,1) and (1,0) to begin the EEA process.
    x,y, u,v = 0,1, 1,0
    #'while a is not equal to 0' is also saying 
    # 'continue to run this loop all the way down until a = 0 and then stop.'
    while a != 0:
        #during each iteration define q as b divided by a (integer). 
        #define k as 'b modulo a'
        #the loop is keeping track of these as they change during each iteration
        q, k = b//a, b%a
        #setting m to x-u*q and setting n to y-v*q
        #this is calculating m & n while will be used during the next iteration of the loop
        m, n = x-u*q, y-v*q
        #at the end of each loop, b,a is set as a,k; x,y is set as u,v; u,v is set as m,n
        #it does this because when the loop reaches the terminating iteration (a = 1), 
        # x & y need to be set as the previous m&n (s1 & t1). 
        # This sets x & y with the final Bezout's Coefficients
        b,a, x,y, u,v = a,k, u,v, m,n
    #After the last loop iteration, set the gcd(a,b) to b
    gcd = b
    #Return the gcd and (x,y). (x,y) are the bezout's coefficients. For encryption, d = x.
    return gcd, x, y


a = 13
b = 2436

print(EEA(a, b))