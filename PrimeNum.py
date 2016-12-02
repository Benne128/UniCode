"""checking to see if a number entered by the user is prime or not"""
def PrimeNum (f,j):
    if f<2:
        print (f, " This is not a prime number")
    else:
        #call function to handle with remainders
        mod = f % j#using mod fuction to devide f and j, mod handles remainders
        if  j ==1:
            print (f, "This is a prime number !")
        elif mod ==0:
            print(f, "This is not a prime number")
            #make call so that the number decreases every time 
        else:
            j = j -1
            PrimeNum(f,j)
#get user input to calculate prime number
f = int(input("Please enter a number"))
j = f-1
PrimeNum(f,j)
