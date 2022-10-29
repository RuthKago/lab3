#Exercise 9
#Write a program that reads a sentence from the user and prints it out word by word,
#and also prints the length of each word. Each word should be on a separate line


def main():
    sentence = str(input("Write any complete sentence: "))
    split = sentence.split()

    for word in range(0, len(split)):
        print(split[word], len(split[word]))
        
main()




                 
    
