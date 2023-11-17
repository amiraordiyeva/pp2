import os
def d(path):
    every = os.listdir(path)
    directories = [item for item in every if os.path.isdir(os.path.join(path, item))]
    print(directories)
def f(path):
    every = os.listdir(path)
    files = [item for item in every if os.path.isfile(os.path.join(path, item))]
    print(files)
def all(path):
    every = os.listdir(path)
    print(every)
specified_path = input()
d(specified_path)
f(specified_path)
all(specified_path)




