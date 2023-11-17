import os
path = input()
try:
    os.remove(path)
    print(f"'{path}' deleted.")
except OSError as e:
    print(f"Error: {e}")





