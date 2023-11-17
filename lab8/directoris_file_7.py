with open('first.txt','r') as first, open('second.txt','a') as second: 
	for line in first: 
			second.write(line)
print("first text was copied into second text")