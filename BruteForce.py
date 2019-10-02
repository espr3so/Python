from itertools import product

def findPassword(chars,function,show=50,format_="%s"):
    """
    This function finds and returns a password and returns the number of retries.
    
     Stop chars: Digits a password can have.
    
     Stop function: Function that must have a parameter to
     receive a password. If the return of this function is True, the password attempted
     is considered the correct one.

     Stop show: Shows one attempt every X attempts.

     Stop format_: Format in which the password will be printed.
    """

    password = None
    attempts = 0
    size = 1
    stop = False
    
    while not stop:

        # Gets all possible combinations with the digits of the "chars" parameter.
        for pw in product(chars,repeat=size):
            
            password = "".join(pw)
            
            # Print the password that will be tried.
            if attempts % show == 0:
                print(format_%password)

            # Checks if the password is the correct one.
            if function(password):
                stop = True
                break
            else:
                attempts += 1
        size += 1
        
    return password,attempts


def getChars():
    """
    This is the method for obtaining a list of all letters of the alphabet and all numbers.
    """
    chars = []

    # This adds all capital letters to the list
    for id_ in range(ord("A"),ord("Z")+1):
        chars.append(chr(id_))

    # This adds lowercase letters
    for id_ in range(ord("a"),ord("z")+1):
        chars.append(chr(id_))

    # Adds all numbers to the list
    for number in range(10):
        chars.append(str(number))
        
    return chars



# If this module was not imported, the program will be tested.
# To perform the test, user must enter password to be found.

if __name__ == "__main__":

    import datetime
    import time
    
    # Prompts the user for a password
    pw = input("\n Type a password: ")
    print("\n")

    def testFunction(password):
        """
        This is the function that will be used to do the test.
         We can think of it as a function
         that tries to connect to a site using the
         password passed in the "password" parameter.
        """
        global pw
        if password == pw:
            return True
        else: return False

    # Gets the digits a password can have
    chars = getChars()

    t = time.process_time()

    # Get password found and number of retries
    password,attempts = findPassword(chars,testFunction,show=1000,format_=" Trying %s")

    t = datetime.timedelta(seconds=int(time.process_time()-t))
    input("\n\n Password found: {}\n Attempts: {}\n Time: {}\n".format(password,attempts,t))

