N=int(input())

lines=[]
for i in range(N):
	lines.insert(i,input())	

ans=[]

for line in lines:
	words=line.split()
	newline=[]
	for word in words:
		if word[-1]=="'" or word[-1]==":" or word[-1]=="," or word[-1]=="." or word[-1]==";":
			word=word[:-1]
		if len(word)>1:
			if word[-2]=="'":
				word=word[:-2]+word[-1]
		newline.insert(0,word)
	ans.insert(0,newline)

for line in ans:
	for word in line:
		print(word,end=" ")
	print("")
