#A python function to show the frequency of characters in a string
string1='lost in the middle of nowhere'
def character_frequency(string):
 
    #frequency of each element in string
    all_freq = {}
 
    for i in string:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
 
    # printing result
    print(str(all_freq))


character_frequency(string1)