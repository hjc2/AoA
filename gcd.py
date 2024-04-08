
# iterative
def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

# recursive
def gcdR(a, b):
    if(b == 0):
        return(a)
    return gcd(b, a % b)

#
def printGCD(a,b):
    print("the GCD of " + str(a) + " and " + str(b) + " is " + str(gcd(a,b)))
