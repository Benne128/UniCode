"""A peice of code that determines the longest sequence of numbers within a array"""
array=[1,2,3,4,4,7,9,1,2,5,2,6,2]
def LongestSeq(array):
    count = 1
    lst= []
    for i in range(0, len(array)-1):#function to handle the range of the numbers in lenght of the array while it decreases by 1 element each time
        if array[i] >= array[i+1]: # if the array item is lager then array item +1 append that number to count
            lst.append(count)
            count=1
        elif array[i]<array[i+1]:#else if the item is less then array item +1 then add 1 to count 
            count+= 1
    lst.append(count)
    longest = max(lst)#longest is equal to the maximum of list 
    index=lst.index(longest)#index is equal to the lists index with longest taken as an argument
    sumLst = 0
    for i in range(index):#for all items within range of index 
        sumLst += lst[i]# add the sum of list to the list itself with the item/items taken as an arguments
    result = array[sumLst:sumLst+longest]
    return result#return the final reasult of the longest sequence 
print (LongestSeq(array))
