# TODO

def main():

    #TODO: Prompt for pyramid height (between 1 and 8)
    height = 0
    while (height < 1 or height > 8):
        height = int(input("Height: "))
    
    #TODO: Print pyramid
    for i in range(height):
        print(end='')
        for j in range(height - (i + 1)):
            print(' ', end='')
        k = height
        while k > height - (i + 1):
            print('#', end='')
            k -= 1
        print()
        
if __name__ == "__main__":
    main()