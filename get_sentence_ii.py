import random

# Lists of possible determiners, nouns, verbs, adjectives, and prepositions
determiners = ['A', 'One', 'The', 'Some', 'Many']
nouns = ['cat', 'man', 'woman', 'girls', 'dogs', 'boys', 'house', 'bird']
verbs = {
    'present_singular': ['laughs', 'eats', 'thinks', 'runs', 'writes'],
    'present_plural': ['laugh', 'eat', 'think', 'run', 'write'],
    'past_singular': ['laughed', 'ate', 'thought', 'ran', 'wrote'],
    'past_plural': ['laughed', 'ate', 'thought', 'ran', 'wrote'],
    'future_singular': ['will laugh', 'will eat', 'will think', 'will run', 'will write'],
    'future_plural': ['will laugh', 'will eat', 'will think', 'will run', 'will write']
}
adjectives = ['red', 'happy', 'quick', 'small', 'beautiful']
adverbs = ['quickly', 'happily', 'loudly', 'softly', 'suddenly']
prepositions = ['for', 'off', 'on', 'above', 'at', 'about', 'across', 'past', 'under', 'beside']

def main():
    for i in range(5):
        sentence = make_sentence()
        print(sentence)

def make_sentence():
    determiner = get_determiner()
    noun = get_noun()
    adjective = get_adjective()
    verb = get_verb(determiner)
    preposition_phrase1 = get_prepositional_phrase("near the loft")
    preposition_phrase2 = get_prepositional_phrase("in the compound")
    
    sentence = f"{determiner} {adjective} {noun} {verb} {preposition_phrase1} and {preposition_phrase2}."
    return sentence

def get_determiner():
    return random.choice(determiners)

def get_noun():
    return random.choice(nouns)

def get_adjective():
    return random.choice(adjectives)

def get_verb(determiner):
    tense = random.choice(['present', 'past', 'future'])
    number = random.choice(['singular', 'plural'])
    
    if number == 'singular':
        verb_list = verbs[f'{tense}_singular']
    else:
        verb_list = verbs[f'{tense}_plural']
    
    return random.choice(verb_list)

def get_preposition():
    return random.choice(prepositions)

def get_prepositional_phrase(additional_word):
    preposition = get_preposition()
    determiner = get_determiner()
    noun = get_noun()
    preposition_phrase = f"{preposition} {determiner} {noun} {additional_word}"
    return preposition_phrase

if __name__ == '__main__':
    main()
