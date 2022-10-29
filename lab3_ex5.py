#Exercise 5



def main():
    str = "This sentence has 27 chars."
    
    for i in range((len(str)-1), -1, -1):
        print(str[i], end = '')



main()


#Method 2 with using negatives

print()


def main_2():
    str = "This sentence has 27 chars."

    for i in range(len(str)):       
        print ([i * -1], end="")


main()
                    
    



