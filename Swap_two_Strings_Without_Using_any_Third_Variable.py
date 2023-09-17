'''Swap two Strings Without Using any Third Variable
 Input: a = "Hello", b = "World".
Output: Strings after swap: a = World and b = Hello'''

a = "Hello"
b = "World"
print("Strings before swap: a =", a, "and b =", b)
a = a + b
b = a[:len(a) - len(b)]
a = a[len(b):]
print("Strings after swap: a =", a, "and b =", b)