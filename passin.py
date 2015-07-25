import sys
import readchar


class PassInput():
    def __init__(self):
        self.password = ''

    def passin(self):
        self.password = ''
        sys.stdout.write("Password:")
        sys.stdout.flush()
        self.letter = readchar.readkey()
        while self.letter != "\x0D":
            self.password += self.letter
            sys.stdout.write("*")
            sys.stdout.flush()
            self.letter = readchar.readkey()

        return self.password
