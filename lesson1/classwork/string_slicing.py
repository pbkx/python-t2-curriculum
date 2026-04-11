word = "pineapple"
print("The word is: " + word)

# Strings are 0 indexed (first character is index 0)
print("First letter:", word[0])
print("Second letter:", word[1])

# Negative indexing starts from the end
print("Last letter:", word[-1])
print("Second to last letter:", word[-2])

# Slicing: word[start:stop] ([start, stop))
print(word[0:4])
print(word[4:9])

# Shortcuts:
print(word[:4]) # from the beginning
print(word[4:]) # to the end