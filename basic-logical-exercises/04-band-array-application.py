'''
@author:    Victor Pedroso Curtarelli
@linkedin:  linkedin.com/in/victorcurtarelli/
@github:    github.com/curtarelli
@created:   July, 2020.
'''
# Importing the packages needed:
import numpy as np
import matplotlib.pyplot as plt

# Function to create 2 random bands [(n)x(m) - (x)-bits] sum it and correct it:
def random_matrix_sum(bits, lines, columns):
    # Creating 2 random (n)x(m) (x)-bit matrix (bands):
    dn = (2 ** bits) - 1
    
    b1 = np.random.random_integers(0, dn, size = (lines, columns))
    b2 = np.random.random_integers(0, dn, size = (lines, columns))
    
    # Calculating the sum of the 2 bands:
    b3 = b1 + b2
    
    # Correcting the result matrix for values higher than 255:
    b3[b3 > dn] = dn
    
    # Matix display:
    print('\n''Band 1 [' + str(lines) + 'x' + str(columns) + ' - ' + str(bits) + '-bits]:''\n\n', b1,
          '\n\n''Band 2 [' + str(lines) + 'x' + str(columns) + ' - ' + str(bits) + '-bits]:''\n\n', b2,
          '\n\n''Band 3 = Band 1 + Band 2 (corrected) [' + str(lines) + 'x' + str(columns) + ' - ' + str(bits) + '-bits]:''\n\n', b3)
    
    # Configuring the plot:
    pb3 = plt.imshow(b3, vmax = dn, cmap = 'gray')
    plt.xlabel('Columns -->')
    plt.ylabel('<-- Lines')
    plt.title('Band 3 = Band 1 + Band 2 (corrected) [' + str(lines) + 'x' + str(columns) + ' - ' + str(bits) + '-bits]:')
    cbar = plt.colorbar()
    cbar.set_label('Digital Number (DN)')
    
    # Ploting the result:
    plt.show()

# Apliyng the function:
random_matrix_sum(8, 50, 50)
