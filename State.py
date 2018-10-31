FINISH_STATE = 'FINISH'


class StateStack(object):
    """
    Holds game states in a stack.
    The current game stack is at the top of the stack
    """
    def __init__(self):
        self._state_stack = []

    def size(self):
        return len(self._state_stack)

    def is_empty(self):
        return not self._state_stack

    def pop(self):
        """
        pops current state object and returns it
        """
        return self._state_stack.pop()

    def push(self, state):
        self._state_stack.append(state)

    def get_current_state(self):
        return self._state_stack[-1]

    def run_current_state(self):
        if self.get_current_state().state.state_run() == FINISH_STATE:
            self.get_current_state().state.delete()
            self.pop()


class State(object):
    def __init__(self, input_handler, update, draw, on_delete, screen, stack):
        """
        Every state object should implement all of these arguments.
        TODO: Figure out how to use ABC in a way that
              is compatible with python 2.7 and 3
        """
        if None in [input_handler, update, draw, on_delete]:
            raise ValueError('All state arguments must be defined functions')

        self.input_handler = input_handler
        self.update = update
        self.draw = draw
        self.delete = on_delete
        self.screen = screen
        self.stack = stack

    def state_run(self):
        """
        Input handler result used to inform state stack when
        the state should be popped
        """
        result = self.input_handler()
        self.update()
        self.draw()
        return result

    @property
    def screen(self):
        return self._screen

    @screen.setter
    def screen(self, screen):
        self._screen = screen
