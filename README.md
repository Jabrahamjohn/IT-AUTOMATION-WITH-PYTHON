Study Guide: Conditionals
This study guide provides a quick-reference summary of what you learned in this lesson and serves as a guide for the upcoming practice quiz.  

In the Conditionals segment, you learned about the built-in Python operators used for comparing values and the logical operators for making complex comparisons. You also learned how to use operators in if-else-elif blocks. 

 

Knowledge
Comparison operators with numerical values
Comparison expressions return a Boolean result (True or False). 

x == y        If x is equal to y, return True. Else, return False.

x != y         If x is not equal to y, return True. Else, return False.

x < y          If x is less than y, return True. Else, return False.

x <= y        If x is less than or equal to y, return True. Else, return False.

x > y          If x is greater than y, return True. Else, return False.

x >= y        If x is greater or equal to y, return True. Else, return False.

Comparison operators with strings
Comparison expressions with strings also return a Boolean result (True or False).

"x" == "y"  If the words are the same, return True. Else, return False.

"x" != "y"   If the words are not the same, return True. Else, return False.

When used with strings, the following comparison expressions will alphabetize the strings.

"x" < "y"   	If string "x"  has a smaller Unicode value than string "y", return True.  Else, return False.

"x" <= "y" 	If the Unicode value for string "x" is smaller than or equal to the Unicode value of string "y", return True. Else, return False.

"x" > "y"    	If string "x" has a larger Unicode value than string "y", return True. Else, return False.

"x" >= "y"  	If the Unicode value for string "x" is greater than or equal to the Unicode value of string "y", return True. Else, return False.


Unicode values for the alphabet

Image containing the unicode value of each letter of the alphabet
 The Unicode numbering for the alphabet starts at 65 for capital letter A and runs to 90 for capital letter Z. Then, the lowercase alphabet values start at 97 for lowercase a and run to 122 for lowercase z. Using these Unicode numbers, capital A's code is less than the codes of all other letters, which Python interprets as the beginning of the alphabet. Lowercase z's code is greater than the codes of all other letters, which Python interprets as the ultimate end of the English alphabet.


Logical operators
Logical operators are used to combine comparison expressions and also return Boolean results (True or False).

comparison1 and comparison2 

Returns a True result if both comparison1 and comparison2 are true. 

If they are not both true, return False.

comparison1 or comparison2 

Returns a True result if either comparison1 and/or comparison2 are True. 

If neither comparison is true, return False.

not comparison1

Returns the inverse Boolean value of the comparison. 

Returns a True result if comparison1 is false. 

If comparison1 is true, then returns False.
Syntax of an if-elif-else block
if condition1:
    action1
elif condition2:
    action2
else:
    action3
If condition1 is True:

Then perform action1 and exit if-elif-else block

If condition2 is True:

Then perform action2 and exit if-elif-else block

If neither condition1 nor condition2 are True:

Then perform action3 and exit if-elif-else block

 

Coding skills
Skill Group 1

Use a comparison operator with numbers

Use a comparison operator to alphabetize strings

print("tall" < "short")  # Should print False
Skill Group 2

Use a function with the def() keyword

Pass a parameter to the function

Use an if-elif-else statement

Assign strings to variables 

Use conditional operators

Return a value

- Skill Group 2

Use a function with the def() keyword

Pass a parameter to the function

Use an if-elif-else statement

Assign strings to variables 

Use conditional operators

Return a value

Skill Group 3

Use an if-elif-else statement with:

comparison operators

logical operators

Skill Group 4

Use an if statement to calculate a return value

Use conditional operators

Recall the arithmetic operators // and %
