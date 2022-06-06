# Problem 2: least intention checker

from boolean_palindrome_check import palindromeChecker

def leastIntentionChecker(string):
    normalized_string = string.lower()
    char_count = 0
    for char_needed in range(len(normalized_string)):
        if palindromeChecker(normalized_string[:len(normalized_string) - char_needed]) or palindromeChecker(normalized_string[char_needed:]):
            char_count += char_needed
            return f'### {char_count} characters are needed to make a palindrome...'
        
input_string = input("Enter a string to check to find the least amount of characters to make a palindrome: ")
print(leastIntentionChecker(input_string))
