from fractions import Fraction

f = Fraction(3, 4)
print("Let's print \"f\". F is 3/4")
print(f)
print(f + 1 + 1.5)
print(f + 1 + Fraction(2/4))

print("\n")
print("Let's look at Complex Numbers now")
print("a = 2 +3j")
a = 2 + 3j
print(a)
print(type(a))
a1 = complex(2, 3)
print(a1)

print("\n")
b = 3 + 3j
print(b)
print("a + b =")
print(a + b)

c = input("C input: ")
print(int(c) + 1)

try:
    d = float(input('Enter a number: '))
except ValueError:
    print('You entered an invalid number')

f = int(input('Input an integer'))

print(f + 2)

g = Fraction(input('Enter a fraction: '))
print(g + 3)

h = complex(input('Enter a complex number: '))

def is_factor(i, j):
    if j % i == 0:
        return True
    else:
        return False

is_factor(4,1024)