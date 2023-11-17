import string
import os
a = "letters"
if not os.path.exists(a):
    os.makedirs(a)
for letter in string.ascii_uppercase:
    filepath=os.path.join(a, letter + ".txt")
    with open(filepath, "w") as f:
        f.write(letter)
