'''caesar cipher using UTF-8 character substitution'''

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M'
            , 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
            , 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
            , 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_key(letter_in):
    '''returns letters index in alphabet'''
    for index , alphabet_letter in enumerate(alphabet):
        if alphabet_letter == letter_in:
            return index

USER_TEXT = ''
dec_key = int(input('enter a key for decryption:'))
print('enter your text, type "." on a line by itself to decrypt:')

while True:
    user_in = input()
    if user_in == '.':
        break
    USER_TEXT +=  user_in + '\n'
USER_TEXT = USER_TEXT.removesuffix('\n')

DECRYPTED_TEXT = ''
for letter in USER_TEXT:
    if letter not in alphabet:
        DECRYPTED_TEXT += letter
        continue
    key = get_key(letter)
    DECRYPTED_TEXT += alphabet[(key + dec_key)%52]
print('this is the decrypted text using key:',key)
print(DECRYPTED_TEXT)
