# Task 1: Input name, address, hobby and display it

def main():
    name = input("Enter name: ")
    address = input("Enter address: ")
    hobby = input("Enter hobby: ") 

    print("USER DETAILS:")
    print("=============")
    print("Name:\t\t{}".format(name))
    print("Address:\t{}".format(address))
    print("Hobby:\t\t{}".format(hobby))


if __name__ == "__main__":
    try:
        main()
    except:
        pass
    
