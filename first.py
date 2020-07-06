a=28        #int
b=1.5       #float
c="asim"    #str
d=True      #bool
e=None      #nonetype

print ("Input your name:")
name = input()#input("Name:")
print(f"Hello {name}")#print("Hello," + name)
num = int(input("Number:"))

if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is Zero")
