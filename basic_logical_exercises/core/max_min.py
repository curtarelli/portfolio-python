'''
@author:    Victor Pedroso Curtarelli
@linkedin:  linkedin.com/in/victorcurtarelli/
@github:    github.com/curtarelli
@created:   July, 2020.
'''
#   Function to assess the maximum and minimum values from a list:
def max_min(list_i):
    print('Maximum:', max(list_i))
    print('Minimum', min(list_i))
    
    return max(list_i), min(list_i)

#   Function to assess the n-st value from a list. For the highest use 1, 2..., for the
#   lowest use -1, -2...:
def n_value(list_i, position):
    if position > 0:                # Test normalization for highest values;
        position = position - 1
    
    elif position < 0:              # Test for lowest values;
        position = position
    
    else:                           # Error value and message;
        print('Error in the chosen position')
        position = int(input('Insert new position: '))
        
    list_i.sort(reverse = True)     # Descendent sorting;
    
    print('N-st value: ', list_i[position])
    return list_i[position]

