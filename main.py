from Generator import *
from Test import testeur
import string

# Use this file to call functions and test

print("===== Tests Alphabet =====")
testeur("Alphabet", Create_Alphabet(), string.ascii_letters)
testeur("Alphabet_numbers", Create_Alphabet(
    True), string.ascii_letters + string.digits)
testeur("Alphabet_symbols", Create_Alphabet(symbols=True),
        string.ascii_letters + string.punctuation)
testeur("Alphabet_numbers_symbols", Create_Alphabet(True, True),
        string.ascii_letters + string.digits + string.punctuation)
print()

# Tests for Random Char
print("===== Tests Random Char =====")
alphabet = Create_Alphabet(True, True)
chosen = Random_Char(alphabet)
testeur("Random_Char1", len(chosen), 1)
testeur("Random_Char2", True, chosen in alphabet)
print()

# Tests for checkPassword
print("===== Tests CheckPassword =====")
testeur("CheckPassword_OnlyLower", Check_Password("aaaaaa"), False)
testeur("CheckPassword_OnlyUpper", Check_Password("AAAAAA"), False)
testeur("CheckPassword_OnlyNumbers", Check_Password("11111"), False)
testeur("CheckPassword_OnlySymbols", Check_Password("[[[[[["), False)
testeur("CheckPassword_NoNumbers", Check_Password("aaaAAA[[["), False)
testeur("CheckPassword_NoSymbols", Check_Password("aaaAAAA1111"), False)
testeur("CheckPassword", Check_Password("aA1["), True)
