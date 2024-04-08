
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


def generatorList(G, m):
    F = set()
    for a in G:
        K = G.copy()
        for i in range(0,100):
            # if(pow(a, i), m % 1):
            res = pow(a, i) % m
            if(res and res in K):
                print(str(a) + "^" + str(i) + " mod " + str(m) + " = " + str(pow(a, i) % m))
                K.remove(res)

        if(len(K) == 0):
            F.add(a);
            print(str(a) + " satisfies all elements")
        else:
            print(str(a) + " does not satisfies all elements")
    print("----")
    print(str(F) + " is the list of primitive roots")



def modList(m):
    F = set()
    for i in range(0,m):
        if(gcd(i, m) == 1):
            F.add(i)
    # print(str(F))
    print("U_" + str(m) + " = " + str(F))
    print("----")
    generatorList(F, m)


# generatorList({1, 5, 7, 11, 13, 17}, 18)
modList(10)

