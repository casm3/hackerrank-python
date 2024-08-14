# You are given a string S.
# S contains alphanumeric characters only.

# Your task is to sort the string  in the following manner:

# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits.
# Input Format

# A single line of input contains the string S.

# Constraints
# 0 < len(S) < 1000

# Output Format

# Output the sorted string S.

# Sample Input

# Sorting1234
# Sample Output

# ginortS1324
# Enter your code here. Read input from STDIN. Print output to STDOUT
string = input()
lower_case_letters = []
upper_case_letters = []
numbers = []


for character in string:
    if character.islower():
        lower_case_letters += character
    elif character.isupper():
        upper_case_letters += character
    else:
        numbers += character

odd_numbers = sorted([number for number in numbers if int(number) % 2 != 0])
even_numbers = sorted([number for number in numbers if int(number) % 2 == 0])
numbers = odd_numbers + even_numbers

print(
    "".join(sorted(lower_case_letters)) + "".join(sorted(upper_case_letters)) + "".join(numbers)
)