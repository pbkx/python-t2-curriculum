# Problem 1
# Ask the user for a word.
# Print how many vowels it has (a, e, i, o, u).

word = input("Please input a word:")
vowel = "aeiou"
c = 0
for ch in word:
    if ch in vowel:
        c += 1
print(c)

# Problem 2
# Ask the user for a word.
# Print "Palindrome" if it reads the same backwards, otherwise print "Not palindrome".

word = input("Please input a word:")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

# Problem 3
# Ask the user for a word.
# Build a new string that contains ONLY the letters at odd indexes (1, 3, 5, ...).

res = ""
word = input("Please input a word:")
for i in range(len(word)):
    if i % 2 == 1:
        res += word[i]
print(res)

# Problem 4
# Ask the user for two words.
# Print the two words combined with a dash in the middle. Example: "cat-dog".



# Problem 5
# Ask the user for a phrase.
# Build a new string that removes all spaces.
