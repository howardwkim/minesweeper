class Cell():
    def __init__(self):
        self.is_mine = False
        self.adjacent_mines = 0
        self._is_hidden = True
        self._shown_value = '-'

    def _reveal_value(self):
        self._set_hidden_to_false()
        if self.is_mine:
            self._shown_value = '*'
        elif self.adjacent_mines == 0:
            self._shown_value = ' '
        else:  # not self.mine and self.value != 0
            self._shown_value = self.adjacent_mines

    def increment_mine_hint(self):
        self.adjacent_mines += 1

    def set_mine(self):
        self.is_mine = True

    def get_is_hidden(self):
        return self._is_hidden

    def _set_hidden_to_false(self):
        self._is_hidden = False
