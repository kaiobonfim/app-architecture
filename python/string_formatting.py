string1 = "First string"
string2 = 'Another string'

print(string1)
print(string2)

string3 = """A
long
string"""

print(string3)

string4 = "This is a 'string'"
string5 = 'This is a "string"'
string6 = "This is a \"string\""
string7 = 'This is a \'string\''

print(string4)
print(string5)
print(string6)
print(string7)

string8 = "New\nline"
print(string8)

string9 = "\\ \x41\x42\x43"
print(string9)

string10 = "ABC" * 3
print(string10)
print(len(string10))

print("ABC" in string10)
print("ABCD" in string10)
print(string10.startswith("A"))
print(string10.startswith("B"))

string11 = "One more string"
print(string11.index("string"))
print(string11.upper())
print(string11.lower())

space_string = "   Spaces?   "
print(space_string)
print(space_string.strip())
print(space_string.replace("?", "!").strip())
print(space_string.split())

string12 = "Regular string"
print("String 12 is " + str(len(string12))+ " characters long")
print("String 12 is {} characters long".format(len(string12)))
print("{} {} {}".format(len(string12), 5.0, 0xf))
print("{0} {2} {1}".format(len(string12), 5.0, 0xf))
print("{length}".format(length=len(string12)))
length = len(string12)
print(f"String 12 is {length} characters long")
print("String 12 is {length:.1f} characters long".format(length=len(string12)))
print("String 12 is {length:.2f} characters long".format(length=len(string12)))
print("String 12 is {length:x} characters long".format(length=len(string12)))
print("String 12 is {length:b} characters long".format(length=len(string12)))
print("String 12 is %d characters long" % len(string12))
print("String 12 is %.2f characters long" % len(string12))
print("String 12 is %x characters long" % len(string12))