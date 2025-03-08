#/ Arithmetic operators
#/ Addition (+)
num1 = 5
num2 = 2
result = num1 + num2
print (result)
#/ Subtraction (-)
num1 = 10
num2 = 4
result = num1 - num2 
print (result)
#/ Multiplication (*)
num1 = 8
num2 = 2
result = num1 * num2
print (result)
#/ Division /
num1 = 10
num2 = 2
result = num1 / num2
print(result)
#/ Floor Division (//)
num1 = 10
num2 = 3
result = num1 // num2
print (result)
#/ Modulus (%)
num1 = 7
num2 = 5
result = num1 % num2
print (result)
#/ Exponentation (**)
base = 5
exponent = 2
result = base ** exponent
print (result)

#/ Assigment Operators
#/ Assign (=)
x = 7
print ("x =", x)
y = 3
print ("y =" , y)
#/ Add and Assign (+=)
a = 3
a += 2
print (a)
#/ Subtract and assign (-=)
b = 7
b -= 3
print (b)
#/ Multiply and Assign (*=)
c = 8
c *= 3
print (c)
#/ Divide and Assign (/=)
d = 20
d /= 5
print (d)
#/Floor divide and Assign (//=)
e = 12
e //= 4
print (e)
#/ Modulus and Assign (%=)
f = 15
f %= 5
print (f)
#/ Exponentiate and Assign (**=)
g = 3
g **= 2
print (g)

#/ Comparison/Relational operators 
#/ Equal to (==)
x = 7
y = 7
if x == y:
    print ("x is equal to y")
else :
    print ("x is not equal to y")
#/ Not Equal To (!=)
a = "anusha"
b = "sumbul"
if a != y :
    print ("a is not equal to b")
else :
    print ("a is equal to b")
#/ Greater than (>)
x = 15
y = 3
if x > y:
    print ("x is greater than y")
else :
    print ("x is not greater than y")
#/ Less than (<)
a = 10
b = 20
if a < b :
    print ("a is less than b")
else :
    print ("a is not less than b")
#/ Greater than OR Equal to (>=)
x = 4
y = 4
if x >= y :
    print ("x is greater than or equal to y")
else :
    print ("x is not greater than or equal to y")
#/ Less than OR equal to (<=)
x = 9
y = 9
if x <= y :
    print ("x is less than or equal to y")
else :
    print ("x is not less than or eqaul to y")

#/ Bitwise Operatores 
#/ And (&)

a = 5  #  Binary:  0101
b = 3  #  Binary:  0011
result = a & b  #  Result: 0001 (1 in decimal)
print(result)  # Output: 1

#/ Or (|)

result = a | b  # Result: 0111 (7 in decimal)
print(result)  # Output: 7

#/ Xor (^)

result = a ^ b  # Result: 0110 (6 in decimal)
print(result)  # Output: 6


#/ Not (~)

result = ~a  # -6 (because Python uses two’s complement)
print(result)  # Output: -6


#/ Left Shift (<<)

result = a << 1 # Binary: 0010 (2 in decimal)
print(result)  # Output: 10


#/ Right Shift (>>)

result = a >> 1  # Binary: 0010 (2 in decimal)
print(result)  # Output: 2

