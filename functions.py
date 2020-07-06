def inputfun():
    print ("Input your name:")
    name = input()#input("Name:")
    print(f"Hello {name}")#print("Hello," + name)

    num = int(input("Number:")) #int func

    if num > 0:#conditions
        print(f"{num} is positive")
    elif num < 0:
        print(f"{num} is negative")
    else:
        print(f"{num} is Zero")
    return None

def main():
    print("should not print while importing but print while functions is run")

if __name__ == "__main__":
    main()
