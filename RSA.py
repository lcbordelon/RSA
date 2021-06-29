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




b = 1568160359
k = 20000446
m = 645

print(FastModularExponentiation(b, k, m))


