import random

def get_words(length_words, num_words, words):
    words_of_length = get_words_list_of_length(length_words, words)
    return map(lambda x:words_of_length[x].upper(), gen_random_numbers(
        len(words_of_length), num_words))

def get_words_list():
    with open('enable1.txt', 'r') as f:
        return map(lambda x:x.strip(), f.readlines())

def get_words_list_of_length(length_words, words_list):
    return filter(lambda x: len(x) == length_words, words_list)

def gen_random_numbers(max_random, num_randoms):
    return random.sample(range(max_random), num_randoms)

def display_words(words):
    print '\n'.join(words)

def display_num_correct(num_correct, length_word):
    print str(num_correct) + ' of ' + str(length_word) + ' Correct'

def check_num_correct(guess, answer):
    return len([True for x in xrange(len(guess))if guess[x] == answer[x]])

if __name__ == '__main__':
    LENGTH_WORDS, NUM_WORDS = (6, 8)

    words = get_words(LENGTH_WORDS, NUM_WORDS, get_words_list())
    answer = get_words(LENGTH_WORDS, 1, words)[0]
    display_words(words)

    num_guess = 0
    while num_guess < 4:
        guess = raw_input('Guess %s of 4: ' %(str(num_guess+1))).upper()
        if guess not in words:
            print 'Illegal Guess'
            continue
        elif guess == answer:
            print 'CORRECT'
            break
        num_guess += 1
        display_num_correct(check_num_correct(guess, answer), LENGTH_WORDS)

