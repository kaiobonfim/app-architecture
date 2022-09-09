test = input()
print(test)

test2 = input("Enter the IP address: ")
print(test2)

while True:
    test = input("Enter the IP add: ")
    print(">>> {}".format(test))
    if test == "exit":
        break
    else:
        print("Exploiting...")
