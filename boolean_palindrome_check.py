'''
Problem 1:
How to check if a string is a palindrome?
'''

def palindromeChecker(string):
    
    normalized_string = string.lower()
    
    for char in range(0, int(len(normalized_string)/2)):
        if normalized_string[char] != normalized_string[len(normalized_string)-char-1]:
            return False
    return True

'''
ONLY FOR LOCAL TESTING
Please uncomment below lines to run locally
'''
# word = input("Enter word to check to see if it is a palindrome: ")
# print(palindromeChecker(word))
