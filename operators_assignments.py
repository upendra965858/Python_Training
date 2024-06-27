# What will be the output of following statements
print({1, 2, 3, 5} - {3, 4, 7, 8})
# Out put is - {1, 2, 5}
print({1, 2, 3, 5} + {3, 4, 7, 8})
# Out put is - TypeError: unsupported operand type(s) for +: 'set' and 'set'

# What will be the output of following programs
print('Hi ' + 'Anil')
# Out put is - Hi Anil
print([1, 2] + [3, 4])
# Out put is - [1, 2, 3, 4]
print('Hi' + [1, 2])
# Out put is - TypeError: can only concatenate str (not "list") to str

# What will be the output of following programs
print((1, 2, 3) * 4)
# Out put is - (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
print(8 // 3)
# Out put is - 2
print(21 % 6)
# Out put is - 3

# What will be the output of following programs
a = 7
a /= 2
print(a)
# Out put is - 3.5
b = 5
print(b > 5 and b < 10)  # Also write the short form for this expression
# Out put is - False
# Short form "print(5<b<10)"
print(5 < b < 10)
# Out put is - False

# Write the output of following programs
print(4 and 6)
# Out put is - 6
print(1 or 5)
# Out put is - 1
print(not 7)
# Out put is - False

# what is the output of following programs
print(2 not in [3, 4, 5, 2, 9])
# Out put is - False
print([1, 2, 5, (1, 2)] in ['hi', 3, 4, 5, 2, 9, [1, 2, 5, (1, 2)]])
# Out put is - True

# what is the output of following programs
a = 400.30123
b = 400.30123
print(a is b)
# Out put is - True

i = 23
j = 23
print(i is j)
# Out put is - True
print(i == j)
# Out put is - True

a1 = 999
b1 = 999
print(a1 is b1)
# Out put is - True
print(a1 == b1)
# Out put is - True

y = 4
z = -4
print(y == z)
# Out put is - False

s1 = 4096 * 'a'
s2 = 4096 * 'a'
print(s1 is s2)
# Out put is - True

# write the output of following programs
a = 2
b = 11
print(a & b)
# Out put is - 2
print(a | b)
# Out put is - 11
print(a ^ b)
# Out put is - 9
print(~b)
# Out put is - -12
print(a << 3)
# Out put is - 16
print(b >> 2)
# Out put is - 2

# write the output of following programs
print(+-4)
# Out put is -  -4
print(--4)
# Out put is - 4
a = [1, 2, 3]
print(2 * a[1] << 2 > 8 and 9)
# Out put is - 9
print(2 * 3 - 3 ** 2 ** 1 & 5 // 2 + (4 + 2) or 5)
# Out put is - 8