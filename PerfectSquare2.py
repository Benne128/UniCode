#!/usr/bin/python
"""A peice of code that returns the numbers that could be perf squares in a list"""
list= [17, 5, 12, 3, 9, 2]#creating a small list

#initilizing the function to handle and execute the function 
def square(list):
    x = 9
    for i in list:
        """for items in list"""
            list = sorted(i for i in list if x >= i)
            """The list is equal to items in list if conditions are met"""
            return [i ** 2 for i in list] #return the final funtion 
        
print ("The Higest perfect square : ", square(list,)) 
#final print statement where you call your function with the argument list
