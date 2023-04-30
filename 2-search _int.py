#A python program to search for an interger in a list and print it's index
list2 = [1, 2, 3, 4]
n =int(input('enter the interger\n'))
def find_first_occurrence(my_list, num):
    ind = my_list.index(num) #Finding the index of an interger
    if num in my_list: 
      print(num,'is in the list') #
    else:
      print(num,'isnt in the list')  
    print('The index of an interger is',ind)
   
    
  

find_first_occurrence(list2, n)
          