import random

# Lists of possible determiners, nouns, and verbs
determiners = ['A', 'One', 'The', 'Some', 'Many']
nouns = ['cat', 'man', 'woman', 'girls', 'dogs', 'boys','house','bird']
verbs = ['laughed', 'eats', 'will think', 'thought', 'run', 'will write']
prepositions = ['for', 'off', 'on', 'above', 'at', 'about', 'across', 'past']

def main():
    for i in range(5):
        sentence = make_sentence()
        print(sentence)

def make_sentence():
    determiner = get_determiner()
    noun = get_noun()
    verb = get_verb()
    preposition_phrase =get_preposition_phrase()
    sentence =f"{determiner} {noun} {verb} {preposition_phrase}."
    return sentence

def get_determiner():
    return random.choice (determiners)

def get_noun():
    return random.choice(nouns)

def get_verb():
    return random.choice(verbs)

def get_preposition():
    return random.choice(prepositions)

def get_preposition_phrase():
    preposition = get_preposition()
    determiner = get_determiner()
    noun = get_noun()
    preposition_phrase = f"{preposition} {determiner} {noun}"
    return preposition_phrase


if __name__ == '__main__':
    main() 