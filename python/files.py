f = open("top100.txt")
print(f.read())
print(f.readlines())
print(f.readlines())
f.seek(0)
print(f.readlines())

f.seek(0)
for line in f:
    print(line.strip())
f.close()

f = open("text.txt", "wr")
f.write("Test line.")
print(f.read())
f.close()

f = open("text.txt", "wr")
f.write("Test line number two.")
print(f.read())
f.close()

f = open("text.txt", "ar")
f.write("Test line number three.")
print(f.read())
f.close()

print(f.name())
print(f.closed())
print(f.mode())

with open("rockyou.txt", encoding="latin-1") as f:
    for line in f:
        pass