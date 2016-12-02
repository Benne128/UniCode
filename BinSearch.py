"""A binary search addapted to find if the numbers entered by the user are within a sequence"""
def BinSearch(list, low, high, start, end):
    if end < start:#if the end is less then the start return false
        return False
    else:
        mid=int((end - start)/2) + start# initialize the end - start divide it by two and add this to the start again 
        if list[mid]>=high:#if the mid point of the list is lager or equal then the high value then decrease the mid point by 1
            return BinSearch(list, low, high, start, mid-1)
        elif list[mid]<=low:# else if the mid point is less or equal to the low value then increase the mid point  
            return BinSearch(list, low, high, mid+1, end)
        else:
            return True
list =[2,5,7,9,16,27,32]#simple list
start = 0
end = len(list)-1
low = int(input("What is the low value ?:"))#gain input from user to calculate the low value in the sequence
high = int(input("What is the high value ?:"))#gain input from user to calculate the high value in the given sequence 
print(BinSearch(list, low, high, start, end))
