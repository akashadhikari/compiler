"""
Scanner implementation for micro compiler.
"""
from .errors import LexicalError

# Globals
tokens = {'BEGIN': 'BeginSym',
          'END': 'EndSym',
          'READ': 'ReadSym',
          'WRITE': 'WriteSym'}


class Scanner(object):

    def __init__(self, micro_lang):
        self.micro_lang = str(micro_lang.read()).rstrip('\n');
        self.buffer = ''
        self.i = iter(self.micro_lang)

    def read(self):
        try:
            return self.micro_lang[0]
        except IndexError:
            return 'EofSym'

    def buffer_char(self, c):
        self.buffer += c

    def inspect(self, i):
        try:
            return self.micro_lang[i+1]
        except IndexError:
            return ''

    def advance(self, i):
        try:
            self.micro_lang = self.micro_lang[i+1:]
        except IndexError:
            self.micro_lang = ''

    def check_reserved(self):
        if self.buffer in tokens:
            return tokens[self.buffer]
        else:
            return 'Id'

    def check_none(self, c):
        return c == ' ' or \
               c == '\t' or \
               c == '\n'

    def check_alpha(self, c, beg=None):
        if beg:
            return c.isalpha() and c.lower or \
                   c.isalpha() and c.upper
        else:
            return c.isalpha() and c.lower or \
                   c.isalpha() and c.upper or \
                   c.isdigit() or c == '_'

    def check_int_literal(self, c):
        return c.isdigit()
    def check_lparen(self, c):
        return c == '('
    def check_rparen(self, c):
        return c == ')'
    def check_scolon(self, c):
        return c == ';'
    def check_comma(self, c):
        return c == ','
    def check_plus(self, c):
        return c == '+'
    def check_colon(self, c):
        return c == ':'
    def check_assignment(self, c):
        return c == '='
    def check_minus(self, c):
        return c == '-'

    def scan(self):
        # Clear the buffer
        self.buffer = ''

        # Check for EOF
        if self.micro_lang == '$':
            return 'EofSym'

        # Loop through our Micro Lang
        else:
            while True:
                i = 0
                char = self.read()

                # Check if the char should be ignored
                if self.check_none(char):
                    self.advance(i)
                    continue

                # Check if alpha, if so grab th token
                if self.check_alpha(char, beg=True):
                    self.buffer_char(char)
                    while True:
                        next_char = self.inspect(i)
                        if self.check_alpha(next_char):
                            self.buffer_char(next_char)
                            self.advance(i)

                        else:
                            self.advance(i)
                            return self.check_reserved()

                # Check for IntLiterals
                if self.check_int_literal(char):
                    self.buffer_char(char)
                    while True:
                        next_char = self.inspect(i)
                        if self.check_int_literal(next_char):
                            self.buffer_char(next_char)
                            self.advance(i)
                        else:
                            self.advance(i)
                            return 'IntLiteral'

                # Check for misc. chars
                if self.check_lparen(char):
                    self.advance(i)
                    return 'LParen'
                if self.check_rparen(char):
                    self.advance(i)
                    return 'RParen'
                if self.check_scolon(char):
                    self.advance(i)
                    return 'SemiColon'
                if self.check_comma(char):
                    self.advance(i)
                    return 'Comma'
                if self.check_plus(char):
                    self.advance(i)
                    return 'PlusOp'

                # Check for assignment
                if self.check_colon(char):
                    next_char = self.inspect(i)
                    if self.check_assignment(next_char):
                        self.advance(1)
                        return 'AssignOp'
                    else:
                        raise LexicalError(next_char)

                # Check for comments or MinusOp
                if self.check_minus(char):
                    next_char = self.inspect(i)
                    if self.check_minus(next_char):
                        while char != '\n':
                            self.advance(i)
                            char = self.read()
                    else:
                        self.advance(i)
                        return 'MinusOp'
                else:
raise LexicalError(char)
