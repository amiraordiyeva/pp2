new = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2]
file = open('fail_new.txt','w')

for item in new:
            file.write(str(item) + '\n')
file.close()

print(f"List was added in fail.")
