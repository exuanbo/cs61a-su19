"""This module implements the built-in data types of the Scheme language, along
with a parser for Scheme expressions.

In addition to the types defined in this file, some data types in Scheme are
represented by their corresponding type in Python:
    number:       int or float
    symbol:       string
    boolean:      bool
    unspecified:  None

The __repr__ method of a Scheme value will return a Python expression that
would be evaluated to the value, where possible.

The __str__ method of a Scheme value will return a Scheme expression that
would be read to the value, where possible.
"""

from __future__ import print_function  # Python 2 compatibility

import numbers

from ucb import main, trace, interact
from scheme_tokens import tokenize_lines, DELIMITERS
from buffer import Buffer, InputReader, LineReader
import scheme

# Pairs and Scheme lists

class Pair(object):
    """A pair has two instance attributes: first and second. Second must be a Pair or nil

    >>> s = Pair(1, Pair(2, nil))
    >>> s
    Pair(1, Pair(2, nil))
    >>> print(s)
    (1 2)
    >>> print(s.map(lambda x: x+4))
    (5 6)
    """
    def __init__(self, first, second):
        from scheme_builtins import scheme_valid_cdrp, SchemeError
        if not (second is nil or isinstance(second, Pair) or type(second).__name__ == 'Promise'):
            raise SchemeError("cdr can only be a pair, nil, or a promise but was {}".format(second))
        self.first = first
        self.second = second

    def __repr__(self):
        return 'Pair({0}, {1})'.format(repr(self.first), repr(self.second))

    def __str__(self):
        s = '(' + repl_str(self.first)
        second = self.second
        while isinstance(second, Pair):
            s += ' ' + repl_str(second.first)
            second = second.second
        if second is not nil:
            s += ' . ' + repl_str(second)
        return s + ')'

    def __len__(self):
        n, second = 1, self.second
        while isinstance(second, Pair):
            n += 1
            second = second.second
        if second is not nil:
            raise TypeError('length attempted on improper list')
        return n

    def __eq__(self, p):
        if not isinstance(p, Pair):
            return False
        return self.first == p.first and self.second == p.second

    def map(self, fn):
        """Return a Scheme list after mapping Python function FN to SELF."""
        mapped = fn(self.first)
        if self.second is nil or isinstance(self.second, Pair):
            return Pair(mapped, self.second.map(fn))
        else:
            raise TypeError('ill-formed list (cdr is a promise)')

class nil(object):
    """The empty list"""

    def __repr__(self):
        return 'nil'

    def __str__(self):
        return '()'

    def __len__(self):
        return 0

    def map(self, fn):
        return self

nil = nil() # Assignment hides the nil class; there is only one instance

# Scheme list parser

# Quotation markers
quotes = {"'":  'quote',
          '`':  'quasiquote',
          ',':  'unquote'}

def scheme_read(src):
    """Read the next expression from SRC, a Buffer of tokens.

    >>> scheme_read(Buffer(tokenize_lines(['nil'])))
    nil
    >>> scheme_read(Buffer(tokenize_lines(['1'])))
    1
    >>> scheme_read(Buffer(tokenize_lines(['true'])))
    True
    >>> scheme_read(Buffer(tokenize_lines(['(+ 1 2)'])))
    Pair('+', Pair(1, Pair(2, nil)))
    """
    if src.current() is None:
        raise EOFError
    val = src.remove_front() # Get the first token
    if val == 'nil':
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        # END PROBLEM 2
    elif val == '(':
        # BEGIN PROBLEM 2
        "*** YOUR CODE HERE ***"
        # END PROBLEM 2
    elif val in quotes:
        # BEGIN PROBLEM 7
        "*** YOUR CODE HERE ***"
        # END PROBLEM 7
    elif val not in DELIMITERS:
        return val
    else:
        raise SyntaxError('unexpected token: {0}'.format(val))

def read_tail(src):
    """Return the remainder of a list in SRC, starting before an element or ).

    >>> read_tail(Buffer(tokenize_lines([')'])))
    nil
    >>> read_tail(Buffer(tokenize_lines(['2 3)'])))
    Pair(2, Pair(3, nil))
    """
    try:
        if src.current() is None:
            raise SyntaxError('unexpected end of file')
        elif src.current() == ')':
            # BEGIN PROBLEM 2
            "*** YOUR CODE HERE ***"
            # END PROBLEM 2
        else:
            # BEGIN PROBLEM 2
            "*** YOUR CODE HERE ***"
            # END PROBLEM 2
    except EOFError:
        raise SyntaxError('unexpected end of file')

# Convenience methods

def buffer_input(prompt='scm> '):
    """Return a Buffer instance containing interactive input."""
    return Buffer(tokenize_lines(InputReader(prompt)))

def buffer_lines(lines, prompt='scm> ', show_prompt=False):
    """Return a Buffer instance iterating through LINES."""
    if show_prompt:
        input_lines = lines
    else:
        input_lines = LineReader(lines, prompt)
    return Buffer(tokenize_lines(input_lines))

def read_line(line):
    """Read a single string LINE as a Scheme expression."""
    return scheme_read(Buffer(tokenize_lines([line])))

def repl_str(val):
    """Should largely match str(val), except for booleans and undefined."""
    if val is True:
        return "#t"
    if val is False:
        return "#f"
    if val is None:
        return "undefined"
    if isinstance(val, numbers.Number) and not isinstance(val, numbers.Integral):
        return repr(val)  # Python 2 compatibility
    return str(val)

# Interactive loop
def read_print_loop():
    """Run a read-print loop for Scheme expressions."""
    while True:
        try:
            src = buffer_input('read> ')
            while src.more_on_line:
                expression = scheme_read(src)
                if expression == 'exit':
                    print()
                    return
                print('str :', expression)
                print('repr:', repr(expression))
        except (SyntaxError, ValueError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            print()
            return

@main
def main(*args):
    if len(args) and '--repl' in args:
        read_print_loop()