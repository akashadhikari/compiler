"""
Errors for the compiler
"""

class CompilerError(Exception):
    """
    Base class for exceptions in this compiler module.
    """
    pass

class LexicalError(CompilerError):
    """
    Exception raised when a lexical error is detected.
    """
    def __init__(self, bad_char):
        self.err = bad_char


class SyntaxError(CompilerError):
    """
    Exception raised when a syntax error is detected.
    """
    def __init__(self, syn_err):
        self.err = syn_err

class OpError(CompilerError):
    """
    Exception raised when a invalid operater is detected.
    """
    def __init__(self, typ_error):
        self.err = typ_error

class LiteralError(CompilerError):
    """
    Exception raised when a invalid Id is detected.
    """
    def __init__(self, lit_error):
        self.err = lit_error

class IdError(CompilerError):
    """
    Exception raised when a invalid Id is detected.
    """
    def __init__(self, id_error):
self.err = id_error
