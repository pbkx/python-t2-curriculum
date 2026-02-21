# A tuple is like a list, but it cannot be changed after being created (immutable).
point = (3, 5)
print(point)

print("x:", point[0])
print("y:", point[1])

red = (255, 0, 0)

print(red)
print("Length:", len(red))

# Tuples can hold mixed types too
info = ("Max", 16, "Redmond")
print(info)

# You can loop through a tuple
for item in info:
    print(item)

for i in range(len(info)):
    print(info[i])