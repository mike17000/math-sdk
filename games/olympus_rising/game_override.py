from game_executables import GameExecutables
from src.calculations.statistics import get_random_outcome


class GameStateOverride(GameExecutables):
    """
    This class is is used to override or extend universal state.py functions.
    e.g: A specific game may have custom book properties to reset
    """

    def reset_book(self):
        super().reset_book()

    def assign_special_sym_function(self):
        # No special symbol functions in v1 (no multipliers)
        self.special_symbol_functions = {}

    def assign_mult_property(self, symbol) -> dict:
        """Assign multiplier value to Wild symbol in freegame."""
        # v1: No multipliers, always return 1
        multiplier_value = 1
        symbol.assign_attribute({"multiplier": multiplier_value})

    def check_repeat(self):
        super().check_repeat()
        if self.repeat is False:
            win_criteria = self.get_current_betmode_distributions().get_win_criteria()
            if win_criteria is not None and self.final_win != win_criteria:
                self.repeat = True
                return
            if win_criteria is None and self.final_win == 0:
                self.repeat = True
                return
