import random

class PuzzleWord:

    def __init__(self):

        self._secret_word = []
        self._word_display = []
        self._last_hint = True

    def random_word(self):

        words = ["CHAIR", "HEADPHONES", "MOUSE", "COMPUTER", "MIRROR", "DRINK" , "FLOWERS" , "SINGER"]
        self._secret_word = list(random.choice(words))
        
        for i in range(len(self._secret_word)):
            self._word_display.append(" _ ")
    
    def last_hint_correct(self, guess):

        count = self._secret_word.count(guess)

        if (count == 0):
            self._last_hint = False
        else:
            self._last_hint = True
            self._update_word_displayed(guess)

    def _update_word_displayed(self, letter):

        for i in range(len(self._secret_word)):
            if self._secret_word[i] == letter:
                self._word_display[i] = letter
        
    def correct_word_hint(self):

        secret = "".join(self._secret_word)
        word = "".join(self._word_display)

        return secret == word

    def get_word_displayed(self):

        return " ".join(self._word_display)

    def get_last_hint(self):

        return self._last_hint

    
