"""reversing a sentence using a temp file to store reversed words"""
def reverseS(sent):
    sent= sent.split#splitting the sentence 
    temp = sent[0]#adding sentence to temp
    sent[0] = sent[2]#reversing word 0 with word 2 
    sentence[2] = temp#adding reversed word to temp

def reverseS2(s):
    print(s)
    if s == []:#if the sentence is empty return nothing
          return
    else:
          print(s[len(s)-1])#if there is a sentence take the length and -1 to length of the sentence so it traverses the words backwards
          reverseS2(s=s[:-1])#using the split function to return the words in a reversed order 
          
sent = "The cat in the hat".split(" ")#final print of sentence split with somewhere to print the reversed sentence 
reverseS2(sent)

