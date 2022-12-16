import string
import secrets

# This is an example on how to use strings, in this case symbols
symbols = string.punctuation

"""
Function which returns the alphabet from which our password will be generated

numbers: does the alphabet contain numbers
symbols: does the alphabet contain symbols
return: string with the whole alphabet
"""


def Create_Alphabet(numbers=False, symbols=False) -> str:
    pass


"""
Function which returns a true random character from the alphabet
Use the secrets module

alphabet: string with the alphabet for the password
return: a random character within the alphabet
"""


def Random_Char(alphabet: str) -> str:
    pass


"""
Generates the password with the specified params

size: The number of characters in the password
numbers: if numbers are enabled
symbols: if symbols are enabled
"""


def Generate_Password(size: int, numbers: bool, symbols: bool) -> str:
    pass


"""
This functions has to check if the password respects strong constraints
meaning: at least <numbers> numbers and <symbols> symbols if there are enabled.
It should also check for the existence of a lowercase and uppercase character
It is recommended to have at least 1 number and 1 symbol

password: the password to check
numbers: minimum numbers required
symbols: minimum symbols requires
return: a boolean that checks password constraints
"""


def Check_Password(password: str, numbers=1, symbols=1) -> bool:
    pass


"""
This function has to write the password to the destination file:

password: the generated password to be written
destination: the file in which to write
"""


def Write_Password(password: str, destination: str):
    pass


"""
Main function to call
It should use IO calls to handle password generation parameters 
and to write it to "password.txt"
This means it should use all functions from before

If the password fails CheckPassword, it should regenerate a new password
"""


def Generate():
    test = input("Input a message to be printed")
    print(test)
