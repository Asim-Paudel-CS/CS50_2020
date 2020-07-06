from functions import inputfun

class points():#customclass
    def __init__(self,x,y):#__init__calls function when trying to create point. 1st parameter represents itself in functions that call themselves
        self.x=x
        self.y=y
        self.list=[]
        self.list.append((x,y))
    def add_points(self,x,y):
        self.list.append((x,y))

def pointinp():
    p=points(5,6)
    p.add_points(2,3)
    p.add_points(10,11)
    print(p.list)
    print(p.list[2])

def decor(samplefun):#decorator
    def subdecor():
        print("func running...")
        samplefun()
        print("func done.")
    return subdecor

@decor
def HW():
    print("Hello, World!")

def exceptions():
    x = int(input("num:"))
    y = int(input("num:"))
    try:
        r = x/y
        print(f"{x}/{y} = {r}")
    except: #except ZeroDivisionError:
        print("error")

def main():
    a=28        #int
    b=1.5       #float
    c="asim"    #str
    d=True      #bool
    e=None      #nonetype

    namestr="abcde"#string
    print(namestr[2])#c

    namesarray=["asim","amol"]#list
    namesarray.append("anita")
    namesarray.sort()
    print(namesarray)
    print(namesarray[1])#anita

    coordinate=(1.0,2.0)#tuple
    print(coordinate[1])#2

    nameset = set()#set
    nameset.add("A")
    nameset.add(2)
    nameset.add(1)
    nameset.add("Amol")
    nameset.remove(2)
    print(nameset)#random arrangement
    print(f"Length of set: {len(nameset)}")#3

    for i in [0,1,2,3]:
        print(i)#0123
    for i in range(5):
        print(i)#01234
    for strlp in "asim":
        print(strlp)

    namedict={"Asim":"Good","Amol":"Nice"}#dictionary
    namedict["Anita"]="Cute"
    print(namedict["Anita"])

    peopledict=[
        {"name":"B","class":"1"},
        {"name":"A","class":"2"},
        {"name":"C","class":"3"}
    ]

    #def sortppl(dict):
    #return dict["name"]

    #peopledict.sort(key=sortppl)
    #print(peopledict)

    peopledict.sort(key=lambda sortppl:sortppl["name"])
    print(peopledict)

if __name__ == "__main__":
    main()
    pointinp()
    HW()
    inputfun()
    exceptions()
