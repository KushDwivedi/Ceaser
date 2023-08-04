'This is for lower case letters'
import string

plain_text="olssv dvysk"

shift=26-7
shift %=26
alphabet=string.ascii_lowercase
shifted=alphabet[shift:] + alphabet[:shift]
table=str.maketrans(alphabet,shifted)
encrypted=plain_text.translate(table)
print(encrypted)



'This is for Letters and Punctuation'

import string
def ceasar(text,shift,alphabets):

    def shift_alphabet(alphabet):
        return alphabet[shift:]+ alphabet[:shift]

    shift_alphabet=tuple(map(shift_alphabet,alphabets))
    final_alphabet=''.join(alphabets)
    final_sdhifted_alphabet = ''.join(shift_alphabet)
    table=str.maketrans(final_alphabet,final_sdhifted_alphabet)
    return text.translate(table)

plain_text="This is a new tesr Kush !$%"
print(ceasar(plain_text,7,[string.ascii_lowercase,string.ascii_uppercase,string.punctuation]))


