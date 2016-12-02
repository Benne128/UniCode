"""remove vowles from a sentence reasulting in a print of remaining letters"""
def vocals(inputl, output, counter):
    if index == "a" or "e" or "i" or "o" or "u":
        del inputl[counter]#if the counter finds any of these words del them
        vocals(inputl,output,counter)
    else:
        output.append([inputl[counter])#else append the word to counter
        del inputl[counter]
        print(output)
    if counter < len(inputl) +1:#while length of list is larger then count list +1
        vocals(inputl, output, counter)
inputl=list("handsome")
output =[]
counter= 0
vocals(inputl, output, counter)
    
