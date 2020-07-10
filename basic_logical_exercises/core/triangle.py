'''
@author:    Victor Pedroso Curtarelli
@linkedin:  linkedin.com/in/victorcurtarelli/
@github:    github.com/curtarelli
@created:   July, 2020.
'''
# Function that returns if tree measurements can compose a trinagle form, giving the type of the triangle;
def triangle():
    a = float(input('\n''First side: '))                # Input of Side 1;
    b = float(input('\n''Second side: '))               # Input of Side 2;
    c = float(input('\n''Third side: '))                # Input of Side 3;
	
    if abs(b - c) < a and a < (b + c) and \
        abs(a - c) < b and b < (a + c) and \
        abs(a - b) < c and c < (a + b):
		
        list_i = [a, b, c]
        list_i.sort(reverse = True)
        max_1 = list_i[0] ** 2
        max_2 = list_i[1] ** 2
        max_3 = list_i[2] ** 2
        
        # If triangle test = true:
        if a == b and b == c:                   # Equilateral triangle test;
            print('\n''Equilateral triangle')

        elif max_2 + max_3 == max_1:            # If not, rectangle triangle test;
            print('\n''Rectangle triangle')

        elif a != b and b != c and a != c:      # If not, scalene triangle test;
            print('\n''Scalene triangle')

        else:
            print('\n''Isoceles triangle')      # If does not attend any test, it is classified as isoceles triangle;

	# If triangle test = false:
    else:                                                       
        print('\n''These measures does not match a triangle form')           	# Returns the error message;
        triangle()