'''
@author:    Victor Pedroso Curtarelli
@linkedin:  linkedin.com/in/victorcurtarelli/
@github:    github.com/curtarelli
@created:   July, 2020.
'''
# Function to test if a word is a palindrome:
def palindrome(x):
    y = x

    x = x.lower()

    x = x.replace(" ", "")

    if x == x[::-1]:
        print('The word ' + y + ' is a palindrome')
    else:
        print('The word ' + y + ' is not a palindrome')

# Function to test if a phrase is a palindrome:
def palindrome_phrase(x):
    cr = (" ", ",", ".", "!", "-")

    y = x

    x = x.lower()

    for c in cr:
        x = x.replace(c, "")

    if x == x[::-1]:
        print('Phrase: ' + y + ', is a palindrome')
    else:
        print('Phrase: ' + y + ', is not a palindrome')

