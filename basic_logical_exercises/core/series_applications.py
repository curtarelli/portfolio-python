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

# Triangular series function based on chosen term [initial = 0]:
def triangular(x):
    i = 1
    print(0)

    while i <= x:
        a = int((i * (i + 1)) / 2)
        i = i + 1
        print(a)

# Square series function based on chosen term [initial = 1]:
def square(x):
    i = 1

    while i <= x:
        a = i ** 2
        i = i + 1
        print(a)

# Pentagonal series function based on chosen term [initial = 1]:
def pentagonal(x):
    i = 1

    while i <= x:
        a = int((3 * (i ** 2) - i) / 2)
        i = i + 1
        print(a)

