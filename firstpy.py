
import os.path

def func(name):
    print(name)

digits= [1,3]
i= 0

for i in digits:
    print("hello world")

students= {'ali', 'ahmet'}

m= 'ali'

for s in students:
    if m== s:
        print(m)

func('cagdas')

if os.path.isfile("text.txt"):
    print("text.txt file is existed\n")
    os.remove("text.txt")
    print("text.txt file is removed")
else:
    print("text.txt file is not existed\n")

try:
    mFile= open("text.txt", 'a', encoding= 'utf-8')
    mFile.write("hello world\n")
    mFile.write("my python tutorial\n")

finally: 
    mFile.close()

mFile= open("text.txt", 'r', encoding= 'utf-8')
fileStr= mFile.read(30)
print(fileStr)

print("read line\n")
mFile.seek(0)

for i in range(2):
    line= mFile.readline()
    print(line)

