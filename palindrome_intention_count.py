'''
Problem 2:
How to find the least amount of intention of characters to make a giving 
string into a palindrome? 
(e.g. if input is "abb", then the answer is 1, making it into "abba")

Rephrase in my words:
With a string input, 
what are the least amount of characters to turn it into a palindrome...
What are the least number of character to make the first half to look like th back half
'''
# import math
from boolean_palindrome_check import palindromeChecker

def leastIntentionChecker(string):
    '''
    normalize string to all lower case given an input may be uppercase
    '''
    normalized_string = string.lower()
    # init empty character count
    char_count = 0
    # loop through the string input
    for char_needed in range(len(normalized_string)):
        # if string input
        if palindromeChecker(normalized_string[:len(normalized_string) - char_needed]) or palindromeChecker(normalized_string[char_needed:]):
            char_count += char_needed
            # return char_count 
            return f'### {char_count} characters are needed to make a palindrome...'
        
input_string = input("Enter a string to check to find the least amount of characters to make a palindrome: ")
print(leastIntentionChecker(input_string))
