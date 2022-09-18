mStr= "hello world"
print("length of mStr", len(mStr))
print("\npos of world in mStr", mStr.index("world"))

worldStr= mStr[mStr.index("world"):]
print(worldStr)

mStr= "welcome to the jungle"
x= mStr.split()
print(x)
print(x[1])