# TODO

def main():

    #TODO: Prompt for pyramid height (between 1 and 8)
    height = 0
    while (height < 1 or height > 8):
        height = int(input("Height: "))

    #TODO: Print pyramid
    for i in range(height):
        print(i, end='')
        for j in range(height - i):
            print(j, end='')
        for k in range(height - i):
            k = height
            print(k, end='')
            k -= 1
        print('')
        
if __name__ == "__main__":
    main()