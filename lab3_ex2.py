def main():
    print ("#Exercise 2#")
    str = "This sentence has 27 chars."
    print (len(str))     #It gives the number of characters in the string
    print(str[-1])      #Its give the last character in the sentence
    # print(str [len(str)]) gives an error IndexError: string index out of range
    print(str [len(str)-1]) #It gives the last character in the sentence
    print (str [4])        #It gives the 4 character in the sentence which is an empty space
    print (str [:4])       #It gives the first letters in the sentence
    print (str [-6:])    
    print (str [-9:-7])
    print (str [4:1])       #It gives an empty space
    print (str [-10:27])
    print()
    print ("#The end of Exercise 2#")
    print()
    
           
main()
