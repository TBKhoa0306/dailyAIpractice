# The function check prime number
def isPrime(num):
    if num < 2:
        return False
    else:
        for i in range (2,int(num / 2) + 1):
            if num % i == 0:
                return False
    return True

# Output prime numbers from 1 to 100
print("Prime numbers from 1 to 100 are: ", end=" ")
for i in range(1, 100):
    if isPrime(i) == True:
        print(i, end=" ")