'''
@author:    Victor Pedroso Curtarelli
@linkedin:  linkedin.com/in/victorcurtarelli/
@github:    github.com/curtarelli
@created:   July, 2020.
'''

# Lucas series function based on chosen term [initial = 0]:
def lucas(x):
    a = 2
    b = 1
    i = 2
    print(a)
    
    print(b)
    while i <= x:
        v = b + a
        a = b
        b = v
        i = i + 1
        print(v)

# Example of Lucas sequence use:
nn = 8
print('Lucas sequence example for the term number: ', nn)
print(lucas(nn))
n = int(input('\n''Input the Lucas sequence term you want: '))
print(lucas(n))

# Pell series function based on chosen term [initial = 0]:
def pell(x):
    a = 0
    b = 1
    i = 2
    print(a)
    print(b)

    while i <= x:
        v = 2 * b + a
        a = b
        b = v
        i = i + 1
        print(v)

# Example of Pell sequence use:
nn = 8
print('Pell sequence example for the term number: ', nn)
print(pell(nn))
n = int(input('\n''Input the Pell sequence term you want: '))
print(pell(n))

# Triangular series function based on chosen term [initial = 0]:
def triangular(x):
    i = 1
    print(0)

    while i <= x:
        a = int((i * (i + 1)) / 2)
        i = i + 1
        print(a)

# Example of Triangular sequence use:
nn = 8
print('Triangular sequence example for the term number: ', nn)
print(triangular(nn))
n = int(input('\n''Input the Triangular sequence term you want: '))
print(triangular(n))

# Square series function based on chosen term [initial = 1]:
def square(x):
    i = 1

    while i <= x:
        a = i ** 2
        i = i + 1
        print(a)

# Example of Square sequence use:
nn = 8
print('Square sequence example for the term number: ', nn)
print(square(nn))
n = int(input('\n''Input the Square sequence term you want: '))
print(square(n))

# Pentagonal series function based on chosen term [initial = 1]:
def pentagonal(x):
    i = 1

    while i <= x:
        a = int((3 * (i ** 2) - i) / 2)
        i = i + 1
        print(a)

# Example of Pentagonal sequence use:
nn = 8
print('Pentagonal sequence example for the term number: ', nn)
print(pentagonal(nn))
n = int(input('\n''Input the Pentagonal sequence term you want: '))
print(pentagonal(n))
