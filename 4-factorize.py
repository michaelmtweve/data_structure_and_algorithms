#A python program to give a list of prime factors of a number
n=int(input('Enter the number\n'))
def factorize(number):
    prime_factorials = [] #Declearing an empty list of prime factors
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            prime_factorials.append(divisor) #Putting the values in one list
            number = number/divisor
        else:
            divisor = divisor + 1
    return prime_factorials


if __name__ == "__main__":
    print(factorize(n))