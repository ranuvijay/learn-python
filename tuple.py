# collection of items indexed, ordered and immutable

first_tuple = ("a", "b", "c")
print(tuple[1])
print(tuple)

# access tuple
x, y, z = first_tuple
print(y, z, x)
print(x, y)


# error accessing partial
# x, y = first_tuple
# print(x, y)


tuple_constructor = tuple(("l", "m", "n"))
print(tuple_constructor)


# difference withour ","
# t1 splits into  individual  character not t2 due to  , and due to tuple property of iterate
t1 = tuple(("ranu"))
print("t1", t1)

t2 = tuple(("ranu",))
print("t2", (t2))


# single data

# this is string type
single_item = "item"
print(type(single_item))


# this is tuple type -  add a , at the end
single_item = ("item",)
print(type(single_item))