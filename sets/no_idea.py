# There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. 
# You like all the integers in set A and dislike all the integers in set B. 
# Your initial happiness is 0. 
# For each  integer in the array, if i ∈ A, you add 1 to your happiness. 
# If i ∈ B, you add -1 to your happiness. 
# Otherwise, your happiness does not change. Output your final happiness at the end.

# Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

# Constraints
# 1 <= n <= 10^5
# 1 <= m <= 10^5
# 1 <= Any integer in the input <= 10^9

# Input Format

# The first line contains integers n and m separated by a space.
# The second line contains n integers, the elements of the array.
# The third and fourth lines contain m integers, A and B, respectively.

# Output Format

# Output a single integer, your total happiness.

# Sample Input

# 3 2
# 1 5 3
# 3 1
# 5 7
# Sample Output

# 1
# Explanation

# You gain 1 unit of happiness for elements 3 and 1 in set A. 
# You lose 1 unit for 5 in set B. 
# The element 7 in set  does not exist in the array so it is not included in the calculation.

# Hence, the total happiness is 2 - 1 = 1.
# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
array_elements = list(map(int, input().split()))
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

happiness_lvl = 0

for element in array_elements:
    if element in a_set:
        happiness_lvl += 1
    elif element in b_set:
        happiness_lvl -= 1
        
print(happiness_lvl)
