class FiniteStateAutomaton:
    def __init__(self):
        self.start_state = 0
        self.state_a = 1
        self.accept_state = 2

        # Set the current state to start
        self.current_state = self.start_state

    def reset(self):
        """Reset the FSA to the start state."""
        self.current_state = self.start_state

    def transition(self, char):
        """Transition to the next state based on the input character."""
        if self.current_state == self.start_state:
            if char == 'a':
                self.current_state = self.state_a
            else:
                self.reset()

        elif self.current_state == self.state_a:
            if char == 'b':
                self.current_state = self.accept_state
            else:
                self.reset()

        elif self.current_state == self.accept_state:
            if char == 'a':
                self.current_state = self.state_a
            else:
                self.reset()

    def is_accepting(self):
        """Check if the FSA is in the accepting state."""
        return self.current_state == self.accept_state

    def recognize(self, string):
        """Process the string through the FSA to determine if it's recognized."""
        self.reset()
        for char in string:
            self.transition(char)
        return self.is_accepting()


# Test the FSA with some example strings
fsa = FiniteStateAutomaton()

# Test strings
test_strings = ["ab", "aab", "bba", "babab", "aaaaab"]

for s in test_strings:
    if fsa.recognize(s):
        print(f"'{s}' is recognized by the FSA (ends with 'ab').")
    else:
        print(f"'{s}' is NOT recognized by the FSA (does not end with 'ab').")
