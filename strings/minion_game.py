# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

# For Example:
# String S = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

# For better understanding, see the image below:
# Your task is to determine the winner of the game and their score.

# Function Description

# Complete the minion_game in the editor below.

# minion_game has the following parameters:

# string string: the string to analyze
# Prints

# string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
# Input Format

# A single line of input containing the string S.
# Note: The string  will contain only uppercase letters: [A - Z].

# Constraints
# 0 < len(S) <= 10^6

# Sample Input

# BANANA
# Sample Output

# Stuart 12
# Note :
# Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.

def minion_game(string):
    vowels = {"A", "E", "I", "O", "U"}
    consonants = {"B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"}
    kevin_points = 0
    stuart_points = 0
    for score_maker in range(len(string)):
        if string[score_maker] in vowels:
            kevin_points += len(string) - score_maker
        elif string[score_maker] in consonants:
            stuart_points += len(string) - score_maker

    if kevin_points > stuart_points:
        print("Kevin " + str(kevin_points))
    elif kevin_points < stuart_points:
        print("Stuart " + str(stuart_points))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)