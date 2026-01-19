# Problem 1
# Ask the user for a word.
# Print the first 3 letters, and then print the last 3 letters.

word = input("Enter a word: ")
print("First 3:", word[:3])
print("Last 3:", word[-3:])

# Problem 2
# Ask the user for a sentence.
# Print it in all caps, then print it in all lowercase.

sentence = input("Enter a sentence: ")
print(sentence.upper())
print(sentence.lower())

# Problem 3
# Ask the user for a first name and a last name.
# Print their initials (first letter of first name + first letter of last name).

first = input("First name: ")
last = input("Last name: ")
print("Initials:", first[0] + last[0])

# Problem 4
# Ask the user for a sentence.
# Replace all spaces with underscores and print the result.

sentence = input("Enter a sentence: ")
print(sentence.replace(" ", "_"))

# Problem 5
# Ask the user for a phrase.
# Print "Contains python" if the word "python" appears anywhere (case-insensitive).
# Otherwise print "No python found".

phrase = input("Enter a phrase: ")
if "python" in phrase.lower():
    print("Contains python")
else:
    print("No python found")