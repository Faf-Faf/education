"""
Education project.

by Faf-Faf
welma20038@gmail.com

https://github.com/Faf-Faf/education.git

"""

def hello(nm_string):
    """
    Takes a name and prints it on the console.
    """
    print("Hello", nm_string)



def get_name(prompt):
    """
    Gets a name from the console.

    Get a name from the console input.
    If it's doesn't pass check, try again.

    Returns a valid name or an empty string
    """
    wrong_name = True
    name = ""
    while wrong_name:
        name = input(prompt)
        if len(name) == 0 or name.isdecimal():
            wrong_name = True
        else:
            wrong_name = False

    return name



name = get_name("Enter your name: ")

hello(name)

num = input("Enter a number: ")
if num.isdecimal():
    num = float(num)
    print("Square of", num, "is", num**2)
    print("Square root of", num, "is", num**0.5)
else:
    print("Invalid number", num)
