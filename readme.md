# Palindrome Checker
Problem 1:
* How to check if a string is a palindrome?

###### Please note: 
* palindrome_check.py was simply used a visual aid for problem solving
* boolean_palindrome_check.py is ran in the second test, palindrome_intention_count.py. 
* To run boolean_palindrome_check.py localy, PLEASE ensure to commit out the word input section at the bottom of the script.

###### My Steps:
1. Lowercase the string so all characters so the are all the same case.
2. Using a for loop, I iterate over the first half of the string.
3. Then compare first half of string characters to other half.
4. If they dont match, return string is not a palindrome.
5. If they match, return string is A palindrome.

# Least Intention Palindrome Finder 
Problem 2:
* How to find the least amount of intention of characters to make a giving 
string into a palindrome? 
(e.g. if input is "abb", then the answer is 1, making it into "abba")

Problem Rephrased into my words:
* With a string input,  what are the least amount of characters to turn it into a palindrome... What are the least number of character to make the first half to look like th back half

###### My Steps:
1.  Imported Palindrome Checker function from problem 1, and added normalize string to all lower case given an input may be uppercase.

2. Initialized an empty character count to 0 to count number required to make palidrome.

3. Looped through inputted string to return characters needed to make palindrome.

4. Using the palindromeChecker function, to count to see amount of characters needed to make palindrome.

5. Added characters need to character count to get total count of characters needed to make a palindrome.

6. Tested against abb, ab, and han.

7. Documented solution.