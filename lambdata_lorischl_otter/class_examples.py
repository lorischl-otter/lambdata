# Generate an example class for practice

from random import random


class Coinflips():
    """
    Simulate a heads/tails coinflip, with an option
    to change frequency of each.
    """

    def __init__(self, rounds=0, heads_frequency=.5,
                 tails='Tails', heads='Heads'):
        """Initialize class."""
        self.rounds = rounds
        self.heads_frequency = heads_frequency
        self.tails = tails
        self.heads = heads

    def add_round(self):
        """Increase rounds by 1."""
        self.rounds += 1

    def flip(self):
        """Generate flip outcome."""
        return self.heads if random() <= self.heads_frequency else self.tails
