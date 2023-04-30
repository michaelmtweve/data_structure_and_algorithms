# Python Program to Print Right Angled Triangle Star Pattern
h = int(input("Please Enter the triangle height\n")) 
def print_right_triangle(height):
    for i in range(1, height + 1): #looping using a triangle height value
        for j in range(1, i + 1):
            print('*', end = '')
        print()
  
    
    
   
print_right_triangle(h)