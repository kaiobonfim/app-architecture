a=1
while a < 5:
    a += 1
    print(a)

for i in [0, 1, 2, 3, 4]:
    print(i+6)

for i in range(5):
    print(i+6)

for i in range(3):
    for j in range(3):
        print(i, j)

for i in range(5):
    if i == 2:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)

for c in "string":
    print(c)

for k, v in {"a":1, "b":2, "c":3}.items():
    print(k, v)