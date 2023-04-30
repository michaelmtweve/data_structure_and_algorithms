""" A Python Function to convert integer to Roman values"""

n=int(input("Enter the number\n")) #prompting a user to enter the number

def  int_to_roman(n):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
     
    while n:
        div = n // num[i]
        n %= num[i]
 
        while div:
            print(sym[i], end = "")
            div -= 1
        i -= 1
 

if __name__ == "__main__":
    number = n
    print("Roman value is:", end = " ")
   
int_to_roman(number)