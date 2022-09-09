tuple1 = ("item1", "item2", "item3")
print(tuple1)
print(type(tuple1))

tuple2 = (1, 2, 3)
print(tuple2)
print(type(tuple2))

tuple3 = ("Item", ) * 4
print(tuple3)
print(type(tuple3))

mixed_tuple = ("A", 1, ("B", 2))
print(mixed_tuple)
print(type(mixed_tuple))

tuple4 = tuple1 + tuple2
print(tuple4)
print(type(tuple4))

item1, item2, item3 = tuple1
print(item1)
print(item2)
print(item3)

print('item3' in tuple1)
print("item4" in tuple1)
print(tuple1.index("item1"))
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(len(tuple1))
print(tuple1[-1])
print(tuple1[-2])
print(tuple1[-3])
print(tuple1[0:2])
print(tuple1[:2])

string1 = "I am a string"
print(string1[:4])
print(string1[-1])