'''Swap two numbers without using a temporary variable
 Input:integer a = "10", b = "50".
Output: Strings after swap: a = 50 and b = 10'''
x = 10
y = 5
print("Strings before swap: a=", x, " and b=", y)
x ^= y
y ^= x
x ^= y
print("Strings after swap: a=", x, " and b=", y)