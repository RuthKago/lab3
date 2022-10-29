#Exercise 6

def main():
    
    for i in range(20):
        print("X" * i)     #Starts from 1 x to ascending order by a margin of 1
        print("X" * (2*i))     
        print("X" * i + "O" * i)
        print("X" * i + "O" * (20-i))      


main()
