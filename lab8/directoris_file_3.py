import os
def exist_or_not(path):

    if os.path.exists(path):
        print("Exists")
        f=os.path.basename(path)
        d=os.path.dirname(path)
        print(f"Filename: {f}")
        print(f"Directory: {d}")

    else:
        print(f"Doesnt exist")
        return
    
    
n = input()
exist_or_not(n)
