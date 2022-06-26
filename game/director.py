from game.jumper import Jumper
from game.puzzle_word import PuzzleWord
from game.terminal_service import TerminalService

class Director:

    def __init__(self):
        # Initializes all the values
        self._jumper = Jumper()
        self._puzzle_word = PuzzleWord()
        self._terminal_service = TerminalService()
        self._is_playing = True

    def start_game(self):
        #Starts game
        print("\nWelcome to Jumper. Find the correct word and don't lose your parachute")
        self._puzzle_word.random_word()
        self._terminal_service.draw(self._jumper.get_parachute())

        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            self._choose_playing()

    def _get_inputs(self):
        #Guess a letter 
        guess = self._terminal_service.read_text("Guess a letter [A-Z]: ")
        self._puzzle_word.last_hint_correct(guess)

    def _do_updates(self):

        if (not self._puzzle_word.get_last_hint()):
            self._jumper.update_parachute()

        if self._puzzle_word.correct_word_hint() or not self._jumper.quantity_wrong_hints():
            self._is_playing = False

    def _do_outputs(self):
        
        self._terminal_service.write_text(self._puzzle_word.get_word_displayed())
        self._terminal_service.draw(self._jumper.get_parachute())
        if not self._is_playing:
            print("GAME OVER ♥")


    def _choose_playing(self):
        #Depending on the letter you choose the game will finalize or start again
        if not self._is_playing: 
            continue_playing = input("Do want to continue playing again? [Y/N] ")
            if continue_playing.capitalize() == "N":
                self._is_playing = False
                print("\nThanks for playing Jumper by Nadia. Have a good day\n")
            elif continue_playing.capitalize() == "Y":
                exec(open("./__main__.py").read())
            else:
                print("\nSelect a correct letter")
                self._choose_playing()

