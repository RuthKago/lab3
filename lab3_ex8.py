#Exercise 8

#Write a program that reads a digit (0-9) from the user and prints its name

def main():
    number = int(input("Enter a number between 0 and 9: "))
    number_names = ['Zero', 'One', 'Two', 'Three', 'Four',
           'Five', 'Six', 'Seven', 'Eight', 'Nine']

    print(f"{number} -> {number_names[number]}")

    
main()
