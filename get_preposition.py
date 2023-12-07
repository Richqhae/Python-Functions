import random

# Lists of possible determiners, nouns, verbs, and prepositions
determiners = ['A', 'One', 'The', 'Some', 'Many']
nouns = ['cat', 'man', 'woman', 'girls', 'dogs', 'men', 'bird', 'child', 'car', 'rabbit', 'children', 'cats']
verbs = ['talked', 'drinks', 'will run', 'drank', 'laugh', 'will talk']
prepositions = ['for', 'off', 'on', 'above', 'at', 'about']

def main():
    for _ in range(5):
        sentence = make_sentence()
        print(sentence)

def make_sentence():
    determiner = get_determiner()
    noun = get_noun()
    verb = get_verb()
    prepositional_phrase = get_prepositional_phrase()
    sentence = f"{determiner} {noun} {verb} {prepositional_phrase}."
    return sentence

def get_determiner():
    return random.choice(determiners)

def get_noun():
    return random.choice(nouns)

def get_verb():
    return random.choice(verbs)

def get_preposition():
    return random.choice(prepositions)

def get_prepositional_phrase():
    preposition = get_preposition()
    determiner = get_determiner()
    noun = get_noun()
    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase

if __name__ == "__main__":
    main()
