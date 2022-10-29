#Print all the characters with ASCII code 1 to 255, using a for loop (you need to use
#chr() ).


def main():
    for i in range (256):      #states that the statements inside it gets executed 256 number of times with value of i from 0 to 255.
        ch = chr(i)
        print(i, ch)

main()
