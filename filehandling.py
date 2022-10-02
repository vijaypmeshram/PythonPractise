v = open("redme.txt")
"""we pointer to denote/direct the file ehich open in here"""
#content = v.read()
#when u v.read() function used then file pointer gets empty, it give nothing. so to get file line by line in foor loop
#print(content)

#readline() function used to get line one by one
print(v.readline())

print(v.readlines())

#to use line in file for is used which direct to pointer value/variable to give output
for line in v:
    print(line, end="")

v.close()

#below lines create file with name vjy.txt and  write passing argument
#f=open("vjy.txt", "w")

#below line add content in existing content without arase it
#f=open("vjy.txt", "a")
#f.write("how are you today\n")
#print(f)

#handle read and write mode
f=open("vjy.txt","r+")
print(f.read())
f.write("i m fine\n")

f.close()

a=20