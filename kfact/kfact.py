# kfact
# This program computes the k-factor factorization with the lowest spread
# Useful for dividing a non-square area into equally sized parcels

def kfact(N,K):
    for i in range(15):
        pfact = badFact(i)  
        print("%d gives:"%(i))
        print(pfact)



def badFact(N):
    # I can only imagine there's a better way to do this
    testProduct = 1
    facts = []

    for i in range(2,N/2 + 1):

        if (N % i) == 0:
            while testProduct < N:
                print(testProduct)
                if testProduct*i <= N:
                    facts.append(i)
                    testProduct *= i
        
        if testProduct == N:
            break
    if facts == []:
        # it's prime
        facts = [N]

    return facts


if __name__ == "__main__":
    kfact(240,3)
