#A python function to test whether a number is prime or not
n=int(input("Enter the number\n"))
def is_prime(number):

   # If given number is greater than 1
    if number > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(number/2)+1):
            """ If num is divisible by any number between
             2 and n / 2, it is not prime"""
            if (number % i) == 0:
                print(False)
                break
        else:
            print(True)
    else:
        print(False)   

is_prime(n)