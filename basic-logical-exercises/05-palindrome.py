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

# Exameple:
aa = 'Asa'
print('Example for: ' + aa)
palindrome(aa)

a = str(input('\n''Insira uma palavra iniciando com letra maiúscula e sem acentuação: '))   # Pergunta ao usuário uma palavra;
palindromo(a)                                                         # Aplica a função palindromo na palavra escolhida;

def frase_palindromo(x):        # Função que testa se frase é palindromo;
    cr = (" ", ",", ".", "!", "-")

    y = x                       # Cópia da frase original;

    x = x.lower()

    for c in cr:
        x = x.replace(c, "")

    if x == x[::-1]:
        print('Frase: ' + y + ', é palindromo')
    else:
        print('Frase: ' + y + ', não é palindromo')

aa = 'Never odd or even'                            # Frase exemplo;
print('Exemplo para a frase: Never odd or even')
frase_palindromo(aa)                                # Aplica função palindromo sobre a frase;

a = str(input('\n''Insira uma frase sem acentos: '))    # Pergunta uma frase ao ususário;
frase_palindromo(a)                                     # Aplica função palindromo sobre a frase escolhida;