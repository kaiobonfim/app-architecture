try:
    f = open("qwerty")
except:
    print("This file does not exist!")

try:
    f = open("qwerty")
except FileNotFoundError:
    print("The file has not been found")
except Exception as e:
    print(e)
finally:
    print("This message")

n = 1
if n == 0:
    raise Exception("n can't be 0!")
print(1/n)

c = 1
if type(c) is not int:
    raise Exception("c must be an int!")
print(1/c)

d = 1
assert (d != 0)
print(1/d)