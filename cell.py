class Cell():
    def __init__(self, row, col):
        self.mine = False
        self.value = 0
        self._hidden = True

    def _reveal_value(self):
        self._set_hidden_to_false()
        if self.mine:
            return '*'
        elif self.value == 0:
            return ' '

        else:  # not self.mine and self.value != 0
            return self.value

    def _is_hidden(self):
        return self._hidden

    def _set_hidden_to_false(self):
        self._hidden = False
