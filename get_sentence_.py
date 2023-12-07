import random

# Lists of possible determiners, nouns, and verbs
determiners = ['A', 'One', 'The', 'Some', 'Many']
nouns = ['cat', 'man', 'woman', 'girls', 'dogs', 'men']
verbs = ['laughed', 'eats', 'will think', 'thought', 'run', 'will write']

def main():
    for _ in range(5):
        sentence = make_sentence()
        print(sentence)

def make_sentence():
    determiner = get_determiner()
    noun = get_noun()
    verb = get_verb()
    sentence = f"{determiner} {noun} {verb}."
    return sentence

def get_determiner():
    return random.choice(determiners)

def get_noun():
    return random.choice(nouns)

def get_verb():
    return random.choice(verbs)

if __name__ == "__main__":
    main()
