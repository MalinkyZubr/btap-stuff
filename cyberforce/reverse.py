import sys

def main():
    # if at least one argument is not supplied, return None
    if len(sys.argv) != 2: 
        print('Invalid args')
        return None

    password = sys.argv[1] # password is the first argument passed at program runtime start
    counter = 0 # counter initially at 0
    vals = list('tfzbwlyzljylawhzzdvyk') # list of characters

    # if the length of the password provided is not equal to the length of the list, return None
    if len(password) != len(vals):
        print('incorrect')
        return None
    
    # while the counter is less than the length of the character list
    while counter < len(password):
        x = ord(password[counter]) + 7 # x is the ascii value of the character + 7. a -> h
        
        # if the value of x is greater than z, wrap it back around 
        if x > ord('z'):
            x -= 26

        # 7 shift caesar cipher

        if chr(x) != vals[counter]:
            print ('incorrect')
            return None
        counter += 1
    print('correct')

if __name__ == '__main__':
    main()

    # password is mysupersecretpassword