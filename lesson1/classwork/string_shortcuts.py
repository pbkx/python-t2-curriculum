first = "Sova"
last = "Coding"

# String concatenation
full = first + " " + last
print(full)

# Repeat a string
print("ha" * 3)  # 'hahaha'

# 'in' check if something appears inside a string.
sentence = "I like python"
print("python" in sentence)

if "java" in sentence:
    print("Java is in the sentence.")

print("Py\"th\'on\\")  # In order to use ' or " inside a string, you must use the escape character \
print("Java\nPython")  # The '\n' escape character is a line break.

print("Age is " + str(16))