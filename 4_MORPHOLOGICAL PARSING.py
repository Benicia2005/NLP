class PluralFSM:
    def __init__(self):
        self.state = "START"

    def reset(self):
        """Reset the FSM to the start state."""
        self.state = "START"

    def transition(self, word):
        """Transition based on the ending of the word and generate the plural form."""
        if word.endswith(('s', 'x', 'z', 'ch', 'sh')):
            return word + 'es'
        elif word.endswith('y') and not word[-2].lower() in "aeiou":
            return word[:-1] + 'ies'
        elif word.endswith('f'):
            return word[:-1] + 'ves'
        elif word.endswith('fe'):
            return word[:-2] + 'ves'
        else:
            return word + 's'

    def pluralize(self, word):
        """Generate the plural form of the given word."""
        self.reset()
        plural_word = self.transition(word)
        return plural_word
fsm = PluralFSM()

# Test words
test_words = ["cat", "dog", "bus", "fox", "buzz", "church", "baby", "knife", "leaf", "boy", "hero"]

for word in test_words:
    plural_form = fsm.pluralize(word)
    print(f"The plural of '{word}' is '{plural_form}'.")
