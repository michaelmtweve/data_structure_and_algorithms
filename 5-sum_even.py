# Python function to print the sum of Even Numbers in a list

list1 = [10, 21, 4, 45, 66, 93]  # list of numbers
def sum_even_numbers(my_list):
    even_number=[]
 
    # iterating each number in list
    for num in my_list:
 
    # checking condition
        if num % 2 == 0:
            even_number.append(num)
            
        
        
    total=sum(even_number)    
    print(total)
        
        
        
sum_even_numbers(list1)