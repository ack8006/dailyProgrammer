import random

def random_word(pattern):
    new_word = ''
    for char in pattern:
        new_letter = random.choice(letter_dict[char.lower()])
        if char in ['C','V']:
            new_letter = new_letter.upper()
        new_word += new_letter
    return new_word

while True:
    letter_dict = {'c': 'bcdfghjklmnpqrstvwxyz',
                'v': 'aeiou'}

    pattern = raw_input()
    if pattern.lower().replace('c','').replace('v',''):
        print 'Input must be upper or lower c or v'
    else:
        print random_word(pattern)
