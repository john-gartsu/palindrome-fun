'''
Problem 1:
How to check if a string is a palindrome?
This was simply for my visual processing
'''

def palindromeChecker(string):
    
    normalized_string = string.lower()
    
    for char in range(0, int(len(normalized_string)/2)):
        if normalized_string[char] != normalized_string[len(normalized_string)-char-1]:
            return f'### String: {normalized_string} is not a palindrome! ###'
    return f'### String: {normalized_string} IS A PALINDROME! ### '

word = input("Enter word to check to see if it is a palindrome: ")
print(palindromeChecker(word))
           