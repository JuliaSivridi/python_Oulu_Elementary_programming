def prompt_input(prompt, err):
    """
    Prompts the user for an integer using the prompt parameter.
    If an invalid input is given, an error message is shown using
    the error message parameter. A valid input is returned as an
    integer. Only accepts integers that are bigger than 1.
    """
    while True: 
        try:
            num = int(input(prompt))
        except ValueError:
            print(err)
        else:
            if num <= 1:
                print(err)
            else:
                return num

def check_prime(num):
    """
    Checks whether an integer is a prime number. Returns False
    if the number isn't a prime; if it is a prime, returns True
    """
    for i in range(2, (num//2)+1):
        if (num % i) == 0:
            return False
    else:
        return True

number = prompt_input(
    "Give an integer that's bigger than 1: ",
    "You had one job"
)
if check_prime(number):
    print("This is a prime")
else:
    print("This is not a prime")
