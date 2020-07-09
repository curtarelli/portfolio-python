'''
@author:    Victor Pedroso Curtarelli
@linkedin:  linkedin.com/in/victorcurtarelli/
@github:    github.com/curtarelli
@created:   July, 2020.
'''

# Test function to assess if two lines intersects each other:
def intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    s123 = (y2 - y1) * (x3 - x1) - (x2 - x1) * (y3 - y1)
    s124 = (y2 - y1) * (x4 - x1) - (x2 - x1) * (y4 - y1)

    if (s123 == 0.0) and (s124 == 0.0):

        if x1 == x2:
            result = (min(y1, y2) <= max(y3, y4)) and (min(y3, y4) <= max(y1, y2));
        else:
            result = (min(x1, x2) <= max(x3, x4)) and (min(x3, x4) <= max(x1, x2));

    else:

        s341 = (y4 - y3) * (x1 - x3) - (x4 - x3) * (y1 - y3)
        s342 = (y4 - y3) * (x2 - x3) - (x4 - x3) * (y2 - y3)

        result = ((s123 * s124) <= 0.0) and ((s341 * s342) <= 0.0);

    if result == True:
        print('The segments L1 and L2 intercept each other!''\n');
    else:
        print('The segments L1 and L2 does not intercept each other!''\n');

# Example coordinates:
x1 = 0
y1 = 0

x2 = 10
y2 = 10

x3 = 10
y3 = 0

x4 = 0
y4 = 10

# Returning the lines for this example:
print('Exampl lines:')
print('L1: [(', x1, ';', y1, ') , (', x2, ';', y2,')]')
print('L2: [(', x3, ';', y3, ') , (', x4, ';', y4,')]')

# Aplica a função para as retas deexemplo;
print(intersection(x1, y1, x2, y2, x3, y3, x4, y4))
