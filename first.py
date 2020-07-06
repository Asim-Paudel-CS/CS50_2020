from functions import inputfun

inputfun()

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

if __name__ == "__main__":
    main()
